# Annotated bibliography: Computational identification and analysis of rhyme

## Rhyme-related

### Abdul-Rahman, A., Lein, J., Coles, K., Maguire, E., Meyer, M., Wynne, M., Johnson, C. R., Trefethen, A., and Chen, M. 2013. “Rule-based visual mappings–with a case study on poetry visualization.” 

Eurographics Conference on Visualization (EuroVis) 2013, volume 32, issue 3, part 4, pages 381–90. Wiley Online Library. <https://doi.org/10.1111/cgf.12125>

Rhyme is computed, but method is not discussed. Visualized as dendrogram to left edge of interlinear full text and graphic representation of phonetic features. PoemViewer. “Abdul-Rahman et al. (2013) visualize a poem by phonetic and semantic connections with a latitudinal layout representation.” (Kesarwani 2018: 24) “The poetic variables that are included in Poem Viewer are consonants, vowels, assonance, alliteration, rhyme, semantic relations, and many more.” (Noh et al. 2019: 177)

### Ananian, C. Scott. 2001. “Perceptual salience in English reduplication.” 

Unpublished. <https://cscott.net/Publications/proj4.pdf>   

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

### Coles, Katharine and Julie Gonnering Lein. 2013. “Finding and figuring flow: Notes toward multidimensional poetry visualization.”

Conference 2013 Proceedings (pp. 444-48). <http://hdl.handle.net/2142/38940> (Listed DOI of https://doi.org/10.9776/13250 is invalid.)

Arcs link related sounds, which can be color coded. Acknowledge that patterns are difficult to discern, no explicit alternative yet.

### Delmonte, Rodolfo 2015. “Visualizing poetry with SPARSAR. Visual maps from poetic content.”

*4th Workshop on Computational Linguistics for Literature* (CLfL 2015), 68–78. <https://iris.unive.it/retrieve/handle/10278/3660561/43196/newvisualizing_final.pdf>

Cites several earlier paper by Delmonte, some with coauthors. “SPARSAR (Delmonte and Prati, 2014) is one such system that aims to study poetry by the use of NLP tools like tokenizers, sentence splitters, NER (Named Entity Recognition) tools, and taggers. In addition, the system adds syntactic and semantic structural analysis and prosodic modeling. The authors analyze poems by computing metrical structure and rhyming scheme.” (Kesarwani 2018: 23) Also cites Delmonte 2013. 

“Delmonte (2015) generates three relational views of a poem: phonetic, poetic and semantic. Each of these views shows a color-coded line-by-line representation of a single poem, whereas our system aims to compare multiple poems.” (Kesarwani 2018: 23)

### Kaplan, David Maxwell 2006. “Computational analysis and visualized comparison of style in American poetry.”

B.S. Thesis, Princeton, 2006. <http://faculty.missouri.edu/kaplandm/pdfs/KaplanBlei2007_ComputationalPoetryStyle_long.pdf>

“As the poem text is scanned, the phoneme sequences that make up the line endings are examined. The sequences start with the consonants before the final stressed vowel phoneme of a line (or simply the final vowel for lines ending with monosyllabic words) and continue to the end of the line of text. A window of four line endings at a time is analyzed. There are four basic types of rhyme, and three additional metrics combining them into “partial rhyme” (slant+semi), “full rhyme” (perfect+identity), and any rhyme (sum of all four). The definitions used are: Identity rhyme: the phoneme sequences are identical. Perfect rhyme: the initial consonants differ, but from the stressed vowel onward the sequences are identical. Semirhyme: a perfect rhyme where one word has an additional syllable at the end, such as “stick” and “picket.” Slant rhyme: either the stressed vowels are identical, or the phoneme strings following the stressed vowels are identical, but not both (otherwise it would be a perfect or identity rhyme). No rhyme: everything else.” (41)

### Kesarwani, Vaibhav. 2018. “Automatic poetry classification using natural language processing.”  

M.S. thesis, University of Ottawa. <https://ruor.uottawa.ca/bitstream/10393/37309/1/Kesarwani_Vaibhav_2018_thesis.pdf> 

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

### Kondrak, Grzegorz. 2000. “A new algorithm for the alignment of phonetic sequences.” 

*Proceedings of the 1st North American chapter of the Association for Computational Linguistics conference, Seattle, Washington, April 29–May 4, 2000.* 288–95. Download link at <https://dl.acm.org/citation.cfm?id=974343>. 

Pairwise dynamic programming approach, targeted at historical cognates. Cites:

