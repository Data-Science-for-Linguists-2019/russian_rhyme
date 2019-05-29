"""
cyrcluster.py

Public functions that return:
    explore(filepath, ceiling=1000, ward=False)
        returns df
    analyze(filepath, ceiling=1000, ward=False)
        returns cophenetic correlation coefficients for different clustering methods and distance metrics

Public functions that render but do not return:
    box(filepath, ceiling=1000, ward=False):
        no return; render comparative box plots from return of analyze()
    visualize(filepath, ceiling=1000, ward=False)
        no return; prints text and renders dendrograms directly

TODO: No tests, and the functions are not testable

"""
# imports
from xml.dom import pulldom  # parse input XML
from xml.dom.minidom import Document  # construct output XML
import numpy as np
import pandas as pd
from scipy import stats
from scipy.cluster.hierarchy import dendrogram, linkage
# see https://joernhees.de/blog/2015/08/26/scipy-hierarchical-clustering-and-dendrogram-tutorial/
from scipy.cluster.hierarchy import cophenet
from scipy.spatial.distance import pdist
import matplotlib.pyplot as plt
import seaborn as sns
import regex as re
import cyr2phon.cyr2phon


# Class and variables for parsing input XML
class Stack(list):  # keep track of open nodes while constructing XML output
    def push(self, item):
        self.append(item)

    def peek(self):
        return self[-1]


open_elements = Stack()
WS_RE = re.compile(r'\s+')  # normalize white space in output


# Function to parse the XML
def process(input_xml):
    poemId = ""
    stanzaNo = 0
    lineNo = 0
    inline = 0  # flag to control behavior inside and outside lines
    result = []  # array of arrays, one per line, with stanzaNo, lineNo, and serialized XML
    doc = pulldom.parse(input_xml)
    for event, node in doc:
        if event == pulldom.START_ELEMENT and node.localName == 'poem':
            poemId = node.getAttribute("opid")
        elif event == pulldom.START_ELEMENT and node.localName == 'stanza':
            stanzaNo = node.getAttribute("stanzaNo")
        elif event == pulldom.START_ELEMENT and node.localName == 'line':
            d = Document()  # each line is an output XML document
            open_elements.push(d)  # document node
            lineNo = node.getAttribute("lineNo")
            inline = 1  # we’re inside a line
            open_elements.peek().appendChild(node)  # add as child of current node in output tree
            open_elements.push(node)  # keep track of open elements
        elif event == pulldom.END_ELEMENT and node.localName == 'line':
            inline = 0  # when we finish our work here, we’ll no longer be inside a line
            open_elements.pop()  # line is finished
            # serialize XML, strip declaration, rewrite &quot; entity as character
            result.append([poemId, int(stanzaNo), int(lineNo),
                           WS_RE.sub(" ",
                                     open_elements.pop().toxml().replace('<?xml version="1.0" ?>', '').replace('&quot;',
                                                                                                               '"'))])
        elif event == pulldom.START_ELEMENT and node.localName == 'stress':
            open_elements.peek().appendChild(node)  # add as child of current node in output tree
            open_elements.push(node)  # keep track of open elements
        elif event == pulldom.END_ELEMENT and node.localName == 'stress':
            open_elements.pop()  # stress element is finished
        elif event == pulldom.CHARACTERS and inline:  # keep text only inside lines
            t = d.createTextNode(node.data)
            open_elements.peek().appendChild(t)
    return result


# Function to extract rhyme zone from rhyme word
rhymezonepat = re.compile(r'(.?[AEIOU]$)|([AEIOU].*$)')


def remove_pretonic_segments(s: str) -> str:  # removes segments in place
    try:
        return rhymezonepat.search(s).group(0)
    except:  # modify this to raise a real error, instead of just reporting
        print(s)


# Imports sample file, analyzes
def explore(filepath, ceiling=1000, ward=None):
    """Render text and dendrograms of rhyme clustering

    Parameters:
        filepath (str): path to XML file with poem, required
        ceiling (int): maximum number of stanzas to return (useful for sampling long poems),
            defaults to high value
        ward (boolean): show Ward dendrogram separately (improves legibility of long stanzas),
            defaults to None

    Return: df
    """

    # Read file
    with open(filepath) as f:
        data = process(f)
    df = pd.DataFrame(data, columns=["PoemId", "StanzaNo", "LineNo", "Text"])

    # Prepare data
    trans_vec = np.vectorize(cyr2phon.transliterate)
    df["Phonetic"] = trans_vec(df["Text"])
    df["RhymeWord"] = df["Phonetic"].str.split().str[-1]  # clitics have already been joined
    df["RhymeZone"] = df["RhymeWord"].apply(remove_pretonic_segments)
    df.loc[df["RhymeZone"].isnull(), "RhymeZone"] = "Abcde"  # provisional placeholder for nulls
    df["tokenized"] = [x[0] for x in df["RhymeZone"].str.
        findall(
        r"(.?)([AEIOU])([^aeiou]*)([aeiou]?)([^aeiou]*)([aeiou]?)([^aeiou]*)([aeiou]?)([^aeiou]*)([aeiou]?)([^aeiou]*)([aeiou]?)([^aeiou]*)([aeiou]?)([^aeiou]*)([aeiou]?)([^aeiou]*)([aeiou]?)")]
    i = 0
    while pd.np.count_nonzero([item[i] for item in df["tokenized"]]) > 0:
        # print([item[i] for item in df["tokenized"]]) # diagnostic
        df["token" + str(i)] = [item[i] for item in df["tokenized"]]
        i += 1
    tokenheaders = df.filter(regex="^token\d").columns
    # tokenheaders = list([item for item in df.columns if re.match(r'token\d', item)])
    df[tokenheaders] = df[tokenheaders].replace(r'^$', "missing",
                                                regex=True)  # replace empty strings with specific value; inplace doesn't work (?)
    df.filter(regex=r"StanzaNo|LineNo|RhymeWord|Text|^token\d").head()  # columns we care about
    dummy = pd.get_dummies(df, columns=df.filter(regex="^token\d").columns, drop_first=True)
    df = df.merge(dummy, on=["PoemId", "StanzaNo", "LineNo", "Text", "Phonetic", "RhymeWord", "RhymeZone", "tokenized"])
    df.set_index(["PoemId", "StanzaNo", "LineNo"], inplace=True)
    return df


