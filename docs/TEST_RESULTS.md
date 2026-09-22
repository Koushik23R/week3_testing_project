# Week 3 Test Execution Results and Metrics

## Environment

| Item | Recorded value |
| --- | --- |
| Python | 3.13.3 |
| Framework | Python `unittest` |
| Operating environment | Windows |
| Command | `python -m unittest discover -s tests -v` |

## Test Summary

| Metric | Actual result |
| --- | ---: |
| Total tests | 32 |
| Passed | 32 |
| Failed | 0 |
| Errors | 0 |
| Pass rate | 100% |
| Execution time | 0.007 sec |

The duration is the value printed by `unittest` on the recorded run and may vary by machine.

## Representative Terminal Output

```text
test_min_max_scale_normal (test_core.TestDataScaler.test_min_max_scale_normal) ... ok
test_clean_text_unicode (test_core.TestTextCleaner.test_clean_text_unicode) ... ok
test_pipeline_end_to_end_success (test_integration.TestDataPipelineIntegration.test_pipeline_end_to_end_success) ... ok
test_pipeline_mismatched_lengths (test_integration.TestDataPipelineIntegration.test_pipeline_mismatched_lengths) ... ok
...
----------------------------------------------------------------------
Ran 32 tests in 0.007s

OK
```

The ellipsis shortens the verbose listing only; all 32 tests were executed by the command above. No failures or errors were recorded.

## Coverage Result

Source coverage was measured separately with:

```text
coverage erase
coverage run --source=src -m unittest discover -s tests
coverage report -m
```

That run also executed 32 tests successfully. The source-only result was 38 statements, 0 missed, and 100% coverage. See [`COVERAGE_REPORT.md`](COVERAGE_REPORT.md).
