#!/usr/bin/env bash
nosetests -v --with-coverage --cover-package=cyr2phon --cover-tests dev/cyr2phon/tests/test_transliterate.py --cover-tests dev/cyr2phon/tests/test_utility.py
