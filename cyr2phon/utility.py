"""Utility functions for Russian rhyme analysis

"""
import regex as re
import itertools  # use itertools.chain(*nested_list) to flatten nested list

# constants for syllabify() and _any_vowel
_VOWEL = "aeiouAEIOU"  # V
_SONORANT = "lrmnLRMNJ"  # S
_OBSTRUENT = "bvgdžzkpstfxɣčšBVGDŽǮZKPQSTFXČŠ"  # O
_CONSONANT = _SONORANT + _OBSTRUENT  # C

# constants for strip_onset()
_OPEN_PAT = re.compile(r'^.*[AEIOU]$')
_ONSET_PAT = re.compile(r'^.*(?=[AEIOU])')
_KEEP_FIRST = re.compile(r'.*?(.?[AEIOU])$') # keep final vowel plus optional first preceding consonant


def _any_vowel(remaining):
    return any(i in remaining for i in _VOWEL)


def syllabify(word):
    """
    Syllabify word in custom phonetic transliteration

    Parameter:
        word (str): word to syllabify, in custom phonetic transliteration

    Returns:
        str: hyphenated syllabified word
        TODO: return list of syllables instead of hyphenated string

    Segment types
        O = obstruent
        S = sonorant (here nasal **\[mnMN\]**, liquid **\[rR\]**, lateral **\[lL\]**, and palatal glide **\[J\]**)
        V = vowel

    Process
        1. Tokenize string into list of characters
        2. Scan list from left to process
        3. Process each character according to what follows
        4. Add result to output list

    Actions

    (syllable patterns from Terence Wade, *A comprehensive Russian grammar*, p. 19)

    Type | Environment | Action
    ---- | ----------- | -------
    C    | any         | C
    V    | end of word | V
    V    | before V    | V-
    V    | before LC   | VL- and skip the L in the loop
    V    | before CV   | V-
    V    | before CL   | V-
    V    | before CC   | V-
    """
    syllables = []
    skip = 0
    for i in range(len(word)):
        if skip == 1:
            skip = 0
        elif word[i] in _CONSONANT:
            syllables.append(word[i])
        else:  # must be a vowel
            if not _any_vowel(word[i + 1:]):  # this is the last syllable
                syllables.append(word[i])
            elif word[i + 1] in _VOWEL:  # VV
                syllables.append(word[i] + '-')
            elif word[i + 1] in _SONORANT and word[i + 2] in _CONSONANT:  # VLC
                syllables.append(word[i] + word[i + 1] + '-')
                skip = 1  # we worked ahead, so skip the next item in the loop
            else:  # must be a consonant after the vowel, and not VLC
                syllables.append(word[i] + '-')
    return [syllable for syllable in "".join(syllables).split('-')]


def strip_onset(l: list) -> list:
    """
    Strip onset characters before stressed vowel

    Parameter:
        l (list): list of syllables

    Returns:
        list: list of syllables with onset consonant stripped from first (stressed) one
    """
    if len(l) == 1 and _OPEN_PAT.match(l[0]):  # open masculine rhyme; keep supporting C
        return [_KEEP_FIRST.sub(r'\1', l[0])]
    else:  # otherwise trim pretonic C
        return list(itertools.chain(*[[_ONSET_PAT.sub("", l[0])], [item for item in l[1:]]]))  # flatten nested lists
