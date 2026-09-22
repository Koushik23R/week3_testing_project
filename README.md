# Data Preprocessing Engine

## 1. Project Title

**Writing Automated Tests for Python Applications — YuvaIntern Week 3**

## 2. Project Overview

The Data Preprocessing Engine is a small, standard-library Python application for preparing paired text and numerical data. It cleans text records, scales numerical values to the `[0, 1]` range, and combines both operations into a structured pipeline result.

## 3. Week 3 Objective

This project demonstrates automated testing of a moderately complex Python application. The test suite uses Python's built-in `unittest` framework to show unit testing, integration testing, boundary and edge-case coverage, precise exception assertions, and reproducible test execution.

## 4. Features

- **Numerical scaling:** `DataScaler` performs min-max scaling and returns rounded floats.
- **Text cleaning:** `TextCleaner` trims whitespace, lowercases text, removes punctuation, and normalizes whitespace.
- **Integrated preprocessing:** `DataPipeline` combines both components and returns cleaned text, scaled numbers, and a record count.
- **Validation:** list types, item types, and matching input lengths are checked before processing.
- **Error handling:** invalid inputs raise explicit `TypeError` or `ValueError` messages.
- **Boundary behavior:** empty lists and constant numerical series are handled without runtime errors.

## 5. Architecture

```text
DataPipeline
├── TextCleaner
└── DataScaler
```

`DataPipeline` owns one `TextCleaner` and one `DataScaler`, so the integration tests verify both component interaction and the final structured output.

## 6. Project Structure

```text
week3_testing_project/
├── .github/
│   └── workflows/
│       └── tests.yml
├── docs/
│   ├── BUG_AND_REFACTOR_LOG.md
│   ├── COVERAGE_REPORT.md
│   ├── TDD_EVIDENCE.md
│   ├── TEST_CASE_CATALOG.md
│   └── TEST_RESULTS.md
├── src/
│   └── data_processor/
│       ├── __init__.py
│       └── core.py
├── tests/
│   ├── __init__.py
│   ├── test_core.py
│   └── test_integration.py
├── .gitignore
├── README.md
├── requirements-dev.txt
├── requirements.txt
├── WEEK3_REPORT.md
└── report.docx
```

## 7. Requirements

- Python 3.10 or later (verified here with Python 3.13.3).
- No third-party runtime dependencies; the application uses the Python standard library.
- `coverage` is an optional development tool for measuring source coverage and is listed in `requirements-dev.txt`.

## 8. Installation

```bash
git clone https://github.com/Koushik23R/week3_testing_project.git
cd week3_testing_project
python -m venv .venv
```

Activate the virtual environment:

```bash
# Windows PowerShell
.venv\Scripts\Activate.ps1

# macOS/Linux
source .venv/bin/activate
```

The application and tests need no package installation. To install the optional coverage tool:

```bash
python -m pip install -r requirements-dev.txt
```

## 9. Running the Application

From the repository root:

```bash
python -c "from src.data_processor.core import DataPipeline; print(DataPipeline().process_dataset(['  Feature A! ', 'Feature B'], [100, 200]))"
```

Expected structure:

```text
{'cleaned_text': ['feature a', 'feature b'], 'scaled_numbers': [0.0, 1.0], 'record_count': 2}
```

## 10. Running All Tests

```bash
python -m unittest discover -s tests -v
```

The final recorded run discovers 32 tests.

## 11. Running Unit Tests Only

```bash
python -m unittest tests.test_core -v
```

## 12. Running Integration Tests Only

```bash
python -m unittest tests.test_integration -v
```

## 13. Running a Specific Test

```bash
python -m unittest tests.test_core.TestDataScaler.test_min_max_scale_normal -v
```

## 14. Test Strategy

- **Unit tests:** isolate `DataScaler` and `TextCleaner` behavior.
- **Integration tests:** exercise `DataPipeline` from input validation through the combined result.
- **Normal and boundary tests:** cover typical values, two-value and single-value lists, empty input, and constant series.
- **Edge-case tests:** cover negative, duplicate, unsorted, mixed numeric, Unicode, newline, and tab input.
- **Invalid-input tests:** cover wrong container types, invalid elements, booleans, and mismatched lengths.
- **Exception tests:** use `assertRaisesRegex` to check both exception type and meaningful message.

