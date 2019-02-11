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
    _vowel_reducation() : unstressed non-high vowels are i after soft consonants and i < e, a < o after hard
    _strip_spaces() : remove all spaces
"""
# imports
from xml.dom import pulldom
import string
import re
import json

# constants
PUNC_REGEX = re.compile("[" + string.punctuation.replace("-", "") + "]+")  # strip all punc except hyphen
OGO_RE = re.compile(r'([ео])г([ео])$', re.IGNORECASE)  # -ogo that needs to be changed to -ego
OGO_EXCEPTIONS = {"немнОго", "мнОго", "стрОго", "убОго", "разлОго", "отлОго", "полОго"}  # exceptions to the above
with open("lexical.json") as f:  # lexical exceptions (match: replace JSON objects)
    tmp = json.load(f)
ALL_LEXICAL_RE = re.compile("|".join(tmp.keys()))  # omnibus regex, keys are strings for this part
LEXICAL_RE = {re.compile(key): value for key, value in tmp.items()}  # now make them regexes for lookup


def flatten(line: str) -> str:
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
    return PUNC_REGEX.sub("", "".join(result))


def ogo(word: str) -> str:
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
    if ALL_LEXICAL_RE.search(word):  # check for any match to avoid checking all of them when not needed
        for key in LEXICAL_RE.keys():  # there's a match, so find the right key
            if key.search(word):
                word = key.sub(LEXICAL_RE[key], word)
                break
    if word not in OGO_EXCEPTIONS:  # g -> v unless exception
        if word == "сегОдня":  # nonce exceptions
            word = "севОдня"
        elif word not in OGO_EXCEPTIONS:
            word = OGO_RE.sub(r'\1в\2', word)
    return word
