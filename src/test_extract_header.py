import unittest
from extractheader import extract_header
class TestExtractHeader(unittest.TestCase):
    def test_extract_header(self):
        text_markdown = """
            # Test Header
            BUnch of stuff man
            lets go yeet
        """
        self.assertEqual(extract_header(text_markdown),"Test Header")
        self.assertEqual(extract_header("# Header"),"Header")

