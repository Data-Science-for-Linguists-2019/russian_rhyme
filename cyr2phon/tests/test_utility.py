import json
import pkgutil
from nose.tools import *
from cyr2phon import syllabify

words_to_syllabify = _lexical_data = json.loads(
    pkgutil.get_data(__package__, 'words_to_syllabify.json').decode('utf-8'))  # file inside package


def test_syllabify_word():
    for word in words_to_syllabify:
        fn = lambda: syllabify(word)
        fn.description = "cyr2phon.tests.test_utility.test_syllabify_word with {}".format(word)
        yield fn


def check_syllabify_word(word):
    assert_equal(syllabify(word), words_to_syllabify[word])
