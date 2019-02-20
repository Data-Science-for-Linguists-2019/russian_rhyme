"""
Parses XML poem into individual <line> elements

Documentation at https://www.balisage.net/Proceedings/vol21/html/Birnbaum01/BalisageVol21-Birnbaum01.html#d9505e2070
"""

# TODO: Currently ignores <latin> elements and associated language tags

from xml.dom import pulldom
from xml.dom.minidom import Document
import pandas as pd
import regex as re


class Stack(list):
    def push(self, item):
        self.append(item)

    def peek(self):
        return self[-1]


open_elements = Stack()
WS_RE = re.compile(r'\s+')


# noinspection PyUnboundLocalVariable
def process(input_xml):
    stanzaNo = 0
    lineNo = 0
    inline = 0
    result = []
    doc = pulldom.parse(input_xml)
    for event, node in doc:
        if event == pulldom.START_ELEMENT and node.localName == 'stanza':
            stanzaNo = node.getAttribute("stanzaNo")
        elif event == pulldom.START_ELEMENT and node.localName == 'line':
            d = Document()  # each line is an output XML document
            open_elements.push(d)  # document node
            lineNo = node.getAttribute("lineNo")
            inline = 1
            open_elements.peek().appendChild(node)  # add as child of current node in output tree
            open_elements.push(node)  # keep track of open elements
        elif event == pulldom.END_ELEMENT and node.localName == 'line':
            inline = 0
            open_elements.pop()  # line is finished
            # TODO: output line stanzaNo, lineNo, line into the dataframe
            result.append([int(stanzaNo), int(lineNo),
                              WS_RE.sub(" " ,open_elements.pop().toxml().replace('<?xml version="1.0" ?>', ''))])
        elif event == pulldom.START_ELEMENT and node.localName == 'stress':
            open_elements.peek().appendChild(node)  # add as child of current node in output tree
            open_elements.push(node)  # keep track of open elements
        elif event == pulldom.END_ELEMENT and node.localName == 'stress':
            open_elements.pop()  # line is finished
        elif event == pulldom.CHARACTERS and inline:  # keep text only inside lines
            t = d.createTextNode(node.data)
            open_elements.peek().appendChild(t)
    return result

with open("data_samples/eo1.xml") as f:
    all_lines = process(f)
df = pd.DataFrame(all_lines)
print(df.head())