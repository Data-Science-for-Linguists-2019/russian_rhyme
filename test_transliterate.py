from djb_lib import djb_library
from nose.tools import *
import re

# test suite constants
key_set = {"ильИничн", "здрАвствуй", "лЕстн", "мЕстн", "очЕчник", "^чтО", "^что", "никИтичн", "скУчно$", "грУстн",
           "нарОчн", "счАстлив", "окрЕстн", "яИчниц", "ландшАфт", "конЕчн", "прАздник", "чАстн", "прАчечн", "звЁздн",
           "извЕстн", "чУвств", "пОздно", "сЕрдц", "сАввичн"}


# constants
def test_PUNC_RE():
    expected = re.compile("[" + '!"#$%&\'()*+,./:;<=>?@[\\]^_`{|}~«»' + "]+")
    assert_equal(djb_library._PUNC_RE, expected)


def test_OGO_RE():
    for s in ["ого", "его", "Ого", "Его", "огО", "егО"]:
        assert_regexp_matches(s, djb_library._OGO_RE)


def test_OGO_EXCEPTIONS():
    expected = {"немнОго", "мнОго", "стрОго", "убОго", "разлОго", "отлОго", "полОго"}
    assert_equal(djb_library._OGO_EXCEPTIONS, expected)


def test_lexical_data_size():
    key_length = len(key_set)
    assert_equal(len(djb_library._lexical_data), key_length)


def test_lexical_data_members():
    for item in key_set:
        assert_in(re.compile(item), djb_library._LEXICAL_DICT.keys())


# translate() TODO: placeholder functions
def test_transliterate_1():
    expected = "hi"
    assert_equal(djb_library.transliterate("hi"), expected)


def test_transliterate_2():
    expected = ""
    assert_equal(djb_library.transliterate(""), expected)


# _flatten()
def test_flatten_stress():
    expected = "бЕрег"
    assert_equal(djb_library._flatten("<line>б<stress>е</stress>рег</line>"), expected)


def test_flatten_lowercase():
    expected = "берег"
    assert_equal(djb_library._flatten("<line>Берег</line>"), expected)


def test_flatten_punc_hyphen():
    expected = "кто-то"
    assert_equal(djb_library._flatten("<line>кто-то</line>"), expected)


def test_flatten_punc_period():
    expected = "берег"
    assert_equal(djb_library._flatten("<line>берег.</line>"), expected)


def test_flatten_punc_question():
    expected = "берег"
    assert_equal(djb_library._flatten("<line>берег?</line>"), expected)


# _ogo()
def test_ogo_mnogo():
    expected = "мнОго"
    assert_equal(djb_library._ogo("мнОго"), expected)


def test_ogo_moego():
    expected = "моевО"
    assert_equal(djb_library._ogo("моегО"), expected)


def test_ogo_segodnja():
    expected = "севОдня"
    assert_equal(djb_library._ogo("сегОдня"), expected)


def test_ogo_konechno():
    expected = "конЕшно"
    assert_equal(djb_library._ogo("конЕчно"), expected)


# _proclitics()
def test_proclitics_s_mamoj():
    expected = "мы смАмой"
    assert_equal(djb_library._proclitics("мы с мАмой"), expected)


def test_proclitics_ne_s_mamoj():
    expected = "что несмамой"
    assert_equal(djb_library._proclitics("что не с мамой"), expected)


# _enclitics()
def test_enclitics_mog_by():
    expected = "мОгбы"
    assert_equal(djb_library._enclitics("мОг бы"), expected)
