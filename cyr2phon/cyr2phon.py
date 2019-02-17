"""
cyr2phon.py

Public function:
    transliterate: pipeline of all private functions, in the order below

Private functions:
    _flatten : convert XML <stress> tags to uppercase; normalize case, punctuation, white space
    _lexical : process lexical exceptions
    _ogo : ogo -> ego
    _proclitics : merge _PROCLITICS with bases
    _enclitics : merge _ENCLITICS with bases
    _tsa : convert ть?ся$ to тса
    _palatalize : capitalize all palatalized consonants (including unpaired)
    _jot : normalize /j/, strip hard and soft signs
    _romanize : romanize now that all information is represented by the segment
    _final_devoice : devoice obstruents in auslaut
    _regressive_devoice : devoice obstruents and /v/ (regressive)
    _regressive_voice : voice obstruents, including /v/ (regressive)
    _palatal_assimilation : palatalization (regressive)
    _consonant_cleanup : c > ts, sč to šč, degeminate
    _vowel_reduction : unstressed non-high vowels are i after soft consonants and i < e, a < o after hard
    _strip_spaces : remove all spaces
"""
# imports
from xml.dom import pulldom
import string
import re
import json
import pkgutil
import functools

"""constants for _flatten()"""
_XML_RE = re.compile(r"<line>.*</line>")  # TODO: check for balanced <stress> tags
# TODO: use regex character class to strip non-letters instead of punctuation?
_PUNC_RE = re.compile("[" + string.punctuation.replace("-", "") + "«»]+")  # strip all punc except hyphen

"""constants for _lexical()"""
_lexical_data = json.loads(
    pkgutil.get_data(__package__, 'lexical.json').decode('utf-8'))  # needed to refer to file inside package
_LEXICAL_DICT = {re.compile(r"\b" + key): value for key, value in _lexical_data.items()}  # regexes for lookup

"""constants and callback for _ogo()"""
_OGO_RE = re.compile(r'([ео])г([ео])\b', re.IGNORECASE)  # -ogo that needs to be changed to -ego
_OGO_EXCEPTIONS = {"немнОго", "мнОго", "стрОго", "убОго", "разлОго", "отлОго", "полОго"}  # exceptions to the above


def _process_match_OGO_RE(m) -> str:  # call when _OGO_RE matches (-ogo)
    return m.group(1) + "в" + m.group(2)


"""constant for _proclitics()"""
_PROCLITICS = {"а", "без", "безо", "благодаря", "близ", "в", "вне", "во", "для", "до", "за", "и", "из", "из-за",
               "из-под", "изо", "или", "иль", "к", "ко", "меж", "на", "над", "надо", "не", "ни", "но", "о", "об",
               "обо", "от", "ото", "перед", "передо", "по", "по-за", "по-над", "по-под", "под", "подо", "пред",
               "предо", "при", "про", "с", "сквозь", "скрозь", "со", "среди", "средь", "у", "через", "чрез"}

"""constant for _enclitics()"""
_ENCLITICS = {"бо", "бы", "же", "ли"}

"""constant for _tsa()"""
_TSA_RE = re.compile(r'ться\b')  # reflexive

"""constants and callback for _palatalize"""
_PAL_RE = re.compile(r'([бвгдзклмнпрстфх])([яеиёюЯЕИЁЮь])')  # C before softening V
_PAL_TRANSTAB = str.maketrans('чщй', 'ЧЩЙ')


def _process_match_PAL_RE(m) -> str:  # call when _PAL_RE matches (C before softening V)
    return m.group(1).upper() + m.group(2)


"""constants and callbacks for _jot()"""
_INTERV_JOT_RE = re.compile(r'([аэыоуяеиёюАЭЫОУЯЕИЁЮьъ])([яеиёюЯЕИЁЮ])')  # V before jotated V
_INITIAL_JOT_RE = re.compile(r'\b[яеёюЯЕЁЮ]')
_JOT_TRANSTAB = str.maketrans('яеиёюЯЕИЁЮ', 'аэыоуАЭЫОУ', 'ьъ')