* Covington (1996, 1998), who looks only at C ~ V ~ R, weightings determined by trial and error.
* Gildea and Jurafsky (1996) and Neerbone and Heeringa (1997), feature-based, using Hamming distance. 

Criticizes binary features because some aspects of articulation, such as front ~ back position, are better described as gradual. Thus Ladefoged (1995), Connolly (1997), and Somers (1998). Criticizes their models because they neglect *salience*, i.e., are unweighted (asserts that place and manner should be weighted most heavily). Favors similarity (large positive and negative values for related and unrelated, small negative for indel) over distance (unmatched features); this is not a metric because not all identical segments will have the same weight. Indel is constant penalty for gap plus scaled penalty for length of gap, since changes may not be at the level of individual segments.

The use of gradual features for place, manner, high, and back is sensible for language change, but not clearly relevant for rhyme, where, among other things, acoustic features may be more important than articulatory ones. Original treatment of gaps of different lengths is similarly relevant for language change, but less clearly useful for rhyme identification. 

### McCurdy, N., Lein, J., Coles, K., & Meyer, M. (2016). “Poemage: visualizing the sonic topology of a poem.” 

*IEEE transactions on visualization and computer graphics,* 22(1), 439–48. <https://doi.org/10.1109/TVCG.2015.2467811>. Source code (in Processing) at <http://www.sci.utah.edu/~nmccurdy/Poemage/>. 

Simultaneous and interlinked color-coded rhyme set, text, and image views (nodes are rhyming words), with the latter representing sonic paths. Rhyme typology (defined broadly) on p. 443. “Poemage [... is a ...] system for poetry analysis is closer to ours in the sense that it aims to visualize the sonic elements of a poem primarily rhyme types as a path view diagram.” (Kesarwani 2018: 23) Built on top of RhymeDesign (McCurdy et al., 2015): “a tool for analyzing sonic devices in
a poem by expressing rhymes as combinations of object components onset O, nucleus N and coda C.” (Kesarwani 2018: 28)

### Mittmann, Adiel, Aldo Von Wangenheim, and Alckmar Luiz Dos Santos. 2016. “Aoidos: a system for the automatic scansion of poetry written in Portuguese.”

In *Computational linguistics and intelligent text processing - 17th international
conference, CICLing 2016, Konya, Turkey, April 3-9, 2016, revised
selected papers, part {II} pp.611-28. <https://www.researchgate.net/publication/323875384_Aoidos_A_System_for_the_Automatic_Scansion_of_Poetry_Written_in_Portuguese>

Two-pass identification of meter that uses ordered rules to deal with elision, syncope, apheresis, crasis, sylaloepha. Rhyme apparently does pairwise comparisons, apparently only for exact matches, although neither of those is stated explicitly. Reuses up to last ten rhyme-scheme letters.

“Aoidos (Mittmann et al., 2016) is a system that analyzes rhymes in Portuguese poetry.” (Kesarwani 2018: 28)

### Myers, Austin, Leslie Milton, and Christine Lu. 2011. “VerseVis: visualization of spoken features in poetry.” 

Paper at <https://wiki.cs.umd.edu/cmsc734_11/images/0/0e/VerseVis.pdf> and <https://pdfs.semanticscholar.org/822f/5cc6a5f4b89e64efdbd25fc68a49fe27c37d.pdf>. The latter is linked from <https://www.semanticscholar.org/paper/VerseVis-%3A-Visualization-of-Spoken-Features-in-Milton-Lu/822f5cc6a5f4b89e64efdbd25fc68a49fe27c37d?tab=abstract&citingPapersSort=is-influential&citingPapersLimit=10&citingPapersOffset=0&year%5B0%5D=&year%5B1%5D=&citedPapersSort=is-influential&citedPapersLimit=10&citedPapersOffset=0>, which does not credit Myers. 

Interactive; about visualization, rather than quantitative analysis. “VerseVis (Milton and Lu) is another interesting work that aims to visualize rhyme and meter in a poem in a color-coded visual representation where height represents stress on a word and color represents a phoneme. The major  difference from our rhyme analysis (explained in Chapter 4) is that we do automatic detection of rhyme by matching phonemes in a word, whereas VerseVis focuses on manual detection and just shows the phoneme distribution of a poem visually.” (Kesarwani 2018: 23–24)

### Noh, Zakiah, 2019. Siti Zaleha Zainal Abidim, and Nasiroh Omar. “Poetry visualization in digital technology.” 

In Meliha Handzic and Daniela Carlucci, eds. *Knowledge management, arts, and humanities. Interdisciplinary approaches and the benefits of collaboration.* Knowledge management and operational learning, 7. Cham, Switzerland: Springer Nature. 171–96.

