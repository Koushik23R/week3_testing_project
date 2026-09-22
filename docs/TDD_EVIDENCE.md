# TDD Development and Refactoring Evidence

This document preserves the project's **Red -> Green -> Refactor** evidence. The current executable suite contains 32 tests; the historical cycles below describe the behavior that was implemented and then protected with regression tests.

## Cycle 1: Core Numerical Normalization

**Requirement:** Scale numerical lists to the range `[0, 1]`.

### RED

`test_min_max_scale_normal` was executed before the `DataScaler` implementation was available and failed with an `ImportError`.

### GREEN

`DataScaler.min_max_scale` was implemented using min-max normalization.

### REFACTOR

The result was rounded to four decimal places for consistent output. The current regression test is `TestDataScaler.test_min_max_scale_normal`.

## Cycle 2: Non-Numeric Element Validation

**Requirement:** Reject invalid elements with a clear `TypeError`.

### RED

The input `[10.0, "invalid", 30.0]` reached `min()`/`max()` without validation and produced an unhelpful comparison error.

### GREEN

Explicit validation was added before numerical calculations:

```python
for item in data:
    if not isinstance(item, (int, float)) or isinstance(item, bool):
        raise TypeError(
            f"All items in data must be integers or floats, "
            f"got: {type(item).__name__}"
        )
```

### REFACTOR

The validation now rejects strings, `None`, and booleans consistently. `test_min_max_scale_invalid_elements` and the pipeline invalid-input tests assert both type and message.

## Cycle 3: Constant-Series Division-by-Zero Handling

**Requirement:** Process a constant series without a `ZeroDivisionError`.

### RED

`[5.0, 5.0, 5.0]` produced a zero denominator when the range was calculated.

### GREEN

The implementation added a zero-range guard:

```python
range_val = max_val - min_val
if range_val == 0:
    return [0.0 for _ in data]
```

### REFACTOR

The behavior is now explicitly covered by both `test_min_max_scale_single_value` and `test_min_max_scale_constant_values`, plus the pipeline constant-number integration test.

## Cycle 4: Data Pipeline Input Validation

**Requirement:** Keep paired text and numerical records aligned.

### RED

The initial pipeline accepted lists with different lengths and could not guarantee record alignment.

### GREEN

Length validation was added:

```python
if len(text_list) != len(number_list):
    raise ValueError(
        "text_list and number_list must contain the same number of items."
    )
```

### REFACTOR

`test_pipeline_mismatched_lengths` now uses `assertRaisesRegex`, and the integration suite also checks invalid list containers, invalid text, numeric validation propagation, empty input, and output metadata.

## Evidence Map

| TDD concern | Current evidence |
| --- | --- |
| Numerical normalization | `tests/test_core.py`, `DataScaler` tests |
| Invalid numeric input | `test_min_max_scale_invalid_elements`, pipeline invalid numeric tests |
| Constant-series safety | `test_min_max_scale_constant_values`, pipeline constant test |
| Pipeline alignment | `test_pipeline_mismatched_lengths` |
| Refactoring record | `docs/BUG_AND_REFACTOR_LOG.md` |
| Scenario rationale | `docs/TEST_CASE_CATALOG.md` |
