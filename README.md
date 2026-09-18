## Author: Koushik R
## Role: Junior Python Developer (YuvaIntern)

# Data Preprocessing Engine

A lightweight Python project for cleaning text and normalizing numerical data for machine learning and data preparation workflows. The project follows a Test-Driven Development (TDD) approach and includes both unit tests and integration tests for validation.

## Overview

This repository contains a simple data processing toolkit with three main components:

- `DataScaler`: normalizes numeric lists into a min-max range of `[0, 1]`
- `TextCleaner`: trims whitespace, lowercases strings, removes punctuation, and collapses repeated spaces
- `DataPipeline`: combines both operations into a single end-to-end processing workflow

## Key Features

- Strict input validation for numeric and string data
- Safe handling of empty input lists
- Protection against division-by-zero when all numeric values are identical
- Clean, reproducible preprocessing logic for ML-style datasets
- Unit and integration tests for functional correctness

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
│   └── BUG_AND_REFACTOR_LOG.md
├── README.md
├── requirements.txt
├── .gitignore
└── report.doc
```

## Requirements

This project uses the Python standard library only, so no external dependencies are required.

```bash
python --version
```

## Setup

1. Clone the repository
2. Open the project folder in your terminal
3. Ensure Python 3 is available

```bash
cd week3_testing_project
```

## Usage

```python
from src.data_processor.core import DataScaler, TextCleaner, DataPipeline

scaler = DataScaler()
print(scaler.min_max_scale([10, 20, 30, 40]))
# Output: [0.0, 0.3333, 0.6667, 1.0]

cleaner = TextCleaner()
print(cleaner.clean_text("  Hello, World! Welcome  "))
# Output: "hello world welcome"

pipeline = DataPipeline()
result = pipeline.process_dataset(
    ["  FEATURE A: high  ", "Feature B: LOW! "],
    [100, 200]
)
print(result)
```

Expected output includes:

```python
{
    "cleaned_text": ["feature a high", "feature b low"],
    "scaled_numbers": [0.0, 1.0],
    "record_count": 2
}
```

## Running Tests

Use the built-in unittest framework:

```bash
python -m unittest discover -s tests -v
```

This project includes:

- Unit tests for `DataScaler` and `TextCleaner`
- Integration tests for `DataPipeline`

## TDD and Refactoring Notes

The codebase was developed with a TDD workflow, including input validation and bug-fix tracking. See the documentation log for details on refactors and verification:

- `docs/BUG_AND_REFACTOR_LOG.md`

## Notes

- Empty input lists are handled cleanly.
- Constant numeric series return a zero vector instead of raising a division-by-zero error.
- Invalid types raise `TypeError` with clear messages for easier debugging.

## License

This project is intended for educational and learning purposes within the internship workflow.
