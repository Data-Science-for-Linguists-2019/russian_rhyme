"""
cyr2phon.py

Public function:
    transliterate: pipeline of all private functions, in the order below

Private functions:
    _flatten : convert XML <stress> tags to uppercase; normalize case, punctuation, white space
    _ogo: ogo -> ego
    _proclitics() : merge _PROCLITICS with bases
    _enclitics() : merge _ENCLITICS with bases
    _tsa() : convert ть?ся$ to тса
    _palatalize() : capitalize all palatalized consonants (including unpaired)
    _jot() : normalize /j/, strip hard and soft signs
    _romanize() : romanize now that all information is represented by the segment
    _final_devoice() : devoice obstruents in auslaut
    _regressive_devoice() : devoice obstruents and /v/ (regressive)
    _regressive_voice() : voice obstruents, including /v/ (regressive)
    _palatal_assimilation() : palatalization (regressive)
    _consonant_cleanup() : c > ts, sč to šč, degeminate
    _vowel_reduction() : unstressed non-high vowels are i after soft consonants and i < e, a < o after hard
    _strip_spaces() : remove all spaces
"""
# imports
from xml.dom import pulldom
import string
import re
import json
import pkgutil
import functools

# constants
# TODO: use regex character class to strip non-letters instead of punctuation?
_PUNC_RE = re.compile("[" + string.punctuation.replace("-", "") + "«»]+")  # strip all punc except hyphen

"""constants for _ogo()"""
_OGO_RE = re.compile(r'([ео])г([ео])$', re.IGNORECASE)  # -ogo that needs to be changed to -ego
_OGO_EXCEPTIONS = {"немнОго", "мнОго", "стрОго", "убОго", "разлОго", "отлОго", "полОго"}  # exceptions to the above
_lexical_data = json.loads(
    pkgutil.get_data(__package__, 'lexical.json').decode('utf-8'))  # needed to refer to file inside package
_ALL_LEXICAL_RE = re.compile("|".join(_lexical_data.keys()))  # omnibus regex, keys are strings for this part
_LEXICAL_DICT = {re.compile(key): value for key, value in _lexical_data.items()}  # now make them regexes for lookup

"""constant for _proclitics()"""
_PROCLITICS = {"а", "без", "безо", "благодаря", "близ", "в", "вне", "во", "для", "до", "за", "и", "из", "из-за",
               "из-под", "изо", "или", "иль", "к", "ко", "меж", "на", "над", "надо", "не", "ни", "но", "о", "об",
               "обо", "от", "ото", "перед", "передо", "по", "по-за", "по-над", "по-под", "под", "подо", "пред",
               "предо", "при", "про", "с", "сквозь", "скрозь", "со", "среди", "средь", "у", "через", "чрез"}

"""constant for _enclitics()"""
_ENCLITICS = {"бо", "бы", "же", "ли"}

"""constant for _tsa()"""
_TSA_RE = re.compile(r'ться\b')  # reflexive

"""constant and callback for _palatalize"""
_PAL_RE = re.compile(r'([бвгдзклмнпрстфх])([яеиёюЯЕИЁЮь])')  # C before softening V


def _process_match_PAL_RE(m) -> str:  # call when _PAL_RE matches (C before softening V)
    return m.group(1).upper() + m.group(2)


"""constants and callbacks for _jot()"""
_INTERV_JOT_RE = re.compile(r'([аэыоуяеиёюАЭЫОУЯЕИЁЮьъ])([яеиёюЯЕИЁЮ])')  # V before jotated V
_INITIAL_JOT_RE = re.compile(r'\b[яеёюЯЕЁЮ]')


def _process_match_INTERV_JOT_RE(m) -> str:  # call when _INTERV_JOT_RE matches (VjV)
    return m.group(1) + "Й" + m.group(2)


def _process_match_INITIAL_JOT_RE(m) -> str:  # call when _INITIAL_JOT_RE matches (#jV)
    return "Й" + m.group(0)


"""constant and callback for _final_devoice()"""
_FINAL_DEVOICE_RE = re.compile(r'[bvgdžzBVGDZ]\b')


def _process_match_FINAL_DEVOICE(m) -> str:  # call when _FINAL_DEVOICE_RE matches (voiced obstruent in auslaut)
    transtab = str.maketrans('bvgdžzBVGDZ', 'pfktšsPFKTS')
    return ""  # TODO: Placeholder


