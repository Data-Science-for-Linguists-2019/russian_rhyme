# Identifying Russian rhyme

David J. Birnbaum  
djbpitt@gmail.com  
http://www.obdurodon.org 

## Summary

End-rhyme in Russian verse works similarly to English end-rhyme: we recognize two lines of poetry as rhyming when their endings conform to a certain measure of phonetic similarity (also subject to other constraints; see below). Given a corpus of Russian poetry, what can machine learning contribute to identifying rhyme—both exact rhyme and imperfect (inexact, slant) rhyme? Can machine-learning methods outperform rules-based rhyme analysis? Can rules-based and machine-learning methods be combined to produce better results than either might offer alone?

## Data

### What will your data look like

I have acces to a corpus of Russian verse that contains approximately 45,000 poems, with each poem in a separate XHTML file. The encoding is CP 1251, and the XHTML markup, which is well-formed, is not very informative, both in general and with respect to rhyme, which is recorded only in a summary way within poorly structured metadata. 

### What sorts of data sourcing and cleaning up effort will be involved?

The cleaning pipeline might look something like:

2. Batch convert to UTF-8 using _iconv_.  
1. Also as a batch process, strip out all or most XML markup using XSLT. Whether to work with plain text or XML needs to be determined. 

### Do you have a sense of the overall data size you should be aiming for?

The portion of the corpus to be used in this course project remains to be determined, but insofar as the cleaning can be done in batch, to the extent that the size will be limited, it will probably be limited for literary, rather than manpower reasons. Specifically, poets vary in the regularity and strictness of their rhyming practice, and in the type of approximate rhyme they admit, and not all poems are rhymed. The amount of data also varies by poet, which creates a risk of overfitting during training.

### Do you have an existing data source in mind that you can start with, and if so, what are the URLs or references?

[To be added after consultation.]

### Analysis

#### Learning goal

The *learning* goal is to acquire knowledge and experience with machine learning methods, that is, not just to identify and analyze rhyme, but to learn specificallly how machine learning can contribute to that identification and analysis. With respect to the prompt “Are you planning to do any predictive analysis (machine learning, classification, etc.), and using what methods?”, my goal is to learn what machine learning can contribute, and at present I know nothing about it, and therefore do not yet know which methods I will use. 

#### Research goal

The *research* goal is to identify which lines function as rhyming with which other lines within the corpus. Rhyme seems to depend on at least three things: phonetic similarity, distance between the lines, and the overall rhyme scheme of the poem (which must be determined, as it is not known in advance). Each of these three parameters is gradual, and the thresholds (how phonetically similar?, how far apart?, how should we characterize the rhyme scheme?) vary.

#### Discussion of research plans

An important aspect of rhyme analysis is to identify not only exact rhyme, but also approximate rhyme. This means distinguishing approximate rhyme (“these lines rhyme even though the endings are only phonetically similar, and not identical”) from non-rhyme (“these line endings are phonetic similar, but a human would not perceive them as rhyming”).

Within approximate rhyme, I hypothesize that certain phonetic differences may be more likely to be neutralized than others, although those tendencies may vary with poet, poetic school, period, and perhaps other properties. That is, understanding what different Russian poets regarded as constituting an approximate rhyme, rather than a non-rhyme, entails not just the degree of difference between strings (however that might be measured), but also the nature of the difference, that is, the distinctive features that can be ignored for rhyming purposes. 

Since the original input is Russian verse in standard Russian orthography, the tasks above entail at least the following pipeline stages:

1. Converting from orthography to phonetics
1. Divide the phonetic stream into syllables.
2. Divide the syllables into onset, nucleus, and coda.
3. Divide the onset, nucleus, and coda into phones.
4. Decompose each sound into phonetic distinctive features. 

I have already developed algorithms for these tasks and implemented them in XSLT, but I will need to port them to Python. The application of machine learning methods (to be determined) to identifying and analyzing rhyme will be entirely new.

### Presentation 

Web publication including:

1. Poem transcriptions with highlighting and interactivity to support the exploration of rhyme on the level of an individual poem. Details to be determined.
2. Graph and chart representations of patterns in the aggregated data. How can we represent, in a graphic way, how poets differ in the types of approximate rhyme they permit? Do poets cluster according to their preferences with respect to approximate rhyme? Does the practice of an individual poet with respect to approximate rhyme differ over time?