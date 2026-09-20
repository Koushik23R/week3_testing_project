# Data Preprocessing Engine

**Author:** Koushik R
**Project:** YuvaIntern Week 3 testing and TDD exercise

A small, standard-library-only Python toolkit for cleaning text, normalizing numerical data, and processing both kinds of data together.

## Features

- `DataScaler` normalizes numeric lists to the `[0, 1]` range using min-max scaling.
- `TextCleaner` trims whitespace, converts text to lowercase, removes punctuation, and collapses repeated whitespace.
- `DataPipeline` combines text cleaning and numerical scaling and returns structured results.
- Inputs are validated with clear `TypeError` and `ValueError` exceptions.
- Empty lists and constant numeric series are handled safely. A constant series returns a list of `0.0` values.
- Tests use Python's built-in `unittest` framework.

## Requirements

- Python 3.13 or a compatible Python 3 release
- No third-party runtime dependencies

The `requirements.txt` file documents the standard-library-only test setup.

## Project Structure

```text
week3_testing_project/
├── src/
│   └── data_processor/
│       ├── __init__.py
│       └── core.py
├── tests/
│   ├── __init__.py
│   ├── test_core.py
│   └── test_integration.py
├── docs/
│   ├── BUG_AND_REFACTOR_LOG.md
│   ├── TDD_EVIDENCE.md
│   └── TEST_RESULTS.md
├── README.md
├── WEEK3_REPORT.md
├── requirements.txt
└── report.docx
```

## Setup

Clone the repository, change into its directory, and confirm that Python is available:

```bash
cd week3_testing_project
python --version
```

No package installation is required.

## Usage

```python
from src.data_processor.core import DataPipeline, DataScaler, TextCleaner

scaler = DataScaler()
print(scaler.min_max_scale([10, 20, 30, 40]))
# [0.0, 0.3333, 0.6667, 1.0]

cleaner = TextCleaner()
print(cleaner.clean_text("  Hello, World! Welcome  "))
# hello world welcome

pipeline = DataPipeline()
result = pipeline.process_dataset(
    ["  FEATURE A: high  ", "Feature B: LOW! "],
    [100, 200],
)
print(result)
# {
#     "cleaned_text": ["feature a high", "feature b low"],
#     "scaled_numbers": [0.0, 1.0],
#     "record_count": 2,
# }
```

`DataPipeline.process_dataset` requires both arguments to be lists of equal length. Text values must be strings, and numeric values must be integers or floats; booleans are rejected as numeric values.

## Running Tests

Run the test discovery command from the repository root:

```bash
python -m unittest discover -s tests -v
```

The current working tree discovers 10 tests. The existing integration test fixture for invalid numeric input uses lists of different lengths, so the pipeline raises its length-mismatch `ValueError` before reaching numeric validation. The intended mismatch-length test is currently nested inside another test method and is not discovered by `unittest`.

Test and TDD records are available in:

- `docs/TEST_RESULTS.md`
- `docs/TDD_EVIDENCE.md`
- `docs/BUG_AND_REFACTOR_LOG.md`
- `WEEK3_REPORT.md`

## License

This project is intended for educational and internship use.