# Analyze
def analyze(filepath, ceiling=1000, ward=None):
    """Return cophenetic correlation coefficients for different clustering methods and distance metrics

    Parameters:
        filepath (str): path to XML file with poem, required
        ceiling (int): maximum number of stanzas to return (useful for sampling long poems),
            defaults to high value
        ward (boolean): show Ward dendrogram separately (improves legibility of long stanzas),
            defaults to None

    Return: dictionary with two keys (euclidean and cosine) and values as df of values
    """

    df = explore(filepath, ceiling, ward)
    methods = {"euclidean": ["single", "complete", "average", "weighted", "centroid", "median", "ward"],
               "cosine": ["single", "complete", "average", "weighted"]}
    metrics = ["euclidean", "cosine"]
    result = {}
    for cm in metrics:  # cm is the clustering metric (euclidean or cosine)
        df_interim = pd.DataFrame()
        stanzas = df.groupby(level=[0, 1])
        for offset, (id, lines) in enumerate(stanzas):
            if offset < ceiling:
                s_interim = pd.Series()
                data = lines.copy().filter(regex=r"^token\d_")  # only one-hot features
                labelList = list(range(1, len(lines) + 1))  # labels are line numbers within stanza
                data.loc[:, "LineNo"] = [2 * n / len(labelList) for n in
                                         labelList]  # scale to avoid tyranny of proximity
                for n, m in enumerate(methods[cm]):
                    linked = linkage(data, method=m, metric=cm)
                    m_c, m_coph_dist = cophenet(linked, pdist(data))
                    s_interim[m] = m_c
                df_interim = df_interim.append(s_interim, ignore_index=True)
        result[cm] = df_interim
    return result


# Visualize
def visualize(filepath, ceiling=1000, ward=None):
    """Render dendrograms of rhyme clustering

    Parameters:
        filepath (str): path to XML file with poem, required
        ceiling (int): maximum number of stanzas to return (useful for sampling long poems),
            defaults to high value
        ward (boolean): show Ward dendrogram separately (improves legibility of long stanzas),
            defaults to None

    Return: No return; prints text and renders dendrograms directly
    """

    df = explore(filepath, ceiling, ward)
    stanzas = df.groupby(level=[0, 1])
    i = 0
    for id, lines in stanzas:
        if i < 11:
            print(pd.concat([lines["Text"].str.replace(r"<[^>]+?>", ""), lines[["RhymeWord", "RhymeZone"]]],
                            axis=1))  # diagnostic
            data = lines.copy().filter(regex=r"^token\d_")  # only one-hot features
            labelList = list(range(1, len(lines) + 1))  # labels are line numbers within stanza
            data.loc[:, "LineNo"] = [2 * n / len(labelList) for n in labelList]  # scale to avoid tyranny of proximity
            complete = linkage(data, method="complete")
            complete_c, complete_coph_dist = cophenet(complete, pdist(data))
            ward = linkage(data, method="ward")
            ward_c, ward_coph_dists = cophenet(ward, pdist(data))
            plt.figure(figsize=(12, 4))
            plt.subplot(1, 2, 1)
            plt.title("Complete: " + str(complete_c))
            dendrogram(complete, labels=labelList)
            plt.subplot(1, 2, 2)
            plt.title("Ward: " + str(ward_c))
            dendrogram(ward, labels=labelList)
        i += 1
    plt.show()

    
# Box
def box(filepath, ceiling=1000, ward=None):
    """Render text and dendrograms of rhyme clustering

    Parameters:
        filepath (str): path to XML file with poem, required
        ceiling (int): maximum number of stanzas to return (useful for sampling long poems),
            defaults to high value
        ward (boolean): show Ward dendrogram separately (improves legibility of long stanzas),
            defaults to None

    Return: No return; renders comparative box plots of cophenetic correlation coeffieicnets of clustering methods
        and distance metrics
    """

    comparison = analyze(filepath, ceiling=1000, ward=None)
    plt.figure(figsize=(15, 4))
    for n,(id, content) in enumerate(comparison.items()):
        plt.subplot(1, 2, n + 1)
        plt.title(id)
        plt.ylim(.75, 1)
        content.boxplot()
    plt.show()