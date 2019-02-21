[![Obdurodon](images/monotreme-obdurodon-blue.svg)](http://www.obdurodon.org)
[![Build Status](https://travis-ci.com/Data-Science-for-Linguists-2019/russian_rhyme.svg?branch=master)](https://travis-ci.com/Data-Science-for-Linguists-2019/russian_rhyme)
[![Code Coverage](https://codecov.io/gh/Data-Science-for-Linguists-2019/russian_rhyme/branch/master/graph/badge.svg)](https://codecov.io/gh/Data-Science-for-Linguists-2019/russian_rhyme)

# Machine-assisted identification of rhyme in Russian verse

David J. Birnbaum  

## Files and directories

### Code

#### Notebook

* [Progress report 1 notebook](progress_report_1.ipynb)

#### Library

* [*cyr2phon*](cyr2phon/cyr2phon.py): Cyrillic to phonetic library; exposes `cyr2phon.transliterate()`

#### Development

* [*test_transliterate*](cyr2phon/tests/test_transliterate.py): Nose tests for [transliteration code](cyr2phon/cyr2phon.py)
* [*test_utility*](cyr2phon/tests/test_utility.py): Nose tests for [utility code](cyr2phon/utility.py) (syllabification)
* [*.travis.yml*](.travis.yml) and [*requirements.txt*](requirements.txt): Configuration information for [Travis CI](https://docs.travis-ci.com/user/tutorial/)

### Data (sample)

* [*eo1.xml*](data_samples/eo1.xml): First book of Aleksandr Puškin’s *Eugene Onegin*; see the [Progress report](progress_report.md#about-the-corpus) for a description of the data source

### Documentation

* [*project_plan.md*](project_plan.md): Original project proposal
* [*degrees-of-rhyme.md*](degrees-of-rhyme.md): Examples or types of imperfect rhyme, with discussion
* [*progress_report.md*](progress_report.md): Progress report (last updated 2019-02-17)

____

**Acknowledgements**

* This project is a contribution to [Meter, rhythm, and rhyme: the computationally assisted analysis of formal features in Russian poetry](http://poetry.obdurodon.org/), co-developed by David J. Birnbaum and Elise Thorsen. The content here builds on collaborative work from that larger project. 
* Stanza markup in the Puškin corpus was implemented by Kyleen Pickering. 
* Thanks to Na-Rae Han, Jevon Heath, and Daniel Zheng for comments and suggestions.