Good review of visualization literature, with comparative table on pp. 184–85. Malay examples with graphic visualization of each sound in grid, with icons for manner and coarticulation features.

### Marc R. Plamondon. 2006. “Virtual verse analysis: analysing patterns in poetry.”

*Literary and linguistic computing, 21 (suppl 1): 127–41.

Basic approach to the identification of meter is similar to the one we use in <http://poetry.obdurodon.org>. Rhyme uses a training corpus to build a table of pairs of rhyming words, tests candidate rhyme schemes, most trouble with ABAB ~ ABCB. No discussion of whether slant rhyme is included.

“AnalysePoems by Plamondon (2006) also used rule-based patterns for classifying
rhymes in poetry.” (Kesarwani 2018: 29)

### Reddy, Sravana and Kevin Knight. 2011. “Unsupervised discovery of rhyme schemes.”

*Proceedings of the 49th Annual Meeting of ACL: shortpapers*, 77-82.

Colored visualizations of different features, including consonance and assonance, with rhyme scheme in traditional AB notation. No description of rhyme identification algorithm, except that it is based on phonetic matching. 

“Reddy & Knight (2011) produce an unsupervised machine learning algorithm for finding rhyme schemes which is intended to be language-independent. It works on the intuition that ‘a collection of rhyming poetry inevitably contains repetition of rhyming pairs. ... This is partly due to sparsity of rhymes – many words that have no rhymes at all, and many others have only a handful, forcing poets to reuse rhyming pairs.’ The authors harness this repetition to build an unsupervised algorithm to infer rhyme schemes, based on a model of stanza generation. [... ] The definition of rhyme the authors used is the strict one of perfect rhyme: two words rhyme if their final stressed vowels and all following phonemes are identical. So no half rhymes are considered.” (Delmonte 2015)

### Robinson, Jason R. 2006. “Colors of poetry: computational deconstruction.”

M.A. Thesis, Georgia State University. <https://getd.libs.uga.edu/pdfs/robinson_jason_r_200605_ma.pdf> 

Rhyme isolates last three syllables of each line and colors matching syllables, apparently after pairwise comparison of all lines. Seems to require exact match of syllables, i.e., some but not all types of approximate rhyme can be recognized.  Color and text-block border visualization of other features, including segment-level sound correspondences, which can also highlight some aspects rhyme. Colors are numerous and dense, i.e., not easy to read.

“Spanish poetry visualization tool [... that ...] analyzes almost all linguistic features of texts such as syllabification, intonation, rhyme, meter, and pauses.
The tool is capable of highlighting parts of semantic interest within the poems.
The main advantage of this poetry visualization is that each line has a more unique
sound average where the tone in the content is continually changed.” (Noh et al. 2019: 174)

### Tanasescu, Chris, Bryan Paget, and Diana Inkpen. “Automatic classification of poetry by meter and rhyme.” 

FLAIRS-2016. <https://docplayer.net/27880336-Automatic-classification-of-poetry-by-meter-and-rhyme.html>

Rhyme classification, in progress, is based on pairwise comparison on sound. Alignment method is not described. 

____

## Visualization, general

### Benner, Drayton C. 2014 “The sounds of the Psalter: computational analysis of soundplay.”

*Literary and linguistic computing*, Vol. 29, No. 3, 361–78.  doi:10.1093/llc/fqu024

Visualizes sounds as colored letters or bars to explore alliteration.

### Chaturvedi, Manish. 2011. “Visualization OF TEI encoded texts. In support close reading.”

M.C.S. thesis, Miama University, OH. <https://etd.ohiolink.edu/!etd.send_file?accession=miami1323623830&disposition=inline>

Myopia tool. Focus on meter, color-coded and text. Nothing about rhyme. 

### Chaturvedi, M., Gannod, G., Mandell, L., Armstrong, H., & Hodgson, E. 2012. “Myopia: a visualization tool in support of close reading.” 

*Digital Humanities 2012.* Abstract at
<http://www.dh2012.uni-hamburg.de/conference/programme/abstracts/myopia-a-visualization-tool-in-support-of-close-reading.1.html>. Video at <https://lecture2go.uni-hamburg.de/l2go/-/get/v/13930> (21 min). Slides at <http://www.helenarmstrong.site/wp-content/uploads/2013/04/visualization_stacked.pdf>. 

### Madnani, N. (2005). “Emily: A tool for visual poetry analysis.” 

Technical Report: University of Maryland (April 2005). <https://www.researchgate.net/publication/228384717_Emily_A_Tool_for_Visual_Poetry_Analysis>

