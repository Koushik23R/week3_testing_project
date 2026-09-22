# YuvaIntern Week 3: Writing Automated Tests for Python Applications

**Student:** Koushik R  
**Project:** Data Preprocessing Engine  
**Testing framework:** Python 3 `unittest`
**Runtime dependencies:** Python standard library only

## Project Information

The objective was to build and test a moderately complex preprocessing application with separate numerical, text, and orchestration responsibilities. The repository now contains a 32-test executable suite, measured source coverage, reproducible commands, and evidence for the TDD and refactoring work.

## Application Functionality

- **DataScaler:** validates a list of integers/floats, applies min-max scaling to `[0, 1]`, preserves order, rounds results to four decimal places, returns `[]` for empty input, and returns zeroes for a constant series.
- **TextCleaner:** validates strings, trims and lowercases them, removes punctuation, and collapses whitespace, including newlines and tabs.
- **DataPipeline:** validates paired lists and matching lengths, delegates text and number processing to the two components, and returns `cleaned_text`, `scaled_numbers`, and `record_count`.

## Testing Strategy

The suite separates component-level unit tests from end-to-end integration tests:

| Area | Evidence |
| --- | --- |
| Unit behavior | 22 tests in `tests/test_core.py` |
| Integration behavior | 10 tests in `tests/test_integration.py` |
| Boundary tests | Empty, single-value, two-value, and constant inputs |
| Edge cases | Negative, duplicate, unsorted, mixed numeric, Unicode, newline, and tab inputs |
| Negative tests | Wrong containers, invalid elements, booleans, and mismatched lengths |
| Exception validation | `assertRaisesRegex` checks type and message |

The full scenario rationale is in [`docs/TEST_CASE_CATALOG.md`](docs/TEST_CASE_CATALOG.md).

## Specific Test Examples

### Example 1 — Normal Scaling

**Input**

```text
[10, 20, 30]
```

**Expected**

```text
[0.0, 0.5, 1.0]
```

**Actual:** `[0.0, 0.5, 1.0]`
**Result:** `PASS` (`test_min_max_scale_normal`)

### Example 2 — Invalid Numeric Input

**Input**

```text
[10, "invalid", 30]
```

**Expected:** `TypeError` containing `All items in data must be integers or floats, got: str`
**Actual:** the same `TypeError` message
**Result:** `PASS` (`test_min_max_scale_invalid_elements`)

### Example 3 — Constant Series

**Input**

```text
[5.0, 5.0, 5.0]
```

**Expected:** `[0.0, 0.0, 0.0]`
**Actual:** `[0.0, 0.0, 0.0]`
**Result:** `PASS` (`test_min_max_scale_constant_values`)

### Example 4 — Text Cleaning

**Input**

```text
"  Hello, World! Welcome to AI/ML.  "
```

**Expected:** `"hello world welcome to aiml"`
**Actual:** `"hello world welcome to aiml"`
**Result:** `PASS` (`test_clean_text_normal`)

### Example 5 — End-to-End Pipeline

**Input**

```text
texts = ["  FEATURE A: high  ", "Feature B: LOW! "]
numbers = [100, 200]
```

**Expected**

```text
{
    "cleaned_text": ["feature a high", "feature b low"],
    "scaled_numbers": [0.0, 1.0],
    "record_count": 2,
}
```

**Actual:** the same dictionary
**Result:** `PASS` (`test_pipeline_end_to_end_success`)

## Test Metrics

These values are from the recorded commands in `docs/TEST_RESULTS.md` and `docs/COVERAGE_REPORT.md`:

| Metric | Actual result |
| --- | ---: |
| Total tests | 32 |
| Unit tests | 22 |
| Integration tests | 10 |
| Passed | 32 |
| Failed | 0 |
| Errors | 0 |
| Pass rate | 100% |
| Execution time | 0.007 sec |
| Source statements | 38 |
| Missed source statements | 0 |
| Source coverage | 100% |

The execution time is machine-dependent; it is the value reported by the recorded Python 3.13.3 run.

## TDD Evidence

The documented Red -> Green -> Refactor cycles cover:

1. Numerical normalization.
2. Early validation for non-numeric elements.
3. Constant-series division-by-zero prevention.
4. Pipeline length validation.

The cycle descriptions and current evidence mapping are in [`docs/TDD_EVIDENCE.md`](docs/TDD_EVIDENCE.md). Existing Git history contains the implementation phases; this resubmission adds regression tests and documentation without rewriting old commits.

## Bug and Refactoring Evidence

[`docs/BUG_AND_REFACTOR_LOG.md`](docs/BUG_AND_REFACTOR_LOG.md) records the original invalid-element and constant-series bugs, their reproduction inputs, the fixes, and verification tests.

## Documentation

- [`README.md`](README.md): setup, usage, test commands, troubleshooting, and deliverables.
- [`docs/TEST_CASE_CATALOG.md`](docs/TEST_CASE_CATALOG.md): scenario-level input, expected result, type, and rationale.
- [`docs/TEST_RESULTS.md`](docs/TEST_RESULTS.md): actual test command, environment, count, pass rate, and output.
- [`docs/COVERAGE_REPORT.md`](docs/COVERAGE_REPORT.md): actual source statement and file coverage.
- [`docs/TDD_EVIDENCE.md`](docs/TDD_EVIDENCE.md): Red -> Green -> Refactor evidence.
- [`docs/BUG_AND_REFACTOR_LOG.md`](docs/BUG_AND_REFACTOR_LOG.md): bugs and corrective refactors.

## Clean Environment Verification

The repository is self-contained at runtime. A clean setup uses:

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements-dev.txt
python -m unittest discover -s tests -v
```

The recorded metrics were produced on Windows with Python 3.13.3 from the repository root. No claim is made about a separate clean-environment run unless that command is executed in that environment.

## Requirements-to-Evidence Matrix

| YuvaIntern requirement | Evidence | Repository location |
| --- | --- | --- |
| Automated testing | 32-test suite | `tests/` |
| Unit testing | DataScaler and TextCleaner tests | `tests/test_core.py` |
| Integration testing | DataPipeline tests | `tests/test_integration.py` |
| Edge cases | Empty, constant, Unicode, whitespace, and ordering cases | `tests/` |
| Error conditions | Precise exception assertions | `tests/` |
| TDD | Red -> Green -> Refactor cycles | `docs/TDD_EVIDENCE.md` |
| Test documentation | Scenario catalog | `docs/TEST_CASE_CATALOG.md` |
| Test execution | Exact setup and commands | `README.md` |
| Results | Actual counts, output, and timing | `docs/TEST_RESULTS.md` |
| Coverage | Source-only coverage report | `docs/COVERAGE_REPORT.md` |
| Refactoring | Reproduction and fix records | `docs/BUG_AND_REFACTOR_LOG.md` |
| Reproducibility | Standard-library runtime and optional dev requirements | `README.md`, `requirements-dev.txt` |

## Deliverables

The source, tests, documentation, CI workflow, and original Word deliverable are retained in the repository. The GitHub Actions workflow at [`.github/workflows/tests.yml`](.github/workflows/tests.yml) runs the same unittest discovery command on pushes and pull requests.
