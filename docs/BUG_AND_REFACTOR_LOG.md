# TDD Refactoring and Evidence Log

The current regression suite contains 32 tests. The entries below retain the original bug evidence and identify the tests that protect each fix.

## Issue 1: Missing Validation for Non-Numeric Elements in DataScaler

- **Issue/Bug**: `min_max_scale` raised generic `TypeError` during comparison loop when list contained invalid types.
- **What was expected**: Explicit `TypeError` with an informative error message raised early during validation.
- **What actually happened**: `TypeError: '<=' not supported between instances of 'str' and 'int'` raised ungracefully inside `min()`.
- **Steps to reproduce**: Call `DataScaler().min_max_scale([10.0, "invalid", 30.0])`.

### Before Code:
```python
def min_max_scale(self, data: list[float]) -> list[float]:
    if not data: 
        return []
    min_val = min(data)
    max_val = max(data)
    return [(x - min_val) / (max_val - min_val) for x in data]

```

* **Why the before code failed**: Iterated directly over items without validating data types upfront.

### After Code:

```python
def min_max_scale(self, data: List[Union[int, float]]) -> List[float]:
    if not isinstance(data, list):
        raise TypeError("Input data must be a list of numbers.")
    if not data:
        return []
    for item in data:
        if not isinstance(item, (int, float)) or isinstance(item, bool):
            raise TypeError(f"All items in data must be integers or floats, got: {type(item).__name__}")

```

* **Why the fix works**: Validates data types explicitly before performing arithmetic operations, guaranteeing a clean early exit.
* **Test input**: `[10.0, "invalid", 30.0]`
* **Expected result**: `TypeError("All items in data must be integers or floats, got: str")`
* **Actual result**: `TypeError("All items in data must be integers or floats, got: str")`
* **Verification status**: `PASS` (`test_min_max_scale_invalid_elements`)

---

## Issue 2: Constant Numerical Series Division by Zero Handling

* **Issue/Bug**: Constant lists (e.g., `[5.0, 5.0, 5.0]`) resulted in zero range denominator (`max_val - min_val = 0`).
* **What was expected**: Return a list of `0.0` values without throwing `ZeroDivisionError`.
* **What actually happened**: `ZeroDivisionError: float division by zero`.
* **Steps to reproduce**: Call `DataScaler().min_max_scale([5.0, 5.0, 5.0])`.

### Before Code:

```python
return [(x - min_val) / (max_val - min_val) for x in data]

```

* **Why the before code failed**: Direct division by zero when min equals max.

### After Code:

```python
range_val = max_val - min_val
if range_val == 0:
    return [0.0 for _ in data]
return [round((x - min_val) / range_val, 4) for x in data]

```

* **Why the fix works**: Explicitly checks `range_val == 0` before division to prevent runtime crash.
* **Test input**: `[5.0, 5.0, 5.0]`
* **Expected result**: `[0.0, 0.0, 0.0]`
* **Actual result**: `[0.0, 0.0, 0.0]`
* **Verification status**: `PASS` (`test_min_max_scale_constant_values`, `test_min_max_scale_single_value`)

---

## Issue 3: Pipeline Records Could Become Misaligned

* **Issue/Bug**: Text and numeric lists could have different lengths, making it impossible to associate every cleaned text value with the intended number.
* **What was expected**: Reject mismatched lists before either component processes the data.
* **Fix**: `DataPipeline.process_dataset` now raises `ValueError` with the message `text_list and number_list must contain the same number of items.`
* **Verification status**: `PASS` (`test_pipeline_mismatched_lengths`), using `assertRaisesRegex` to verify the type and message.