# Test Case Catalog

This catalog explains why the 32 discovered tests exist and what behavior each verifies. The two tests that use `subTest` contain multiple invalid-input scenarios; those scenarios are listed separately below, while `unittest` counts each containing method as one discovered test.

| ID | Component | Scenario | Input | Expected result | Test type | Why this test matters |
| --- | --- | --- | --- | --- | --- | --- |
| DS-01 | DataScaler | Normal positive values | `[10, 20, 30]` | `[0.0, 0.5, 1.0]` | Unit; normal | Verifies the basic min-max formula and exact endpoints. |
| DS-02 | DataScaler | Negative values | `[-10, 0, 10]` | `[0.0, 0.5, 1.0]` | Unit; normal | Confirms scaling is based on range, not sign. |
| DS-03 | DataScaler | Mixed integers and floats | `[1, 2.5, 4]` | `[0.0, 0.5, 1.0]` | Unit; normal | Confirms supported numeric types can be combined. |
| DS-04 | DataScaler | Unsorted input | `[30, 10, 20]` | `[1.0, 0.0, 0.5]` | Unit; functional | Ensures output preserves input order. |
| DS-05 | DataScaler | Duplicate values | `[10, 20, 20, 30]` | `[0.0, 0.5, 0.5, 1.0]` | Unit; functional | Confirms equal inputs receive equal normalized values. |
| DS-06 | DataScaler | Two-value boundary | `[4, 8]` | `[0.0, 1.0]` | Unit; boundary | Verifies the smallest non-constant useful range. |
| DS-07 | DataScaler | Single value | `[5]` | `[0.0]` | Unit; boundary | Confirms a one-item constant series is safe. |
| DS-08 | DataScaler | Constant series | `[5.0, 5.0, 5.0]` | `[0.0, 0.0, 0.0]` | Unit; edge case | Proves the zero-range division guard works. |
| DS-09 | DataScaler | Empty list | `[]` | `[]` | Unit; edge case | Defines behavior for an empty dataset. |
| DS-10 | DataScaler | String element | `[10, "invalid", 30]` | `TypeError`, message names `str` | Unit; invalid input | Ensures invalid data is rejected before arithmetic. |
| DS-11 | DataScaler | `None` element | `[10, None, 30]` | `TypeError`, message names `NoneType` | Unit; invalid input | Covers a common missing-value representation. |
| DS-12 | DataScaler | Boolean element | `[10, True, 30]` | `TypeError`, message names `bool` | Unit; error condition | Confirms booleans are not silently accepted as integers. |
| DS-13 | DataScaler | Tuple container | `(1, 2, 3)` | `TypeError`, list-required message | Unit; invalid input | Verifies the public API requires a list. |
| DS-14 | DataScaler | String container | `"not a list"` | `TypeError`, list-required message | Unit; invalid input | Verifies non-list scalar input is rejected. |
| TC-01 | TextCleaner | Normal text | `"  Hello, World! Welcome to AI/ML.  "` | `"hello world welcome to aiml"` | Unit; normal | Verifies trimming, lowercasing, punctuation removal, and whitespace. |
| TC-02 | TextCleaner | Uppercase and mixed case | `"PYTHON Testing MiXeD"` | `"python testing mixed"` | Unit; functional | Confirms all case patterns normalize consistently. |
| TC-03 | TextCleaner | Leading/trailing whitespace | `"   padded text   "` | `"padded text"` | Unit; boundary | Verifies outer whitespace is removed. |
| TC-04 | TextCleaner | Multiple spaces | `"one    two     three"` | `"one two three"` | Unit; functional | Confirms repeated internal whitespace collapses. |
| TC-05 | TextCleaner | Punctuation | `"Hello, world! (ready?)"` | `"hello world ready"` | Unit; functional | Verifies punctuation is stripped without leaving artifacts. |
| TC-06 | TextCleaner | Numbers in text | `"Version 3.13 released in 2026"` | `"version 313 released in 2026"` | Unit; functional | Confirms word characters and digits remain while `.` is removed. |
| TC-07 | TextCleaner | Newline and tab | `"first\nsecond\tthird"` | `"first second third"` | Unit; edge case | Verifies all whitespace is normalized, not just spaces. |
| TC-08 | TextCleaner | Empty string | `""` | `""` | Unit; boundary | Defines safe behavior for empty text. |
| TC-09 | TextCleaner | Unicode text | `"  Café déjà vu!  "` | `"café déjà vu"` | Unit; edge case | Confirms the regex behavior supports Unicode word characters. |
| TC-10 | TextCleaner | Integer input | `12345` | `TypeError`, message names `int` | Unit; invalid input | Rejects non-string values explicitly. |
| TC-11 | TextCleaner | `None` input | `None` | `TypeError`, message names `NoneType` | Unit; invalid input | Covers missing text input. |
| TC-12 | TextCleaner | List input | `["not", "text"]` | `TypeError`, message names `list` | Unit; invalid input | Prevents accidental use of collection values as text. |
| PI-01 | DataPipeline | End-to-end two records | Text and `[100, 200]` | Cleaned text, `[0.0, 1.0]`, count `2` | Integration; normal | Verifies the complete component interaction. |
| PI-02 | DataPipeline | Three records | Three texts and `[10, 20, 30]` | Three cleaned records and `[0.0, 0.5, 1.0]` | Integration; functional | Confirms results remain aligned for multiple records. |
| PI-03 | DataPipeline | Single record | `["  One! "]`, `[42]` | `["one"]`, `[0.0]`, count `1` | Integration; boundary | Covers the smallest paired dataset. |
| PI-04 | DataPipeline | Empty dataset | `[]`, `[]` | Empty outputs and count `0` | Integration; edge case | Verifies both components compose safely on no data. |
| PI-05 | DataPipeline | Constant numbers | `["A", "B", "C"]`, `[7, 7, 7]` | Three zeroes | Integration; edge case | Confirms the scaler's constant-series behavior survives integration. |
| PI-06 | DataPipeline | Mixed numeric values | Three texts and `[1, 2.5, 4]` | `[0.0, 0.5, 1.0]` | Integration; functional | Confirms numeric type support through the pipeline. |
| PI-07 | DataPipeline | Invalid numeric string | `["Sample"]`, `["invalid"]` | `TypeError`, message names `str` | Integration; error condition | Verifies scaler errors propagate through the pipeline. |
| PI-08 | DataPipeline | Boolean numeric value | `["Sample"]`, `[True]` | `TypeError`, message names `bool` | Integration; error condition | Confirms boolean rejection is retained at the boundary. |
| PI-09 | DataPipeline | Invalid text value | `[123]`, `[10]` | `TypeError`, message names `int` | Integration; error condition | Verifies cleaner validation is reached and preserved. |
| PI-10 | DataPipeline | Invalid list containers | Tuple text or tuple numbers | `TypeError`, list-required message | Integration; invalid input | Confirms both public arguments are validated as lists. |
| PI-11 | DataPipeline | Mismatched lengths | `["a", "b"]`, `[10]` | `ValueError`, same-number message | Integration; error condition | Prevents records from becoming misaligned. |
| PI-12 | DataPipeline | Record count | Any successful paired input | Count equals cleaned record count | Integration; functional | Verifies the metadata describes the returned dataset. |
| PI-13 | DataPipeline | Component interaction | Text cleaning plus scaling in one call | Both transformed fields present together | Integration; functional | Demonstrates that pipeline output is not just one component's result. |

The catalog contains 39 scenario rows because two discovered test methods use subtests for related invalid values and the pipeline result assertions cover several output requirements. The executable suite count remains 32.
