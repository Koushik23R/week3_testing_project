import unittest

from src.data_processor.core import DataScaler, TextCleaner


class TestDataScaler(unittest.TestCase):
    def setUp(self):
        self.scaler = DataScaler()

    def test_min_max_scale_normal(self):
        self.assertEqual(
            self.scaler.min_max_scale([10, 20, 30]),
            [0.0, 0.5, 1.0],
        )

    def test_min_max_scale_negative_values(self):
        self.assertEqual(
            self.scaler.min_max_scale([-10, 0, 10]),
            [0.0, 0.5, 1.0],
        )

    def test_min_max_scale_mixed_integers_and_floats(self):
        self.assertEqual(
            self.scaler.min_max_scale([1, 2.5, 4]),
            [0.0, 0.5, 1.0],
        )

    def test_min_max_scale_unsorted_values_preserve_order(self):
        self.assertEqual(
            self.scaler.min_max_scale([30, 10, 20]),
            [1.0, 0.0, 0.5],
        )

    def test_min_max_scale_duplicate_values(self):
        self.assertEqual(
            self.scaler.min_max_scale([10, 20, 20, 30]),
            [0.0, 0.5, 0.5, 1.0],
        )

    def test_min_max_scale_two_values(self):
        self.assertEqual(self.scaler.min_max_scale([4, 8]), [0.0, 1.0])

    def test_min_max_scale_single_value(self):
        self.assertEqual(self.scaler.min_max_scale([5]), [0.0])

    def test_min_max_scale_constant_values(self):
        self.assertEqual(
            self.scaler.min_max_scale([5.0, 5.0, 5.0]),
            [0.0, 0.0, 0.0],
        )

    def test_min_max_scale_empty_list(self):
        self.assertEqual(self.scaler.min_max_scale([]), [])

    def test_min_max_scale_invalid_elements(self):
        invalid_values = ["invalid", None, True]
        expected_messages = [
            "got: str",
            "got: NoneType",
            "got: bool",
        ]
        for value, expected_message in zip(invalid_values, expected_messages):
            with self.subTest(value=value):
                with self.assertRaisesRegex(
                    TypeError,
                    rf"All items in data must be integers or floats, {expected_message}",
                ):
                    self.scaler.min_max_scale([10, value, 30])

    def test_min_max_scale_invalid_tuple(self):
        with self.assertRaisesRegex(
            TypeError,
            r"Input data must be a list of numbers\.",
        ):
            self.scaler.min_max_scale((1, 2, 3))

    def test_min_max_scale_invalid_string_input(self):
        with self.assertRaisesRegex(
            TypeError,
            r"Input data must be a list of numbers\.",
        ):
            self.scaler.min_max_scale("not a list")


class TestTextCleaner(unittest.TestCase):
    def setUp(self):
        self.cleaner = TextCleaner()

    def test_clean_text_normal(self):
        self.assertEqual(
            self.cleaner.clean_text("  Hello, World! Welcome to AI/ML.  "),
            "hello world welcome to aiml",
        )

    def test_clean_text_uppercase_and_mixed_case(self):
        self.assertEqual(
            self.cleaner.clean_text("PYTHON Testing MiXeD"),
            "python testing mixed",
        )

    def test_clean_text_leading_and_trailing_whitespace(self):
        self.assertEqual(
            self.cleaner.clean_text("   padded text   "),
            "padded text",
        )

    def test_clean_text_multiple_spaces(self):
        self.assertEqual(
            self.cleaner.clean_text("one    two     three"),
            "one two three",
        )

    def test_clean_text_punctuation(self):
        self.assertEqual(
            self.cleaner.clean_text("Hello, world! (ready?)"),
            "hello world ready",
        )

    def test_clean_text_numbers_are_preserved(self):
        self.assertEqual(
            self.cleaner.clean_text("Version 3.13 released in 2026"),
            "version 313 released in 2026",
        )

    def test_clean_text_newline_and_tab_are_normalized(self):
        self.assertEqual(
            self.cleaner.clean_text("first\nsecond\tthird"),
            "first second third",
        )

    def test_clean_text_empty(self):
        self.assertEqual(self.cleaner.clean_text(""), "")

    def test_clean_text_unicode(self):
        self.assertEqual(
            self.cleaner.clean_text("  Café déjà vu!  "),
            "café déjà vu",
        )

    def test_clean_text_non_string_inputs(self):
        for value in (12345, None, ["not", "text"]):
            with self.subTest(value=value):
                with self.assertRaisesRegex(
                    TypeError,
                    rf"Input must be a string, got: {type(value).__name__}",
                ):
                    self.cleaner.clean_text(value)


if __name__ == "__main__":
    unittest.main()
