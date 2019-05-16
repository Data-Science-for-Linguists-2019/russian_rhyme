# Degrees of rhyme

These examples of types of rhyme patterns, listed roughly from more to less exact, is taken from David J. Birnbaum and Elise Thorsen’s “Exploring inexact rhyme in Russian verse”, presented at *Plotting poetry: bringing deep learning to computational poetry analysis*, Free University of Berlin, 2018-09-12. (Despite the name of the conference, our presentation did not engage with deep learning.)

Russian words are represented as transliteration of Russian orthography (that is, not phonetic transcription) according to the “scholarly” system of transliteration that is standard practice within Slavic linguistics (see the Russian column at <https://en.wikipedia.org/wiki/Scientific_transliteration_of_Cyrillic#Table>). Stress in the examples below is marked by bolding. I use this method of representation instead of IPA because it is the norm in Russian verse studies, and scholars of Russian verse are the principal target audience for this research. However, I also use IPA representations below where those elucidate details that would not be clear otherwise.

Our reference to _rhyme_ below refers to line-end rhyme. We do not discuss line-internal or other types of assonance.

## Paired words end with same sounds

**Note:** The zone of Russian rhyme, like that of English rhyme, is in most cases all sounds from the final stressed vowel to the end of the line. But one difference between Russian and English is that Russian open (= no consonant after the final vowel) masculine (= stress on the final vowel) rhyme requires a *supporting consonant*, that is, the consonants before the final stressed vowels of the rhyming lines must match. For that reason, _see_ and _tree_ rhyme in English, but not in Russian. 

In the example above, however, the supporting consonant sounds are not the same; the first word has a palatalized lateral before the final stressed vowel and the second a palatal glide. This neutralization (for rhyme purposes) is common, and perhaps even uniquitous, in poetry of the Golden Age (roughly the first third of the nineteenth century, exemplified most prominently by A. S. Puškin [1799–1837] and M. Ju. Lermontov [1814–41]). Specifically, any palatal or palatalized consonant is permitted to match the palatal glide [j] (however, two palatalized consonants do not match each other; the neutralization obtains only when one line contains the palatal glide).

**Notes:**

1. The first pair is a perfect rhyme because closed (with a consonant after the final stressed vowel) masculine rhyme does not require a supporting consonant. Nonetheless the perfect phonetic identity except for the dental stop in the second item presents the pre-tonic consonants as part of an *enriched* rhyme (Russian verse scholarship refers to phonetic correspondences that are not required by the rhyme, that is, those before the last stressed syllable, as *enrichment*). 
2. The syllabicity of the two words in the second example is different.


**Note:** A masculine rhyme cannot strictly obtain between an open syllable (second item) and one with the same stressed vowel but a post-tonic coda (there are some exceptions to this, but they don’t obtain here). Nonetheless, the tremendous phonetic similarly between these two words creates a rhyme that is difficult to describe with rules about individual segments, features, and positions.

Notes:

1. _sk**o**lʹko_ is normally IPA [ˈskolʲkə], but it has an informal variant, found in the Moscow dialect and elsewhere, of [ˈskokə]. This matters because the informal pronunciation is a) closer to the rhyming word, which lacks the palatalized lateral, and b) more challenging to recognize algorithmically because it is lexically restricted.
2. Standard practice in Russian metrical studies (Gasparov, Skulačeva), including computational metrical studies, is to recognize some categories of words (by part of speech) as always ictal (that is, as having relative metrical prominence on their linguistically stressed syllables), others as never ictal (that generalization is overly broad, but the details are not important in this immediate context), and others are having their ictus conditioned by meter and rhyme scheme. Specifically, words in this third category, which include pronouns (which is what _**i**m_ is), receive ictus when the meter or rhyme leads us to expect it, but not when it doesn’t. Here the rhyme with _koka**i**n_, which has stress and ictus on its final syllable, tells us that _**i**m_ is ictal. This may be challenging for our purposes because of the circularity: ictus is one way we identify rhyme, but here the expectation of rhyme is one of the factors that leads us to conclude that _**i**m_, which is ictal in some contexts and not in others, receives ictus here.

**Note:** The strongest, most consistent feature of Russian rhyme is phonetic identity between the final stressed syllables of the rhyming lines, which does not obtain here. These words nonetheless function as rhyming, and have considerable phonetic similarity not involving the final stressed vowel.