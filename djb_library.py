def prepare_words(line: str) -> str:
    """Clean and flatten input

    Keyword argument:
    input -- line of poetry to process, as well-formed XML, with <stress> tags

    Convert stressed vowels to uppercase and remove stress tags
    Convert other text to lowercase
    Strip punctuation
    Normalize white space
    """
    from xml.dom import pulldom
    import string
    import re
    in_stress = 0  # are we inside a <stress> element?
    result = []  # accumulate output string
    punc_regex = re.compile("[" + string.punctuation.replace("-", "") + "]+")  # strip all punc except hyphen
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
    return punc_regex.sub("", "".join(result))

