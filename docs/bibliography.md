# Annotated bibliography: Computational identification and analysis of rhyme

## Ananian, C. Scott. 2001. “Perceptual salience in English reduplication.” Unpublished.

<https://cscott.net/Publications/proj4.pdf>   

The main focus of this article is not on poetic rhyme, but it describes a method for extracting rhyming pairs, including imperfect rhymes, from an English poetry corpus, using the CMU pronunciation dictionary. Information extracted from the *rhyme zone* is called the *rhyme skeleton* (skeletal because it looks at only vowels), and its onset is the *rhyme onset*. Procedure:

1. Looks only within *stanzas*, defined as sequences of more than one (to avoid titles) consecutive line separated by blank lines.
2. Extracts the rhyme skeleton, identified as vowels in the rhyme zone, ignoring consonants entirely.
3. Groups all lines within stanza that have identical rhyme skeletons (that is, identical rhyme-zone vowels, without regard to consonants) to identify rhyme scheme for stanza. This assumes (reasonably) that vocalic identify combined with consonantal difference is inexact rhyme, rather than non-rhyme.
4. Identifies *best scheme scores*, which is apparently (not stated explicitly, but this interpretation seems to match the examples) the percentage of stanzas that match the most common scheme. The scoring system apparently (also not explicit) requires a score of .75 or higher in order to accept the result, conservatively rejecting lower high scores as non-poems.    

Core methodological assumptions are, then, that:

1. Rhyme is identified only within stanzas.
2. This will fail to idenntify true rhyme in terza rima (both rhyme across tercets and, because single lines are not counted as stanzas, the final line).
3. Rhyme within stanzas is identified without regard to distance between lines. If applied to long stanzas, that is, to verse that is not actually stanzaic, this will falsely identify rhyme at long distance, where the phonetics may match but the distance is too great for a reader or listener to perceive a meaingful rhyme. 
2. On the first pass, rhyme requires identity of all vowels in rhyme skeleton. This will fail (provisionally) to identify rhyme where post-tonic (or, exceptionally, even tonic) vowels differ, including isosyllabic and anisosyllabic examples.
3. Stanza-level rhyme schemes are scored by frequency within the poem, and any that attains a certain score (apparently .75) is accepted, and then (perhaps; this is not explicit) projected back onto others. This may (also unclear) fail to handle poems with stanzas that have different rhyme schemes, although perhaps different schemes could be inferred for stanzas of different lengths within a poem, so that, e.g., sonnets that are lineated as 8-6 or 4-4-4-2 could have different rhyme schemes for the “stanzas” with different line counts.

## Kesarwani, Vaibhav. 2018. “Automatic poetry classification using natural language processing.” M.S. thesis, University of Ottawa. 

<https://ruor.uottawa.ca/bitstream/10393/37309/1/Kesarwani_Vaibhav_2018_thesis.pdf> 

Identify, score, and visualize rhyme information for English-language poetry, using CMU dictionary. Also looks at diction and metaphor. Includes conscientious definitions of terms, both literary and computational, and annotated review of relevant literature about computational analysis of poetry. Identifies original contributions as “rhyme quantification metric called RhymeScore” and “novel alt-n rhyme detection system” (3).

Procedure (32ff.):

1. Check line pairs for consecutive and alternate. Defines *alternate* as “and for Alternate, the last words on alternate lines” (31), but also “[i]n the Alternate rhyme detection, we are considering alternation with a line difference up to the full length of the poem (and not just 1).” (34)
2. Determine similarity: rich (rhymes with homonym), full (exact), slant (inexact).
3. Calculate RhymeScore, typically between 0 and 1, but may exceed 1 with overlap in subtypes. 
4. RhymeScore calculated first for each word (retaining the max where there are alternative pronunciations) and then averaged and normalized for entire poem. The score for a word pair is matched phoneme count / total phonemes in longer word. 
3. Possible valences:
	4. No corresponding segment (words of different length): skip
	5. n, VC mismatch, 0
	6. nv, VV mismatch, 0.2
	7. nc, CC mismatch, 0.4
	8. yv, VV match without stress, 0.6
	9. yc, CC match, 0.8
	10. yv* VV match with stress, 1
1. The total rhyme score of the poem is the sum of the scores of the word pairs, and represents *rhyme density* of the poem. (This seems to misuse the term *density*, which should be *after* normalization.) To normalize for line count (normalized rhyme score), divide consecutive line result by total number of lines - 1 (maximum possible). The divisor for alternate rhyme is (n - 1) * (n - 2) / 2 (34), where n is the line count. Scores types separately for each poem: End, Internal, Eye, Full, Rich, Identical, Slant. 
1. Poems can plotted (visualized) and clustered (analyzed) in two or three dimensions based those types. In the visualization, clicking on a poem node exposes the full text, with rhyme types colored.
2. See p. 41 for limitations and directions for future work.