The complete scenario-to-evidence mapping is in [`docs/TEST_CASE_CATALOG.md`](docs/TEST_CASE_CATALOG.md).

## 15. Test Metrics

The recorded full-suite run used Python 3.13.3 and `unittest`:

| Metric | Actual result |
| --- | ---: |
| Total tests | 32 |
| Passed | 32 |
| Failed | 0 |
| Errors | 0 |
| Pass rate | 100% |
| Execution time | 0.007 sec |
| Source coverage | 100% (38 statements) |

Detailed command output is in [`docs/TEST_RESULTS.md`](docs/TEST_RESULTS.md), and coverage details are in [`docs/COVERAGE_REPORT.md`](docs/COVERAGE_REPORT.md).

## 16. Test Case Documentation

[`docs/TEST_CASE_CATALOG.md`](docs/TEST_CASE_CATALOG.md) documents each important scenario, input, expected result, test type, and reason for inclusion.

## 17. TDD Process

Development followed:

```text
RED → GREEN → REFACTOR
```

The existing evidence records cycles for numerical normalization, invalid numeric input, constant-series handling, and pipeline length validation. See [`docs/TDD_EVIDENCE.md`](docs/TDD_EVIDENCE.md).

## 18. Bug and Refactoring Evidence

[`docs/BUG_AND_REFACTOR_LOG.md`](docs/BUG_AND_REFACTOR_LOG.md) records the invalid-element validation and constant-series division-by-zero fixes, including reproduction inputs and verification tests.

## 19. Coverage

Install coverage with `python -m pip install -r requirements-dev.txt`, then run:

```bash
coverage run --source=src -m unittest discover -s tests
coverage report -m
```

See [`docs/COVERAGE_REPORT.md`](docs/COVERAGE_REPORT.md) for the actual file-by-file result.

## 20. Clean Environment Verification

The reproducible setup is:

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements-dev.txt
python -m unittest discover -s tests -v
```

The application has no runtime dependency beyond Python. The documented results were produced from the repository root with Python 3.13.3; a clean-environment run should be compared with the same command rather than relying on cached bytecode.

## 21. Expected Output

The successful full-suite run ends with:

```text
Ran 32 tests in 0.007s

OK
```

The exact duration can vary by machine; the complete recorded output is preserved in `docs/TEST_RESULTS.md`.

## 22. Troubleshooting

- **Python version:** use Python 3.10 or later and confirm with `python --version`.
- **Incorrect working directory:** run commands from the repository root containing `README.md` and `tests/`.
- **Test discovery issues:** use the exact command `python -m unittest discover -s tests -v`.
- **Import errors:** keep the `src` directory in the repository root and invoke tests with `python -m`, not by running a test file from inside `tests`.
- **Missing coverage command:** install the optional development dependency with `python -m pip install -r requirements-dev.txt`.
- **PowerShell activation policy:** if activation is blocked, run the test command with the virtual environment interpreter directly: `.venv\Scripts\python.exe -m unittest discover -s tests -v`.

## 23. Deliverables

- Source implementation: [`src/data_processor/core.py`](src/data_processor/core.py)
- Unit tests: [`tests/test_core.py`](tests/test_core.py)
- Integration tests: [`tests/test_integration.py`](tests/test_integration.py)
- Test catalog: [`docs/TEST_CASE_CATALOG.md`](docs/TEST_CASE_CATALOG.md)
- Test results: [`docs/TEST_RESULTS.md`](docs/TEST_RESULTS.md)
- Coverage report: [`docs/COVERAGE_REPORT.md`](docs/COVERAGE_REPORT.md)
- TDD evidence: [`docs/TDD_EVIDENCE.md`](docs/TDD_EVIDENCE.md)
- Bug/refactoring log: [`docs/BUG_AND_REFACTOR_LOG.md`](docs/BUG_AND_REFACTOR_LOG.md)
- Week 3 report: [`WEEK3_REPORT.md`](WEEK3_REPORT.md)
- CI workflow: [`.github/workflows/tests.yml`](.github/workflows/tests.yml)
