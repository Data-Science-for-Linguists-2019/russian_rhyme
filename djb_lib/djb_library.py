"""
djb_library.py

Public function:
    transliterate: pipeline of all private functions

Private functions:
    _flatten : convert XML <stress> tags to uppercase; normalize case, punctuation, white space
    _ogo: ogo -> ego
    _proclitics() : merge proclitics with bases
    _enclitics() : merge enclitics with bases
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

# constants
# TODO: use regex character class to strip non-letters instead of punctuation?
_PUNC_RE = re.compile("[" + string.punctuation.replace("-", "") + "«»]+")  # strip all punc except hyphen
_OGO_RE = re.compile(r'([ео])г([ео])$', re.IGNORECASE)  # -ogo that needs to be changed to -ego
_OGO_EXCEPTIONS = {"немнОго", "мнОго", "стрОго", "убОго", "разлОго", "отлОго", "полОго"}  # exceptions to the above
_lexical_data = json.loads(
    pkgutil.get_data(__package__, 'lexical.json').decode('utf-8'))  # needed to refer to file inside package
_ALL_LEXICAL_RE = re.compile("|".join(_lexical_data.keys()))  # omnibus regex, keys are strings for this part
_LEXICAL_DICT = {re.compile(key): value for key, value in _lexical_data.items()}  # now make them regexes for lookup


def transliterate(word: str) -> str:
    return word


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
        if event == pulldom.END_ELEMENT and node.localName == 'stress':
            in_stress = 0
        if event == pulldom.CHARACTERS:
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
        izvestn.*, lestn.*, mestn.*, okrestnost.*, častn.*, sčastliv.*
    No more than one pattern can match, so no need to recurse over entire dictionary
    """
    # perform lexical substitutions
    if _ALL_LEXICAL_RE.search(word):  # check for any match to avoid checking all of them when not needed
        for key in _LEXICAL_DICT.keys():  # there's a match, so find the right key
            if key.search(word):
                word = key.sub(_LEXICAL_DICT[key], word)
                break
    if word not in _OGO_EXCEPTIONS:  # g -> v unless exception
        if word == "сегОдня":  # nonce exceptions
            word = "севОдня"
        elif word not in _OGO_EXCEPTIONS:
            word = _OGO_RE.sub(r'\1в\2', word)
    return word


def _proclitics(line: str) -> str:
    proclitics = ["а", "без", "безо", "благодаря", "близ", "в", "вне", "во", "для", "до", "за", "и", "из", "из-за",
                  "из-под", "изо", "или", "иль", "к", "ко", "меж", "на", "над", "надо", "не", "ни", "но", "о", "об",
                  "обо", "от", "ото", "перед", "передо", "по", "по-за", "по-над", "по-под", "под", "подо", "пред",
                  "предо", "при", "про", "с", "сквозь", "скрозь", "со", "среди", "средь", "у", "через", "чрез", ]
    output_line = []
    words = line.split()
    for word in words:
        output_line.append(word)
        if word not in proclitics:
            output_line.append(" ")
    return "".join(output_line).strip()  # we added a spurious space after the last word


def _enclitics(line: str) -> str:
    enclitics = ["бо", "бы", "же", "ли"]
    output_line = []
    words = line.split()
    for word in words:
        if word not in enclitics:
            output_line.append(" ")
        output_line.append(word)
    return "".join(output_line).strip()  # we added a spurious space before the first word


def _tsa():
    pass


def _palatalize():
    pass


def _jot():
    pass


def _romanize():
    pass


def _final_devoice():
    pass


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