def _process_match_INTERV_JOT_RE(m) -> str:  # call when _INTERV_JOT_RE matches (VjV)
    return m.group(1) + "Й" + m.group(2)


def _process_match_INITIAL_JOT_RE(m) -> str:  # call when _INITIAL_JOT_RE matches (#jV)
    return "Й" + m.group(0)


"""constant for _romanize()"""
_ROMANIZE_TRANSTAB = str.maketrans('абвгджзклмнопрстуфхцшыэАБВГДЖЗЙКЛМНОПРСТУФХЦЧШЩЫЭ',
                                   'abvgdžzklmnoprstufxcšieABVGDŽZJKLMNOPRSTUFXCČŠQIE')

"""constants and callback for _final_devoice()"""
_FINAL_DEVOICE_RE = re.compile(r'[bvgdžzBVGDZ]\b')
_FINAL_DEVOICE_TRANSTAB = str.maketrans('bvgdžzBVGDZ', 'pfktšsPFKTS')


def _process_match_FINAL_DEVOICE(m) -> str:  # call when _FINAL_DEVOICE_RE matches (voiced obstruent in auslaut)
    return m.group(0).translate(_FINAL_DEVOICE_TRANSTAB)


"""constants and callback for _regressive_devoice()"""
_REGRESSIVE_DEVOICE_RE = re.compile(r'([bvgdžzBVGDZpfktšsPFKTSkcČ]+)([pfktšsPFKTSkcČ])')
_REGRESSIVE_DEVOICE_TRANSTAB = str.maketrans('bvgdžzBVGDZ', 'pfktšsPFKTS')

def _process_match_REGRESSIVE_DEVOICE(m) -> str: # call when _REGRESSIVE_DEVOICE_RE matches (voiced/_voiceless)
    return m.group(1).translate(_REGRESSIVE_DEVOICE_TRANSTAB) + m.group(2)


"""constants and callback for _regressive_voice()

ɣ (LC) = U+0263, Ɣ (UC) = U+0194
ʒ (LC) = U+0292, Ʒ (UC) = U+01B7
ǯ (LC) = U+01EF, Ǯ (UC) = U+01EE   
"""
_REGRESSIVE_VOICE_RE = re.compile(r'([bvgdžzBVGDZpfktšsPFKTSxcČ]+)([bgdžzBGDZ])')
_REGRESSIVE_VOICE_TRANSTAB = str.maketrans('pfktšsPFKTSxcČ', 'bvgdžzBVGDZɣʒǮ')


def _process_match_REGRESSIVE_VOICE(m) -> str:  # call when _REGRESSIVE_VOICE_RE matches (voiceless/_voiced)
    return m.group(1).translate(_REGRESSIVE_VOICE_TRANSTAB) + m.group(2)


"""constant and callback for _regressive_palatalization

call when _REGRESSIVE_PALATALIZATION_RE matches
ŠČ has already been split, so requires special treatment
"""
_REGRESSIVE_PALATALIZATION_RE = re.compile(r'[tdnszTDNSZČLJ]+[TDNSZČLJ]|ŠČ')


def _process_match_REGRESSIVE_PALATALIZATION(m) -> str:
    return m.group(0).upper()


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
    if _XML_RE.match(line):
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
    else:
        raise Exception(line, "is not tagged correctly")


def _lexical(line: str) -> str:
    """Adjust for lexical idiosyncrasies (e.g., солнце)

    Č > š: ильиничн.*, конечн.*, нарочн.*, никитичн.*, очечник.*, прачечн.*, саввичн.*, скучн.*, яичниц.*
    Idiosyncrasies: grustn.*, zvezdn.*, zdravstvuj.*, izvestn.*, landšaft.*, lestn.*, mestn.*, okrestn.*, pozdn.*,
    prazdn.*, segodnja, serdc.*, solnc.*, sčastliv.*, častn.*, čto.*, čtO.*, čuvstv.*
    """
    for key in _LEXICAL_DICT.keys():
        line = key.sub(_LEXICAL_DICT[key], line)
    return line


