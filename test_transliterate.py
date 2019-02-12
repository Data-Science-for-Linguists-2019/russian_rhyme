from unittest import TestCase
from djb_lib import djb_library

class TestTransliterate(TestCase):
    def test_transliterate_1(self):
        expected = "hi"
        self.assertEqual(djb_library.transliterate("hi"), expected)
    def test_transliterate_2(self):
        expected = ""
        self.assertEqual(djb_library.transliterate(""), expected)

class TextFlatten(TestCase):
    def test_flatten_stress(self):
        expected = "бЕрег"
        self.assertEqual(djb_library._flatten("<line>б<stress>е</stress>рег</line>"), expected)
    def test_flatten_lc(self):
        expected = "берег"
        self.assertEqual(djb_library._flatten("<line>Берег</line>"), expected)
    def test_flatten_punc_hyphen(self):
        expected = "кто-то"
        self.assertEqual(djb_library._flatten("<line>кто-то</line>"), expected)
    def test_flatten_punc_period(self):
        expected = "берег"
        self.assertEqual(djb_library._flatten("<line>берег.</line>"), expected)
    def test_flatten_punc_question(self):
        expected = "берег"
        self.assertEqual(djb_library._flatten("<line>берег?</line>"), expected)
