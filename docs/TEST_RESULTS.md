# Week 3 Test Execution Results & Metrics

## Environment Specifications
- **Python Version:** Python 3.13 / Standard Library
- **Test Framework:** `unittest`
- **Execution Command:** `python -m unittest discover -s tests -v`

---

## Complete Terminal Execution Output

```text
test_min_max_scale_empty_list (test_core.TestDataScaler.test_min_max_scale_empty_list)
Test handling of empty input list. ... ok
test_min_max_scale_invalid_elements (test_core.TestDataScaler.test_min_max_scale_invalid_elements)
Test that TypeError is raised when input contains non-numeric data. ... ok
test_min_max_scale_invalid_type (test_core.TestDataScaler.test_min_max_scale_invalid_type)
Test that TypeError is raised when input is not a list. ... ok
test_min_max_scale_normal (test_core.TestDataScaler.test_min_max_scale_normal)
Test standard min-max normalization to [0, 1] range. ... ok
test_min_max_scale_single_value (test_core.TestDataScaler.test_min_max_scale_single_value)
Test min-max scale when min == max (division by zero handling). ... ok
test_clean_text_empty (test_core.TestTextCleaner.test_clean_text_empty)
Test that empty string returns empty string. ... ok
test_clean_text_non_string_input (test_core.TestTextCleaner.test_clean_text_non_string_input)
Test that TypeError is raised when input is not a string. ... ok
test_clean_text_normal (test_core.TestTextCleaner.test_clean_text_normal)
Test lowercasing, trimming, and punctuation removal. ... ok
test_pipeline_end_to_end_success (test_integration.TestDataPipelineIntegration.test_pipeline_end_to_end_success)
Test full pipeline processing with valid multi-modal data. ... ok
test_pipeline_invalid_input_propagation (test_integration.TestDataPipelineIntegration.test_pipeline_invalid_input_propagation)
Test that invalid numeric input inside pipeline correctly raises TypeError. ... ok
test_pipeline_mismatched_lengths (test_integration.TestDataPipelineIntegration.test_pipeline_mismatched_lengths)
Test that mismatched list lengths raise ValueError. ... ok

----------------------------------------------------------------------
Ran 11 tests in 0.011s

OK