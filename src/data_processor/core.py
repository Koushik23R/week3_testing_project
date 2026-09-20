import re
from typing import List, Union


class DataScaler:
    """Scales numerical data series with strict type validation."""

    def min_max_scale(self, data: List[Union[int, float]]) -> List[float]:
        """Scales values to a [0, 1] range. Handles constant series by returning zeroes."""
        if not isinstance(data, list):
            raise TypeError("Input data must be a list of numbers.")

        if not data:
            return []

        for item in data:
            if not isinstance(item, (int, float)) or isinstance(item, bool):
                raise TypeError(f"All items in data must be integers or floats, got: {type(item).__name__}")

        min_val = min(data)
        max_val = max(data)
        range_val = max_val - min_val

        if range_val == 0:
            return [0.0 for _ in data]

        return [round((x - min_val) / range_val, 4) for x in data]


class TextCleaner:
    """Cleans and normalizes text strings with type checks."""

    def clean_text(self, text: str) -> str:
        """Trims whitespace, lowercases text, and strips punctuation."""
        if not isinstance(text, str):
            raise TypeError(f"Input must be a string, got: {type(text).__name__}")

        if not text:
            return ""

        cleaned = text.strip().lower()
        cleaned = re.sub(r'[^\w\s]', '', cleaned)
        return re.sub(r'\s+', ' ', cleaned)

class DataPipeline:
    """Combines text cleaning and numerical scaling into an end-to-end pipeline."""

    def __init__(self):
        self.cleaner = TextCleaner()
        self.scaler = DataScaler()

    def process_dataset(self, text_list: List[str], number_list: List[Union[int, float]]) -> dict:
        """Processes text and numerical data together, returning clean structured output."""
        if not isinstance(text_list, list) or not isinstance(number_list, list):
            raise TypeError("Both text_list and number_list must be Python lists.")

        if len(text_list) != len(number_list):
            raise ValueError("text_list and number_list must contain the same number of items.")

        cleaned_texts = [self.cleaner.clean_text(t) for t in text_list]
        scaled_numbers = self.scaler.min_max_scale(number_list)

        return {
            "cleaned_text": cleaned_texts,
            "scaled_numbers": scaled_numbers,
            "record_count": len(cleaned_texts)
        }