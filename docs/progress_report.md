# Progress report

## First progress report

Last revised 2019-02-17

### Summary

Most progress to date has involved implementing a [Python library](../cyr2phon/cyr2phon.py) to convert Russian orthography to a phonetic representation that can be used to evaluate the phonetic similarity between line endings, which is one of the principal components of rhyme. The library exposes a single `transliterate()` function that transforms the Cyrillic input (see below for details about the structure) into a custom phonetic output (not yet documented!) that is easily parsed for subsequent phonetic analysis (decomposition into syllables, syllable parts [onset, nucleus, code], segments, phonetic features—not yet implemented). For ease in creation, testing, debugging, and maintenance, the `transliterate()` function is constructed as a pipeline of sixteen private functions that can be tested individually.

My Russian poetry input is in normal Russian orthography with light XML
markup. Specifically, poems are tagged as `<poem>`, stanzas are tagged as `<stanza>`, and lines are tagged as `<line>`. At the moment the corpus tags only the last stressed vowel in each line (as `<stress>`), which is the only one that matters for rhyme. There will be metadata included in each poem, but I have not yet decided on the markup for that. 

For example, a line looks like:

```xml
<line lineNo="001">"Мой дядя самых честных пр<stress>а</stress>вил,</line>
```

and an artificial one-stanza poem (it really the first stanza of Aleksandr Puškin’s *Eugene Onegin*) looks like:

```xml
<poem>
    <stanza stanzaNo="001">
        <line lineNo="001">"Мой дядя самых честных пр<stress>а</stress>вил,</line>
        <line lineNo="002">Когда не в шутку занем<stress>о</stress>г,</line>
        <line lineNo="003">Он уважать себя заст<stress>а</stress>вил</line>
        <line lineNo="004">И лучше выдумать не м<stress>о</stress>г.</line>
        <line lineNo="005">Его пример другим на<stress>у</stress>ка;</line>
        <line lineNo="006">Но, боже мой, какая ск<stress>у</stress>ка</line>
        <line lineNo="007">С больным сидеть и день и н<stress>о</stress>чь,</line>
        <line lineNo="008">Не отходя ни шагу пр<stress>о</stress>чь!</line>
        <line lineNo="009">Какое низкое ков<stress>а</stress>рство</line>
        <line lineNo="010">Полу-живого забавл<stress>я</stress>ть,</line>
        <line lineNo="011">Ему подушки поправл<stress>я</stress>ть,</line>
        <line lineNo="012">Печально подносить лек<stress>а</stress>рство,</line>
        <line lineNo="013">Вздыхать и думать про себ<stress>я</stress>:</line>
        <line lineNo="014">Когда же чорт возьмет теб<stress>я</stress>!"</line>
    </stanza>
</poem>    
```    

The `transliterate()` function converts the last word of the first line of this poem to: `prAVil`, where stressed vowels are uppercase, unstressed are lowercase, palatal and palatalized consonants are uppercase, and non-palatal, non-palatalized consonants are lowercase (that is, IPA [ˈpra.vʲil]). We use this custom transcription instead of IPA because it is more easily parsed for the sort in stress and feature-level information we use in rhyme analysis. (Real documentation of the transcription will be added later)

### About the corpus

I start with the works of Aleksandr Puškin (1799–1837) for both intellectual and opportunistic reasons. The intellectual reason is that Puškin, often compared to Lord Byron, is Russia’s best-known poet, a representative of the *Golden Age of Russian literature* (roughly the nineteenth century), and specifically of its Romantic period. The opportunistic reason is that I already have a Puškin dataset that marks the last stressed vowel in each line. Normal Russian orthography does not mark stress, and the location of the final stressed syllable of the line is fundamental to identifying and analyzing rhyme. That this position is already marked in my Puškin corpus means that I can extract the rhyming part of each line without having to mark the position of stress myself (whether manually or computationally).

The history of the corpus begins in 1969-1973, when J. Thomas Shaw (University of Wisconsin) arranged to have the complete poetic works of three leading poets of the Golden Age of Russian literature, A. S. Puškin (1799-1837), E. A. Baratynskij (1800-1844), and K. N. Batjuškov (1787-1855), keypunched. The data were stored on magnetic tape and used by Professor Shaw for research purposes through 1982, and when I communicated with Professor Shaw in 1996 the tapes had not been refreshed since that time. Professor Shaw sent me the nine tapes he was still able to find in the hope that it might be possible to salvage the data, so that it could continue to be used in the study of Russian poetry.

