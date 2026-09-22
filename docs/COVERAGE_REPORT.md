# Source Coverage Report

## Command

Coverage was measured with the optional development dependency listed in `requirements-dev.txt`:

```bash
coverage erase
coverage run --source=src -m unittest discover -s tests
coverage report -m
```

## Actual Result

The command executed 32 tests successfully. The source-only report was:

```text
Name                             Stmts   Miss  Cover   Missing
--------------------------------------------------------------
src\data_processor\__init__.py       0      0   100%
src\data_processor\core.py          38      0   100%
--------------------------------------------------------------
TOTAL                               38      0   100%
```

## Interpretation

| File | Statements | Missed | Coverage |
| --- | ---: | ---: | ---: |
| `src/data_processor/__init__.py` | 0 | 0 | 100% |
| `src/data_processor/core.py` | 38 | 0 | 100% |
| **Total source** | **38** | **0** | **100%** |

All executable statements in the current source were exercised by the suite, including validation branches, empty input, constant-series handling, text normalization, and pipeline errors. The report intentionally uses `--source=src` so test-file lines are not mixed into the application coverage metric.

Coverage percentage is not a substitute for assertion quality; the test catalog and precise expected values document what each test proves. Further tests would be appropriate if new features such as missing-value policies, configurable scaling, or additional input containers are added.
