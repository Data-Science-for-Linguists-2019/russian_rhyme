# Matching clusters

## Different cluster length

Post-tonic onset and coda clusters with different segment lengths may participate in approximate rhyme, e.g.:

Word | Tonic | Post-tonic 1 | Post-tonic 2
---|---|---|---
**вы́вести** | vI | Vi | STi
**вы́грести** | vI | gRi | STi

In the preceding example, the onsets of the first post-tonic syllable differ in segment count, and it is unclear how to decide whether the *[V]* in the first word should be aligned for comparison with the *[g]* or with the *[R]* in the second. Thoughts:

1. Finding the closest match doesn’t scale because it requires exponential pair-wise comparison.
2. Duplicating and including columns from both the beginning and the end of the cluster (e.g., *O0* and *O1* are the first and second onset consonants from the left and *O-1* and *O-2* are the last and penultimate) is possible. In this case there are four columns:

Word | O0 | O1 | O-1 | O-2
---|---|---|---|---
**вы́вести** | V |  | V | 
**вы́грести** | g | R | R | g

This would double-count homosyllabic matches. On the one hand, those should be weighted more heavily. On the other hand, the fact that matches like *[g]* ~ *[gR]* include both one match and one non-match already weights the pair less heavily than a perfect homosyllabic match.

## Different syllabicity

### Same syllable count with different syllabification

Rhyming words with the same number of syllables may place corresponding consonants in different syllables, e.g., **вы́бора** *[vI-ba-ra]* ~ **вы́борка** *[vI-bar-ka]*. These are heterosyllabic not because they have a different number of syllables (they don’t), but because they have divergent syllabification of some of the same segmental material.

Dividing the strings into vowels and consonant clusters without regard to syllabification and then counting from both the beginning and the end, as described above, might address this case. An interim alignment table, at the level of V and C-clusters, would read:

Word | 1 | 2 | 3 | 4 | 5 | 6
---|---|---|---|---|---|---
**вы́бора** | v | I | b | a | r | a
**вы́борка** |v | I | b | a | rk |a

The segment-level alignment table for the single consonants would be doubled, counting *O* and *O-1*. The one for position 5 would have four values:

Word | 5O0 | 5O1 | 5O-1 | 5O-2
---|---|---|---|---
**вы́бора** | r | | | r | 
**вы́борка** | r | k | k | r 

See also immediately below.

### Consonant clusters with different order

A modification of one-hot encoding would allow more than one hot value, so that, for example, a **br** cluster would have a `1` value for `b` and a `1` value for `r`. This captures the fact that such a column is partial similar to pure `b` and pure `r` values, although it loses information about relative order, which could be meaningful (e.g., **совра́ть** and **сорва́ть**). See <https://datascience.stackexchange.com/questions/14847/multiple-categorical-values-for-a-single-feature-how-to-convert-them-to-binary-u> for sample code.

This would address the **вы́бора** ~ **вы́борка** example, above.

### Different syllable count

Possibly in combination with the preceding, rhyming words may have a different number of post-tonic syllables, e.g., **мо́рда** *[mOr-da]* ~ **го́рода** *[gO-ra-da]*. 

This type of case raises a challenge to syllable alignment, and not just segment alignment. Specifically, the last syllables of **мо́рда** *[mOr-da]* ~ **го́рода** *[gO-ra-da]* match perfectly, but in the first case the syllable in question is the first post-tonic and in the second case it’s the second post-tonic. The method above, which divides the strings into sequences of V and C-clusters, would fail to associate the two instances of *[da]* because the *[d]* would be part of the second (two-segment) C-cluster in **мо́рда** *[mOr-da]* and the third (one-segment) one in **го́рода** *[gO-ra-da]*.

## Challenges

Aligning segments on the basis of similarity independently of syllable structure is computationally hard (does not scale) because it requires exponential pair-wise comparisons. With that said, such a method might align the perfect matches and then distribute the others either arbitrarily or with recourse to near matching. Thus:

Word | 1 | 2 | 3 | 4 | 5 | 6 | 7 
---|---|---|---|---|---|---|---
**вы́-бо-ра** | v | I | b | a | r | | a
**вы́-бор-ка** | v | I | b | a | r | k | a 

Word | 1 | 2 | 3 | 4 | 5 | 6
---|---|---|---|---|---|---
**мо́р-да** | m | O | r | | d | a
**го́-ро-да** | g | O | r | o | d | a

This might be used for *evaluation* after rhyme pairs (or sets) have been identified, where the number of comparisons is manageably smaller than during the *identification* of those pairs and sets.

This problem is different from witness collation in text criticism because text criticism proceeds from an assumption that all texts represent the same work, and that there is therefore much more similarity than divergence. Rhyme analysis, on the other hand, assumes that the inventory of lines can be divided into mutually exclusive (non-overlapping) rhyme sets. Witness alignment should end in a single cluster that combines all witnesses; rhyme clustering (or classification?) shouldn’t.
