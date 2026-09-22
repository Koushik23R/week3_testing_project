import unittest

from src.data_processor.core import DataPipeline


class TestDataPipelineIntegration(unittest.TestCase):
    def setUp(self):
        self.pipeline = DataPipeline()

    def test_pipeline_end_to_end_success(self):
        result = self.pipeline.process_dataset(
            ["  FEATURE A: high  ", "Feature B: LOW! "],
            [100, 200],
        )
        self.assertEqual(result, {
            "cleaned_text": ["feature a high", "feature b low"],
            "scaled_numbers": [0.0, 1.0],
            "record_count": 2,
        })

    def test_pipeline_multiple_records(self):
        result = self.pipeline.process_dataset(
            ["First record", "Second record", "Third record"],
            [10, 20, 30],
        )
        self.assertEqual(result["cleaned_text"], [
            "first record",
            "second record",
            "third record",
        ])
        self.assertEqual(result["scaled_numbers"], [0.0, 0.5, 1.0])
        self.assertEqual(result["record_count"], 3)

    def test_pipeline_single_record(self):
        result = self.pipeline.process_dataset(["  One! "], [42])
        self.assertEqual(result, {
            "cleaned_text": ["one"],
            "scaled_numbers": [0.0],
            "record_count": 1,
        })

    def test_pipeline_empty_dataset(self):
        self.assertEqual(
            self.pipeline.process_dataset([], []),
            {
                "cleaned_text": [],
                "scaled_numbers": [],
                "record_count": 0,
            },
        )

    def test_pipeline_constant_numbers(self):
        result = self.pipeline.process_dataset(
            ["A", "B", "C"],
            [7, 7, 7],
        )
        self.assertEqual(result["scaled_numbers"], [0.0, 0.0, 0.0])
        self.assertEqual(result["record_count"], 3)

    def test_pipeline_mixed_integer_and_float_values(self):
        result = self.pipeline.process_dataset(
            ["Low", "Middle", "High"],
            [1, 2.5, 4],
        )
        self.assertEqual(result["scaled_numbers"], [0.0, 0.5, 1.0])

    def test_pipeline_invalid_numeric_values(self):
        for value, expected_message in (
            ("invalid", "got: str"),
            (True, "got: bool"),
        ):
            with self.subTest(value=value):
                with self.assertRaisesRegex(
                    TypeError,
                    rf"All items in data must be integers or floats, {expected_message}",
                ):
                    self.pipeline.process_dataset(["Sample"], [value])

    def test_pipeline_invalid_text_value(self):
        with self.assertRaisesRegex(
            TypeError,
            r"Input must be a string, got: int",
        ):
            self.pipeline.process_dataset([123], [10])

    def test_pipeline_invalid_list_types(self):
        with self.assertRaisesRegex(
            TypeError,
            r"Both text_list and number_list must be Python lists\.",
        ):
            self.pipeline.process_dataset(("text",), [10])

        with self.assertRaisesRegex(
            TypeError,
            r"Both text_list and number_list must be Python lists\.",
        ):
            self.pipeline.process_dataset(["text"], (10,))

    def test_pipeline_mismatched_lengths(self):
        with self.assertRaisesRegex(
            ValueError,
            r"text_list and number_list must contain the same number of items\.",
        ):
            self.pipeline.process_dataset(["a", "b"], [10])


if __name__ == "__main__":
    unittest.main()
