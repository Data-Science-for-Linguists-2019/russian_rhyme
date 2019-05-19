[![Obdurodon](images/monotreme-obdurodon-blue.svg)](http://www.obdurodon.org)
[![Build Status](https://travis-ci.com/Data-Science-for-Linguists-2019/russian_rhyme.svg?branch=master)](https://travis-ci.com/Data-Science-for-Linguists-2019/russian_rhyme)
[![Code Coverage](https://codecov.io/gh/Data-Science-for-Linguists-2019/russian_rhyme/branch/master/graph/badge.svg)](https://codecov.io/gh/Data-Science-for-Linguists-2019/russian_rhyme)

# Machine-assisted identification of rhyme in Russian verse

David J. Birnbaum  

## Files and directories

### Code

#### Notebooks

* [Progress report 3 notebook](dev/progress_report_3.ipynb): decomposition into C(C) ~ V (replaces decomposition into syllable parts)
* [Syllable decomposition scratchpad](dev/syllable-decomposition.ipynb): scratch space for decomposition into syllables and into C(C) ~ V
* [Progress report 2 notebook](dev/progress_report_2.ipynb): decomposition into syllable parts (abandoned)
* [Progress report 1 notebook](dev/progress_report_1.ipynb): data preparation, syllabification

#### Library

* [*cyr2phon.py*](dev/cyr2phon/cyr2phon.py): Cyrillic to phonetic library; exposes `cyr2phon.transliterate()`
* [*utility.py*](dev/cyr2phon/utility.py): Utility functions; exposes `utility.syllabify()`

#### Development

* [*test_transliterate*](dev/cyr2phon/tests/test_transliterate.py): Nose tests for [transliteration code](dev/cyr2phon/cyr2phon.py)
* [*test_utility*](dev/cyr2phon/tests/test_utility.py): Nose tests for [utility code](dev/cyr2phon/utility.py) (syllabification)
* [*.travis.yml*](.travis.yml) and [*requirements.txt*](requirements.txt): Configuration information for [Travis CI](https://docs.travis-ci.com/user/tutorial/)

### Data (sample)
	
* [*eo1.xml*](dev/data_samples/eo1.xml): First book of Aleksandr Puškin’s *Eugene Onegin*; see the [Progress report](docs/progress_report.md#about-the-corpus) for a description of the data source

### Documentation

* [*project_plan.md*](docs/project_plan.md): Original project proposal
* [*degrees-of-rhyme.md*](docs/degrees-of-rhyme.md): Examples or types of imperfect rhyme, with discussion
* [*cluster-matching.md*](docs/cluster-matching.md): Discussion of challenges in aligning heterosegmental consonant clusters
* [*progress_report.md*](docs/progress_report.md): Progress report (last updated 2019-02-17)
* [*bibliography.md*](docs/bibliography.md): Annotated bibliography

____

**Acknowledgements**

* This project is a contribution to [Meter, rhythm, and rhyme: the computationally assisted analysis of formal features in Russian poetry](http://poetry.obdurodon.org/), co-developed by David J. Birnbaum and Elise Thorsen. The content here builds on collaborative work from that larger project. 
* Stanza markup in the Puškin corpus was implemented by Kyleen Pickering. 
* Thanks to Na-Rae Han, Jevon Heath, Daniel Zheng, and members of the University of Pittsburgh Spring 2019 Linguistics 1340 course for comments and suggestions.

