import unittest
from src.data_processor.core import DataScaler, TextCleaner

class TestDataScaler(unittest.TestCase):
    def setUp(self):
        self.scaler = DataScaler()

    def test_min_max_scale_normal(self):
        """Test standard min-max normalization to [0, 1] range."""
        data = [10.0, 20.0, 30.0, 40.0, 50.0]
        expected = [0.0, 0.25, 0.5, 0.75, 1.0]
        result = self.scaler.min_max_scale(data)
        self.assertEqual(result, expected)

    def test_min_max_scale_single_value(self):
        """Test min-max scale when min == max (division by zero handling)."""
        data = [5.0, 5.0, 5.0]
        expected = [0.0, 0.0, 0.0]
        result = self.scaler.min_max_scale(data)
        self.assertEqual(result, expected)

class TestTextCleaner(unittest.TestCase):
    def setUp(self):
        self.cleaner = TextCleaner()

    def test_clean_text_normal(self):
        """Test lowercasing, trimming, and punctuation removal."""
        raw_text = "  Hello, World! Welcome to AI/ML.  "
        expected = "hello world welcome to aiml"
        result = self.cleaner.clean_text(raw_text)
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()