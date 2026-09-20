# Comprehensive TDD Development & Refactoring Trail

This document details the **Test-Driven Development (TDD) lifecycle — Red → Green → Refactor** followed during the development of the Data Preprocessing Engine.

---

## Cycle 1: Core Numerical Normalization

**Requirement:**
Scale numerical lists to the range `[0, 1]`.

### RED Phase

Executed `test_min_max_scale_normal` before the `DataScaler` implementation was available, resulting in an `ImportError`.

### GREEN Phase

Implemented the `min_max_scale` method to process valid numerical lists using Min-Max normalization.

### REFACTOR Phase

Improved the implementation by rounding the resulting values to **4 decimal places** for consistent output.

---

## Cycle 2: Non-Numeric Element Validation

**Requirement:**
Reject lists containing non-numeric elements, such as strings mixed with numerical values, with an explicit `TypeError`.

### RED Phase

Tested the input:

```python
[10.0, "invalid", 30.0]
```

The implementation failed during the `min()`/`max()` calculation because the input contained an invalid data type.

### GREEN Phase

Added explicit input validation before performing numerical calculations:

```python
for item in data:
    if not isinstance(item, (int, float)) or isinstance(item, bool):
        raise TypeError(
            f"All items in data must be integers or floats, "
            f"got: {type(item).__name__}"
        )
```

### REFACTOR Phase

Ensured that invalid elements are detected before any `min()` or `max()` operation is performed, resulting in a clear and predictable error.

---

## Cycle 3: Division-by-Zero Handling

**Requirement:**
Prevent errors when all values in the input list are identical.

Example:

```python
[5.0, 5.0, 5.0]
```

### RED Phase

Executed the constant-value test before adding zero-range handling. The implementation resulted in a `ZeroDivisionError`.

### GREEN Phase

Added a zero-range check:

```python
range_val = max_val - min_val

if range_val == 0:
    return [0.0 for _ in data]
```

### REFACTOR Phase

Verified that constant numerical input is handled safely and produces:

```python
[0.0, 0.0, 0.0]
```

---

## Cycle 4: Data Pipeline Input Validation

**Requirement:**
Ensure that `DataPipeline` rejects mismatched text and numerical input lengths.

### RED Phase

Executed `test_pipeline_mismatched_lengths`. The initial implementation allowed inputs with different lengths to be processed without raising an appropriate error.

### GREEN Phase

Added explicit length validation:

```python
if len(text_list) != len(number_list):
    raise ValueError(
        "text_list and number_list must contain the same number of items."
    )
```

### REFACTOR Phase

Verified that mismatched input lengths are rejected cleanly with an explicit `ValueError`.

---

## TDD Summary

The development process followed the **Red → Green → Refactor** methodology:

1. **Red** — Identify a failing test or missing behaviour.
2. **Green** — Implement the minimum required functionality to satisfy the requirement.
3. **Refactor** — Improve validation, readability, consistency, and robustness while keeping the tests passing.

The TDD cycles covered numerical normalization, input validation, division-by-zero handling, and end-to-end data pipeline validation.
