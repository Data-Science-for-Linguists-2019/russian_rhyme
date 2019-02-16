from cyr2phon import cyr2phon
from nose.tools import *
import re

# test suite constants
key_set = {"ильИничн", "здрАвствуй", "лЕстн", "мЕстн", "очЕчник", "^чтО", "^что", "никИтичн", "скУчно$", "грУстн",
           "нарОчн", "счАстлив", "окрЕстн", "яИчниц", "ландшАфт", "конЕчн", "прАздник", "чАстн", "прАчечн", "звЁздн",
           "извЕстн", "чУвств", "пОздно", "сЕрдц", "сАввичн"}


# constants
def test_PUNC_RE():
    expected = re.compile("[" + '!"#$%&\'()*+,./:;<=>?@[\\]^_`{|}~«»' + "]+")
    assert_equal(cyr2phon._PUNC_RE, expected)


def test_OGO_RE():
    for s in ["ого", "его", "Ого", "Его", "огО", "егО"]:
        assert_regexp_matches(s, cyr2phon._OGO_RE)


def test_OGO_EXCEPTIONS():
    expected = {"немнОго", "мнОго", "стрОго", "убОго", "разлОго", "отлОго", "полОго"}
    assert_equal(cyr2phon._OGO_EXCEPTIONS, expected)


def test_lexical_data_size():
    key_length = len(key_set)
    assert_equal(len(cyr2phon._lexical_data), key_length)


def test_lexical_data_members():
    for item in key_set:
        assert_in(re.compile(item), cyr2phon._LEXICAL_DICT.keys())


def test_transliterate_empty():
    expected = ""
    assert_equal(cyr2phon.transliterate(""), expected)


# _flatten()
def test_flatten_stress():
    expected = "бЕрег"
    assert_equal(cyr2phon._flatten("<line>б<stress>е</stress>рег</line>"), expected)


def test_flatten_lowercase():
    expected = "берег"
    assert_equal(cyr2phon._flatten("<line>Берег</line>"), expected)


def test_flatten_punc_hyphen():
    expected = "кто-то"
    assert_equal(cyr2phon._flatten("<line>кто-то</line>"), expected)


def test_flatten_punc_period():
    expected = "берег"
    assert_equal(cyr2phon._flatten("<line>берег.</line>"), expected)


def test_flatten_punc_question():
    expected = "берег"
    assert_equal(cyr2phon._flatten("<line>берег?</line>"), expected)


# _ogo()
def test_ogo_mnogo():
    expected = "мнОго"
    assert_equal(cyr2phon._ogo("мнОго"), expected)


def test_ogo_moego():
    expected = "моевО"
    assert_equal(cyr2phon._ogo("моегО"), expected)


def test_ogo_segodnja():
    expected = "севОдня"
    assert_equal(cyr2phon._ogo("сегОдня"), expected)


def test_ogo_konechno():
    expected = "конЕшно"
    assert_equal(cyr2phon._ogo("конЕчно"), expected)


# _proclitics()
def test_proclitics_s_mamoj():
    expected = "мы смАмой"
    assert_equal(cyr2phon._proclitics("мы с мАмой"), expected)


def test_proclitics_ne_s_mamoj():
    expected = "что несмамой"
    assert_equal(cyr2phon._proclitics("что не с мамой"), expected)


# _enclitics()
def test_enclitics_mog_by():
    expected = "мОгбы"
    assert_equal(cyr2phon._enclitics("мОг бы"), expected)


# _tsa()
def test_tsa():
    expected = "боротса боротса"
    assert_equal(cyr2phon._tsa("бороться бороться"), expected)


# _palatalize()
def test_palatalize():
    expected = "на БеРегУ пустЫнных вОлн"
    assert_equal(cyr2phon._palatalize("на берегУ пустЫнных вОлн"), expected)


def test_palatalize_all_front_vowels():
    for v in "яеиёюЯЕИЁЮ":
        assert_equal(cyr2phon._palatalize("б" + v), "Б" + v)


def test_palatalize_all_back_vowels():
    for v in "аэыоуАЭЫОУ":
        assert_equal(cyr2phon._palatalize("б" + v), "б" + v)


def test_palatalize_unpaired():
    expected = "аЧаЙаЩаба"
    assert_equal(cyr2phon._palatalize("ачайащаба"), expected)


# _jot()
def test_jot_interv():
    expected = "болшАЙа"
    assert_equal(cyr2phon._jot("большАя"), expected)


def test_jot_initial():
    expected = "ЙА ЙУныЙ"
    assert_equal(cyr2phon._jot("Я ЮныЙ"), expected)


def test_jot_soft_sign():
    expected = "стаТЙА"
    assert_equal(cyr2phon._jot("стаТьЯ"), expected)


# _romanize()
def test_romanize_all():
    expected = "abvgdžzklmnoprstufxcšie ABVGDŽZJKLMNOPRSTUFXCČŠQIE"
    assert_equal(cyr2phon._romanize("абвгджзклмнопрстуфхцшыэ АБВГДЖЗЙКЛМНОПРСТУФХЦЧШЩЫЭ"), expected)


# translate() TODO: placeholder functions
# This is really an integration test, since transliterate() calls all other functions
def test_transliterate_line():
    expected = "naBeRegU pustInnix vOln"
    assert_equal(cyr2phon.transliterate("<line>На берег<stress>у</stress> пуст<stress>ы</stress>нных "
                                        "в<stress>о</stress>лн</line>"), expected)
