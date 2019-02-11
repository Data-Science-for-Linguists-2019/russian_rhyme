from unittest import TestCase
from djb_lib import djb_library

class TestTransliterate(TestCase):
    def test_transliterate_1(self):
        expected = "hi"
        self.assertEqual(djb_library.transliterate("hi"), expected)
    def test_transliterate_2(self):
        expected = ""
        self.assertEqual(djb_library.transliterate(""), expected)