Eileen Kopchik and Barbara Hieber of the University of Pittsburgh were able to read four of the nine tapes and recover the data from them. One proved to contain UNIVAC utilities and what appeared to be an ancient version of Dungeons and Dragons, but nothing pertaining to Russian poetry. Three others contained concordances and frequency analyses of the Puškin poetry; they did not contain transcriptions of entire poems, but there was sufficient indexing information in the concordances that I was able to reconstruct the original poems, which I converted first to SGML and then to XML. The only information that could not be reconstructed automatically was the stanza structure, which was recorded for only a portion of the concordance, and stanza markup was reintroduced manually by Kyleen Pickering (then at the University of Pittsburgh) in 2017–18. The remaining five tapes were in a 7-track format that we were unable to read, and although we sent them to other institutions that had access to vintage tape readers (including the Johnson Space Center, which generously agreed to look at them for us), those efforts were not successful. Eventually I returned all of the tapes to Professor Shaw.

I currently have a complete copy of the Puškin poetry that I was able to reconstruct from the Shaw corpus in XML form with full stanza and line tags, stress tags on the final stressed vowel of each line, and descriptive metadata about each poem.

### Sharing plan

I do not have permission to share the Shaw Corpus, Shaw himself passed away in 2011, and it is unclear who the owner is of the intellectual property. For the moment I will post, under Fair Use, illustrative samples of my derived XML, while working with the larger corpus (see below). 

### About the *EO* subcorpus

I will start with Puškin’s *Eugene Onegin* (*EO*) because it is a long work with a consistent rhyme scheme, which makes it easy to validate automated rhyme analysis without manually tagging the corpus for rhyme. The structure of *EO* is “389 fourteen-line stanzas (5,446 lines in all) of iambic tetrameter with the unusual rhyme scheme ‘AbAbCCddEffEgg’, where the uppercase letters represent feminine rhymes while the lowercase letters represent masculine rhymes”. (<https://en.wikipedia.org/wiki/Eugene_Onegin>)

The disadvantage of working only with the *EO* subcorpus is that any modeling will be not of Russian rhyme in general, but of Puškin’s rhyme, and specifically of his rhyme in *EO*. Furthermore, although Puškin’s rhyming, and his poetic craft in general, is universally regarded as virtuosic, rhyme patterns of the Golden Age were stricter than those of later periods, and, in particular, stricter than those of the innovative and experimental *Silver Age of Russian literature* (roughly the first third of the twentieth century, characterized by such literary movements as Symbolism, Futurism, and Acmeism). This means that Puškin’s oeuvre is likely to be less rich in approximate rhyme—which is our eventual principal object of study—than later poetry. On the other hand, the relative strictness of Puškin’s rhyming practice means that we can develop and test our methods with this simpler dataset before attempting to apply those methods to data that is more varied in its use of rhyme.

### Link to notebooks

* [Progress report 1 notebook](../dev/progress_report_1.ipynb) 

### Link to data samples

* [eo1.xml](../data_samples/eo1.xml): First book of Aleksandr Puškin’s *Eugene Onegin*

### What I learned (or relearned)

* Creating and using a package
* Using `reduce()` to construct a function pipeline
* Using the `regex` package as a replacement for `re` to support nested sets and set operations on patterns	
* Using closures (compared to imperative and object-oriented approaches to encapsulation)
* Creating and running nose tests
	* Inside PyCharm and on the command line
	* With coverage
	* Parameterizing tests with `for` loops
* Configuring Travis CI on GitHub
	* Pinning an earlier release after an updated dependency broke

____

## Rubric

For the 1st progress report, **focus on your data**. This milestone consists of 30 data points and 10 presentation points. Goals:

* **[done]** Attempt and mostly complete the data acquisition process.
* **[done]** Start and make headway into cleaning and reorganizing your data.
* **[done]** By now, you should have concrete ideas on the “data end game”: what your data’s final form will be like, the target total size, format, etc.
* **[done]** Devise a couple of options regarding the “sharing plan” of your data.

Contents:

1. *progress_report.md*
	* **[done]** Create a section entitled “1st Progress Report”, and then provide a summary of what you accomplished. Keep it short (a screen-full), and provide links to related documents, including your Jupyter Notebook and data samples.
	* **[done]** Include a subsection where you outline a couple of options (or a single option, if you are fairly sure) regarding the “sharing plan” for your data. You should plan out how much and what you will be sharing. Make sure to include a justification.
2. A python script in the form of a Jupyter Notebook.
	* **[done]** Provide an overview of your data. Clearly document each step of your data processing pipeline.
	* **[done]** Compile some basic stats on your data: the size and the make up are the bare minimum.
	* **[done]** Bullet points have their uses, but let’s see some written summaries and explanations too.
	* **[done]** Remember: your Jupyter Notebook file is also your presentation. Make it easy for the instructors and your classmates to understand what you are doing. Explain your goals, show your data and your processes.
3. **[done]** Some *form* of your data. If all of your data is currently stored in a git-ignored directory, make an appropriately sized samples available in a directory called `data_samples/`.
	
Above are the minimum requirements, but do feel free to impose additional organization as you see fit. This is your project after all! But when you do so, make sure you provide an explanation.