Weighted term search with colored graphic visualization. No discussion of rhyme.

“Emily is an analysis tool for dynamic visualization of poetry, specifically based on searching. Emily provides two different ways of visualization when the poem is selected. The first interface is a document view, which is the default view of Emily. The second interface is a line-based view where each of the poems is represented by a group of lines. The lines are grouped to form a line bar which is proportional to the poem’s length.” (Noh et al. 2019: 174)

### Meneses, Luis and Richard Furuta. “Visualizing poetry: creating tools for critical analysis. *Poetess archive journal* 3.

<https://journals.tdl.org/paj/index.php/paj/article/view/34>

Emphasize retaining original text in visualizations. Term frequency, sentiment, 

### Mittmann, Adiel, Aldo Von Wangenheim, and Alckmar Luiz Dos Santos. 2016. “A multi-level visualization scheme for poetry.”

*Proceedings of the International Conference on Information Visualisation,2016–August,* 312–17. <doi:https://doi.org/10.1109/IV.2016.64>

Letters to sounds, poem as table with meter, collection of poems as abstracted tables with meter, features of entire authorial corpora (e.g., final punctuation). Nothing about rhyme.

### Piez, Wendell. 2010. “Towards hermeneutic markup: An architectural outline.”

Abstract in *Proceedings of the Digital Humanities, 2010*, 1–5, <http://dh2010.cch.kcl.ac.uk/academic-programme/abstracts/papers/pdf/ab-743.pdf>. Supporting paper (slides and examples) at <http://piez.org/wendell/papers/dh2010/index.html>. 

Interactive SVG display of overlapping structural (stanzas, lines, etc.), discourse (speeches), and linguistic (clauses, sentences). 

____

## To check

### Anon. 2018 “Dynamically scoring rhymes wiht phonetic features and sequence alignment.”

<http://axon.cs.byu.edu/Dan/673/papers/bay.pdf> or download link at <https://www.semanticscholar.org/paper/Dynamically-Scoring-Rhymes-with-Phonetic-Features/213eb563257ce26f2463dcf16bbdddff7ddfa339>. No author is indicated (!).

### Hinton, Erik and Joel Eastwood. 2016. “Playing with Pop Culture: Writing an Algorithm To Analyze and Visualize Lyrics From the Musical ‘Hamilton’.”

*Computation + journalism 2016*, Sept. 30–Oct. 1, 2016, not paginated. Download link at <https://www.semanticscholar.org/paper/Playing-with-Pop-Culture-%3A-Writing-an-Algorithm-To-Hinton/8ba81332ebe634f2201eed39cec9206c2118cc38>.

### Hirjee, Hussein and Daniel G. Brown. 2009. “Automatic detection of internal and imperfect rhymes in rap lyrics.”

10th International Society for Music Information Retrieval Conference (ISMIR 2009), 711–16. Download link at <https://www.semanticscholar.org/paper/Automatic-Detection-of-Internal-and-Imperfect-in-Hirjee-Brown/571c8094f19f5b1a19be41bb766ac17bdd684662>.

### Hirjee, Hussein and Daniel G. Brown. 2010. “Using automated rhyme detection to characterize rhyming style in rap music.”

*Empirical musicology review* Vol. 5, No. 4, 2010, 121–45. Download link at <https://www.semanticscholar.org/paper/Using-Automated-Rhyme-Detection-to-Characterize-in-Hirjee-Brown/8b66ea2b1fdc0d7df782545886930ddac0daa1de>.

### McCurdy, Nina, Vivek Srikumar, and Miriah Meyer. 2015. “RhymeDesign: a tool for analyzing sonic devices in poetry.”

Proceedings of NAACL-HLT Fourth Workshop on Computational Linguistics for Literature, Denver: Association for Computational Linguistics, 12–22. <https://www.aclweb.org/anthology/W15-0702>.

### Tizhoosh, Hamid R., Farhang Sahba, and Rozita Dara. 2008. “Poetic features for poem recognition: a comparative study.”

Journal of pattern recognition research (2008) 24-39. Download link at <https://www.researchgate.net/publication/228375375_Poetic_Features_for_Poem_Recognition_A_Comparative_Study>.

### Wattenberg, Martin. 2002. “Arc diagrams: visualizing structure in strings.”

*Proceedings of the IEEE Symposium on Information Visualization 2002 (InfoVis'02), unpaginated. <http://innovis.cpsc.ucalgary.ca/innovis/uploads/Courses/InformationVisualizationDetails2009/Wattenberg2002.pdf>

(Check also visualization links in ASEEES 2019 presentation.)