The method is word-oriented, rather than line-oriented. On an organizational level it is lines that rhyme, but insofar as rhyme constructs meaning, the words matter.
It also aligns segments without regard to C ~ V; compare to Ananian 2001, who ignores consonants. It looks as if the segmental orientation can cause chaining mismatches if a consonant cluster matches a single consonant; the initial *[e]* in **nefarious** is aligned with the *[g]* in **glorious** as a VC mismatch (33), and it isn’t clear what this would mean for Russian **вы́бора** *[vIbara]* ~ **вы́борка** *[vIbarka]* or **мо́рда** *[mOrda]* ~ **го́рода** *[gOrada]*.




____

## To be checked

Noh, Zakiah, Siti Zaleha Zainal Abidim, and Nasiroh Omar. “Poetry visualization in digital technology.” In Meliha Handzic and Daniela Carlucci, eds. *Knowledge management, arts, and humanities. Interdisciplinary approaches and the benefits of collaboration.* Knowledge management and operational learning, 7. Cham, Switzerland: Springer Nature. 171–96.

GraphPoem (Margento 2012) graphs networks of poems, with connections based on shared “rhyme, meter, topic, diction, tropes, etc.” (Kesarwani 2018: 2).

“SPARSAR (Delmonte and Prati, 2014) is one such system that aims to study poetry by the use of NLP tools like tokenizers, sentence splitters, NER (Named Entity Recognition) tools, and taggers. In addition, the system adds syntactic and semantic structural analysis and prosodic modeling. The authors analyze poems by computing metrical structure and rhyming scheme.” (Kesarwani 2018: 23) Also cites Delmonte 2013. 

“Delmonte (2015) generates three relational views of a poem: phonetic, poetic and semantic. Each of these views shows a color-coded line-by-line representation of a single poem, whereas our system aims to compare multiple poems.” (Kesarwani 2018: 23)

“POEMAGE (McCurdy et al., 2016), another system for poetry analysis
is closer to ours in the sense that it aims to visualize the sonic elements of
a poem primarily rhyme types as a path view diagram.” (Kesarwani 2018: 23)

Myers, Austin, Leslie Milton, and Christine Lu. 2011. “VerseVis: visualization of spoken features in poetry.” Paper at <https://pdfs.semanticscholar.org/822f/5cc6a5f4b89e64efdbd25fc68a49fe27c37d.pdf>, linked from <https://www.semanticscholar.org/paper/VerseVis-%3A-Visualization-of-Spoken-Features-in-Milton-Lu/822f5cc6a5f4b89e64efdbd25fc68a49fe27c37d?tab=abstract&citingPapersSort=is-influential&citingPapersLimit=10&citingPapersOffset=0&year%5B0%5D=&year%5B1%5D=&citedPapersSort=is-influential&citedPapersLimit=10&citedPapersOffset=0>, which does not credit Myers.

“VerseVis (Milton and Lu) is another interesting work that aims to visualize rhyme and meter in a poem in a color-coded visual representation where height represents stress on a word and color represents a phoneme. The major  difference from our rhyme analysis (explained in Chapter 4) is that we do automatic detection of rhyme by matching phonemes in a word, whereas VerseVis focuses on manual detection and just shows the phoneme distribution of a poem visually.” (Kesarwani 2018: 23–24)

Abdul-Rahman, A., Lein, J., Coles, K., Maguire, E., Meyer, M., Wynne,
M., Johnson, C. R., Trefethen, A., and Chen, M. (2013). Rule-based
visual mappings–with a case study on poetry visualization. In Computer
Graphics Forum, volume 32, pages 381–390. Wiley Online Library.

“Abdul-Rahman et al. (2013) visualize a poem by phonetic and semantic connections with a latitudinal layout representation.” (Kesarwani 2018: 24)

“... based on rhyme patterns like AABBCC, AABCDD, etc. (Plamondon, 2006) (Delmonte, 2013) or based on just a few rhyme types (no rhyme sub-types) (Mittmann et al., 2016)” (Kesarwani 2018: 28)

“RhymeDesign (McCurdy et al., 2015) is a tool for analyzing sonic devices in
a poem by expressing rhymes as combinations of object components onset O,
nucleus N and coda C.” (Kesarwani 2018: 28)

Reddy and Knight (2011)

“Aoidos (Mittmann et al., 2016) is a system that analyzes rhymes in Portuguese poetry.” (Kesarwani 2018: 28)

“AnalysePoems by Plamondon (2006) also used rule-based patterns for classifying
rhymes in poetry.” (Kesarwani 2018: 29)

“The poetic style analysis carried out by Kao and Jurafsky (2015) involves
rhyme sub-types such as Identity/Perfect/Slant end rhyme, alliteration, consonance, and assonance that are very close to our sub-type categorization.” (Kesarwani 2018: 29)

