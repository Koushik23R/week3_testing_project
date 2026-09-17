import re


class DataScaler:
    """Scales numerical data series."""

    def min_max_scale(self, data: list[float]) -> list[float]:
        """Scales values to a [0, 1] range. Handles constant series by returning zeroes."""
        if not data:
            return []

        min_val = min(data)
        max_val = max(data)
        range_val = max_val - min_val

        # Handle division by zero when min == max
        if range_val == 0:
            return [0.0 for _ in data]

        return [round((x - min_val) / range_val, 4) for x in data]


class TextCleaner:
    """Cleans and normalizes text strings."""

    def clean_text(self, text: str) -> str:
        """Trims whitespace, lowercases text, and strips punctuation."""
        if not text:
            return ""

        # Lowercase and trim surrounding whitespace
        cleaned = text.strip().lower()
        # Remove special characters/punctuation using regex
        cleaned = re.sub(r'[^\w\s]', '', cleaned)
        # Collapse multiple spaces into single space
        return re.sub(r'\s+', ' ', cleaned)