def _ogo(line: str) -> str:
    """Correct for -ого
    
    Keyword argument:
    line -- line to process (Cyrillic)

    g -> v in word-final -ogo/-ego (before stripping spaces, case-insensitive), except:
        (ne)?mnogo, strogo, ubogo, razlogo, otlogo, pologo, segodnja
    """
    # perform lexical substitutions
    result = []
    for word in line.split():
        if word in _OGO_EXCEPTIONS:
            result.append(word)
        else:
            result.append(_OGO_RE.sub(_process_match_OGO_RE, word))
    return " ".join(result).rstrip()


def _proclitics(line: str) -> str:
    """Merge _PROCLITICS with bases

    rstrip() because we add spurious space after last word
    """
    words = line.split()
    return "".join([word if word in _PROCLITICS else word + " " for word in words]).rstrip()


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
    return _PAL_RE.sub(_process_match_PAL_RE, line).translate(_PAL_TRANSTAB)


def _jot(line: str) -> str:
    """Normalize /j/

    Insert Й before softening vowels after vowels, hard or soft sign, and (except in anlaut) и
    Convert softening vowels to non-softening
    Strip hard and soft signs
    """
    t1 = _INTERV_JOT_RE.sub(_process_match_INTERV_JOT_RE, line)  # VjV, ьjV
    t2 = _INITIAL_JOT_RE.sub(_process_match_INITIAL_JOT_RE, t1)  # processes softening vowels except и in anlaut
    return t2.translate(_JOT_TRANSTAB)  # conflate softening vowels into regular ones, strip signs


def _romanize(line: str) -> str:
    """Romanize text"""
    return line.translate(_ROMANIZE_TRANSTAB).replace("Щ", "ŠČ")  # only щ is not one-to-one


def _final_devoice(line: str) -> str:
    """Devoice final obstruents"""
    return _FINAL_DEVOICE_RE.sub(_process_match_FINAL_DEVOICE, line)


def _regressive_devoice(line: str) -> str:
    """Regressive devoicing of obstruents, including v

    v is easier to handle if we devoice first
    """
    return _REGRESSIVE_DEVOICE_RE.sub(_process_match_REGRESSIVE_DEVOICE, line)


def _regressive_voice(line: str) -> str:
    """Regressive voicing of obstruents, but not before /v/"""
    return _REGRESSIVE_VOICE_RE.sub(_process_match_REGRESSIVE_VOICE, line)


def _regressive_palatalization(line: str) -> str:
    """Regressive palatalization assimilation"""
    return _REGRESSIVE_PALATALIZATION_RE.sub(_process_match_REGRESSIVE_PALATALIZATION, line)


def _consonant_cleanup(line: str) -> str:
    pass


def _vowel_reduction(line: str) -> str:
    pass


def _strip_spaces(line: str) -> str:
    pass


# public function
def transliterate(line: str) -> str:
    """
    Transliterate input line from Cyrillic XML to Roman string

    Pipe input XML line through private function pipeline
    See: https://softwarejourneyman.com/python-function-pipelines.html

    Keyword parameters:
    line (str): a line of verse as well-formed XML, with only <line> and <stress> tags

    Returns:
    str: transliterated line
    """
    return functools.reduce(
        lambda value, function: function(value),
        (
            _flatten,
            _lexical,
            _ogo,
            _proclitics,
            _enclitics,
            _tsa,
            _palatalize,
            _jot,
            _romanize,
            _final_devoice,
            _regressive_devoice,
            _regressive_voice,
            _regressive_palatalization
        ),
        line,
    )