# private functions
def _flatten(line: str) -> str:
    """Clean and flatten input

    Keyword argument:
    input -- line of poetry to process, as well-formed XML, with <stress> tags

    Convert stressed vowels to uppercase and remove stress tags
    Convert other text to lowercase
    Strip punctuation
    Normalize white space
    """
    in_stress = 0  # are we inside a <stress> element?
    result = []  # accumulate output string
    doc = pulldom.parseString(line)
    for event, node in doc:
        if event == pulldom.START_ELEMENT and node.localName == 'stress':
            in_stress = 1
        elif event == pulldom.END_ELEMENT and node.localName == 'stress':
            in_stress = 0
        elif event == pulldom.CHARACTERS:
            if in_stress:
                result.append(node.data.upper())
            else:
                result.append(node.data.lower())
    return _PUNC_RE.sub("", "".join(result))


def _ogo(word: str) -> str:
    """Correct for -ого and lexical idiosyncrasies (e.g., солнце)
    
    Keyword argument:
    word -- word to process (Cyrillic)

    g -> v in word-final -ogo/-ego (before stripping spaces, case-insensitive), except:
        (ne)?mnogo, strogo, ubogo, razlogo, otlogo, pologo, segodnja
    Č > š: что(бы)?, конечн.*, нарочн.*, очечник.*, прачечн.*, скучно, яичниц.*, ильиничн.*, саввичн.*, никитичн.*
    Idiosyncrasies: solnc.*, zdravstvuj.*, čuvstv*, zvezdn.*, landšaft.*, pozdno, prazdnik.*, serdc.*, grustn.*,
        izvestn.*, lestn.*, mestn.*, okrestnost.*, častn.*, sčastliv.*; also segodnja
    No more than one pattern can match, so no need to recurse over entire dictionary
    """
    # perform lexical substitutions
    if _ALL_LEXICAL_RE.search(word):  # check for any match to avoid checking all of them when not needed
        for key in _LEXICAL_DICT.keys():  # there's a match, so find the right key
            if key.search(word):
                word = key.sub(_LEXICAL_DICT[key], word)
                break
    if word not in _OGO_EXCEPTIONS:  # g -> v unless exception
        word = _OGO_RE.sub(r'\1в\2', word)
    return word


def _proclitics(line: str) -> str:
    """Merge _PROCLITICS with bases

    rstrip() because we add spurious space after last word
    """
    words = line.split()
    return "".join([word if word in _PROCLITICS else word + " " for word in words ]).rstrip()


def _enclitics(line: str) -> str:
    """Merge _ENCLITICS with bases"""
    output_line = []
    words = line.split()
    for word in words:
        if word not in _ENCLITICS:
            output_line.append(" ")
        output_line.append(word)
    return "".join(output_line).strip()  # we added a spurious space before the first word


def _tsa(line: str) -> str:
    """Convert ть?ся$ to тса"""
    return _TSA_RE.sub('тса', line)


def _palatalize(line: str) -> str:
    """Capitalize all palatalized consonants (including unpaired)"""
    transtab = str.maketrans('чщй', 'ЧЩЙ')
    return _PAL_RE.sub(_process_match_PAL_RE, line).translate(transtab)


def _jot(line: str) -> str:
    """Normalize /j/

    Insert Й before softening vowels after vowels, hard or soft sign, and (except in anlaut) и
    Convert softening vowels to non-softening
    Strip hard and soft signs
    """
    transtab = str.maketrans('яеиёюЯЕИЁЮ', 'аэыоуАЭЫОУ', 'ьъ')
    t1 = _INTERV_JOT_RE.sub(_process_match_INTERV_JOT_RE, line)  # VjV, ьjV
    t2 = _INITIAL_JOT_RE.sub(_process_match_INITIAL_JOT_RE, t1)  # processes softening vowels except и in anlaut
    return t2.translate(transtab)  # conflate softening vowels into regular ones, strip signs


# noinspection SpellCheckingInspection
def _romanize(line: str) -> str:
    """Romanize text"""
    transtab = str.maketrans('абвгджзклмнопрстуфхцшыэАБВГДЖЗЙКЛМНОПРСТУФХЦЧШЩЫЭ',
                             'abvgdžzklmnoprstufxcšieABVGDŽZJKLMNOPRSTUFXCČŠQIE')
    return line.translate(transtab).replace("Щ", "ŠČ")  # only щ is not one-to-one


# def _final_devoice(line: str) -->:
#     """Devoice final obstruents"""
#     _FINAL_VOICED_RE.sub(, line)

def _regressive_devoice():
    pass


def _regressive_voice():
    pass


def _palatal_assimilation():
    pass


def _consonant_cleanup():
    pass


def _vowel_reduction():
    pass


def _strip_spaces():
    pass


# public function
def transliterate(line: str) -> str:  # TODO: trap non-XML input
    """Transliterate input line

    Pipe input XML line through private function pipeline
    See: https://softwarejourneyman.com/python-function-pipelines.html
    """
    return functools.reduce(
        lambda value, function: function(value),
        (
            _flatten,
            _ogo,
            _proclitics,
            _enclitics,
            _tsa,
            _palatalize,
            _jot,
            _romanize
        ),
        line,
    )
