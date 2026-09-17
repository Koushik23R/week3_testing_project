import unittest
from src.data_processor.core import DataPipeline

class TestDataPipelineIntegration(unittest.TestCase):
    def setUp(self):
        self.pipeline = DataPipeline()

    def test_pipeline_end_to_end_success(self):
        """Test full pipeline processing with valid multi-modal data."""
        raw_texts = ["  FEATURE A: high  ", "Feature B: LOW! "]
        raw_scores = [100, 200]

        result = self.pipeline.process_dataset(raw_texts, raw_scores)

        self.assertEqual(result["cleaned_text"], ["feature a high", "feature b low"])
        self.assertEqual(result["scaled_numbers"], [0.0, 1.0])
        self.assertEqual(result["record_count"], 2)

    def test_pipeline_invalid_input_propagation(self):
        """Test that invalid numeric input inside pipeline correctly raises TypeError."""
        raw_texts = ["Valid text"]
        invalid_scores = [10, "corrupted"]

        with self.assertRaises(TypeError):
            self.pipeline.process_dataset(raw_texts, invalid_scores)

if __name__ == "__main__":
    unittest.main()