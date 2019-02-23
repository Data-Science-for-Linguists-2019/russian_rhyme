import json
import pkgutil
from nose.tools import *
from cyr2phon import syllabify, strip_onset

# tests for syllabify()
words_to_syllabify = _lexical_data = json.loads(
    pkgutil.get_data(__package__, 'words_to_syllabify.json').decode('utf-8'))  # file inside package


def test_syllabify_word():
    for word in words_to_syllabify:
        fn = lambda: syllabify(word)
        fn.description = "cyr2phon.tests.test_utility.test_syllabify_word with {}".format(word)
        yield fn


def check_syllabify_word(word):
    assert_equal(syllabify(word), [syllable for syllable in words_to_syllabify[word].split("-")])


#tests for strip_onset()
def test_strip_onset_bA(): # open masculine with onset
    expected = ['BA']
    assert_equal(strip_onset(['BA']), expected)


def test_strip_onset_proch(): # closed masculine with onset
    expected = ['OČ']
    assert_equal(strip_onset(['prOČ']), expected)


def test_strip_onset_babA(): # feminine with onset
    expected = ['A', 'Vil']
    assert_equal(strip_onset(['prA', 'Vil']), expected)


