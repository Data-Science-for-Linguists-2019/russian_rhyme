#!/usr/bin/env bash
nosetests -v --with-coverage --cover-package=cyr2phon --cover-tests cyr2phon/tests/test_transliterate.py
