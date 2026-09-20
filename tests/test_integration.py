import unittest
from src.data_processor.core import DataPipeline

class TestDataPipelineIntegration(unittest.TestCase):
    def setUp(self):
        self.pipeline = DataPipeline()

    def test_pipeline_end_to_end_success(self):
        """Test full pipeline processing with valid multi-modal data."""
        raw_texts = ["  FEATURE A: high  ", "Feature B: LOW! "]
        raw_scores = [100.0, 200.0]

        result = self.pipeline.process_dataset(raw_texts, raw_scores)

        expected_texts = ["feature a high", "feature b low"]
        expected_scores = [0.0, 1.0]

        self.assertEqual(result["cleaned_text"], expected_texts)
        self.assertEqual(result["scaled_numbers"], expected_scores)
        self.assertEqual(result["record_count"], 2)

    def test_pipeline_invalid_input_propagation(self):
        """Test that invalid numeric input inside pipeline correctly raises TypeError."""
        raw_texts = ["Sample text 1", "Sample text 2"]
        invalid_scores = [100.0, "invalid_element"]  # Same length (2 elements)

        with self.assertRaises(TypeError):
            self.pipeline.process_dataset(raw_texts, invalid_scores)

    def test_pipeline_mismatched_lengths(self):
        """Test that mismatched list lengths raise ValueError."""
        raw_texts = ["Text 1", "Text 2"]
        mismatched_scores = [100.0]  # Mismatched length (2 vs 1)

        with self.assertRaises(ValueError):
            self.pipeline.process_dataset(raw_texts, mismatched_scores)

if __name__ == "__main__":
    unittest.main()