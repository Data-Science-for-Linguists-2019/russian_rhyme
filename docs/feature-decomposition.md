# Clustering by phonetic distinctive features

2019-06-28, Prague

## Description

### Data

* *sorvat′*
* *sovrat′*
* *orat′*

In Real Life, we model only the *rhyme zone*, which we define as the last stressed vowel in the line (`t1`) and all postonic segments (`t2`–`tn`, where even numbers are consonant clusters \[0 or more consonants\] and odd numbers are vowels). In the case of open masculine rhyme, we include also the first pretonic consonant (`t0`). In this example, we pretend that stress falls on the first vowel in order to create an example with constrastive post-tonic consonant clusters.

### Tokenize

Tokenize into V and C(C) sequences:

* *s-o-rv-a-t′*
* *s-o-vr-a-t′*
* *o-r-a-t′*

word | t0 | t1 | t2 | t3 | t4 
---|---|---|---|---|---
sOrvaT| s | O | rv | a | T 
sOvraT | s | O | vr | a | T 
OraT | - | O | r | a | T

## One-hot encode the vowels

`t1` (the tonic vowel) is replaced by five columns: **t1_A**, **t1_E**, **t1_I**, **t1_O**, **t1_U** (one of which is omitted by the function as a dummy; here we arbitrarily choose **t1_U**). Other (unstressed) vowels are replaced by three columns, e.g., **t3_a**, **t3_i**, **t3_u** (here we arbitrarily throw away **t3_u**). For this example we ignore **t0**, which is relevant only for open masculine rhyme.

word|t1_A | t1_E | t1_I | t1_O |t2 | t3_a | t3_i | t4
---|---|---|---|---|---|---|---|---
sOrvaT | 0 | 0 | 0 | 1 | rv | 1 | 0 | T
sOvraT | 0 | 0 | 0 | 1 | vr | 1 | 0 | T
OraT | 0 | 0 | 0 | 1 | r | 1 | 0 | T

In the following discussion (but not in practice) we simplify the vowel representations to make it easier to see the treatment of consonants, which is the focus of the method. Here we keep only a single vowel column for each of the two vowels.

word| t1_O | t2 | t3_a | t4
---|---|---|---|---
sOrvaT | 1 | rv | 1 | T
sOvraT | 1 | vr | 1 | T
OraT | 1 | r | 1 | T

## Multi-hot encode the consonants

We create columns for each possible consonant and count the number of times the consonant appears in that position, whether alone or as part of cluster of two or more consonants. We lose information about the order of consonants in a cluster, e.g., /rv/ and /vr/ have the same representation). Because the values are ordinal (the number of times the consonant appears in the cluster, and not just a binary representation of whether it appears), we retain information about repetition. For example, /sts/ has a `2` value for the **s** feature and /st/ and /ts/ both have a `1` value.

**(TODO: Can we retain information about order?)**

In this exposition (but not in practice), we simplify the representation of the consonants by omitting most of the columns. 

word| t1_O | t2_r | t2_v | t3_a | t4_T
---|---|---|---|---|---
sOrvaT | 1 | 1 | 1 | 1 | 1 | 1
sOvraT | 1 | 1 | 1 | 1 | 1 | 1
OraT | 1 | 1 | 0 | 1 | 1 | 1

Finally, for clarity in this description (but not in practice) we retain only the columns pertaining to **t2**.

word | t2_r | t2_v
---|---|---
sOrvaT | 1 | 1
sOvraT | 1 | 1
OraT | 1 | 0

## Decompose segment-by-position columns (e.g., **t2_r**) into binary phonetic distinctive features

The features are:

Segment | Syllabic | Consonantal | Sonorant | Anterior | Coronal | Palatalized | Nasal | Voiced | Continuant | Lateral | Delayed release
---|---|---|---|---|---|---|---|---|---|---|---
r | 0 | 1 | 1 | 1| 1 | 0 | 0 | 1 | 1 | 0 | 0
v | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0

Create columns for combinations of position and distinctive feature, where the value is the mean representation of the feature in question in all consonants in the cluster. Consonants that repeat in a cluster would be counted individually, so that, for example /sts/ would have a value of `0.67` for **continuant**.

word | t2_syllabic | t2_consonantal | t2_sonorant | t2_anterior | t2_coronal | t2_palatalized | t2_nasal | t2_voiced | t2_continuant | t2_lateral | t2_delayed
---|---|---|---|---|---|---|---|---|---|---|---
sOrvaT | 0 | 1 | 0.5 | 1 | 0.5 | 0| 0| 1 | 1| 0| 0
sOvraT | 0 | 1 | 0.5 | 1 | 0.5 | 0| 0| 1 | 1| 0| 0
OraT | 0 | 1 | 1 | 1| 1 | 0 | 0 | 1 | 1 | 0 | 0

## Discussion

Above we identify three ways to represent information about consonant clusters:

1. Tokenization (V ~ C(C)) and treatment of the consonant tokens as indivisible (that is, regarding /rv/ and /r/ each as a separate one-hot feature) fails to capture the fact that /rv/ and /r/ have something in common phonetically, that is, that both contain /r/.
1. Decomposing consonant clusters into segments and multi-hot encoding on those segments improves on the preceding by capturing the fact that /rv/ and /r/ share a segment, that is, a feature that can be used for clustering. But it fails to capture the fact that the phonetic distance between segments, defined in terms of shared distinctive features, is variable. For example, the two segments in /rv/ agree on being **+continuant**, while those in /rb/ disagree on that feature, and therefore are more distant phonetically than the segments in /rv/. Encoding each segment as a feature means that /rv/ and /rb/ would both be represented as equally distant. (**Note:** Although perhaps they should be!)
1. Distinctive feature decomposition improves on the preceding because it does not regard all segments as equally distant from all other segments. Instead, the distance is a function of the number of distinctive feature values the segments share. For example, the value for the **continuant** feature for /rv/ is `1`, since /r/ and /v/ are both **+continuant**, while the value for /rb/ is `0.5` because /r/ is **+continuant** and /b/ is **-continuant**.

## Possible complications

1. The preceding approach weights all features equally. Are some features, though, more significant for identifying rhyme than others?
1. The preceding approach treats all features as independent of one another, but some are contingent. For example, **+lateral** predetermines *all* other features except palatalization. Can we reduce overweighting due to redundancy by applying dimensionality reduction?
1. We continue to lose, as with all methods discussed here, information about the *order* of consonants.

## /j/ and palatalized consonants

One common relaxation in the phonetic exactness of classicial Golden Age Russian verse is that /j/ may rhyme with any palatalized consonant, but otherwise palatalized consonsants do not automatically rhyme with one another. Thus, for example, **i ja** rhymes with **menja** (/j/ ~ /n′/), but /n′/ does not rhyme as easily with /l′/. In other words, rhyme in this situation is not transitive, so that given the premises that 1) /l′/ rhymes with /j/ and 2) /n′/ rhymes with /j/, it does not follow that /l′/ rhymes with /n′/. Rhyme involving /j/ does not observe triangular equality.

Clustering methods assume that items to be clustered (rows) have features (columns), which may be considered dimensions in an n-dimensional space, and the values in the dataframe cells indicate the position of each item along a specific dimension. The available clustering methods operate on those positions independently of the positons of other items.

Below are possible ways of addressing this details. These are explored further in [Palatalization, /j/, and rhyme](../dev/decompose_palatalization.ipynb).

### Palatalization decomposition

Contrary to traditional phonetic and phonemic practice, we can decompose palatalized consonants by breaking out the palatalization as if it were a separate /j/ consonant, that is, by representing /l′/ as if it were /lj/. Because we represent the features of consonant clusters by averaging the feature values of the constituent individual components, this decomposition averages the actual features of the consonant in question with those of /j/, effectively moving it closer to /j/, although at the expense of moving it further from its unpalatalized counterpart.

Here are the differences:

word | syllabic | consonantal | sonorant | anterior | coronal | palatalized | nasal | voiced | continuant | lateral | delayed
---|---|---|---|---|---|---|---|---|---|---|---
/ j / | 0 | 0 | 1	| 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0
/ l / | 0 | 1 | 1 | 1 | 1 | 0 | 0 | 1 |1 | 1 | 0
/ l′ / | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 1 |1 | 1 | 0
/ lj / | 0 | 0.5 | 1 | 0.5 | 1 | 0.5 | 0| 1 | 1| 0.5| 0
/ n / | 0 | 1 | 1 | 1 | 1 | 0 | 1| 1 |0 | 0 | 0
/ n′ / | 0 | 1 | 1 | 1 | 1 | 1 | 1| 1 |0 | 0 | 0
/ nj / | 0 | 0.5 | 1 | 0.5 | 1 | 0.5 | 0.5| 1 |0.5 | 0 | 0

The resulting hierarchy is: ((lj, nj), j), (n, l). This correctly draws the surrogates for the palatalized consonants closer to /j/, while incorrectly drawing them closer to each other. It is correct that palatalized consonants rhyme more readily with (are closer to, in the rhyme vector space) /j/ than with their non-palatalized counterparts.

### “Rhymes with X” features

Instead of blending /j/ feature values with those of palatalized consonants to increase their proximty to /j/ in the vector space, we can add *rhymes with X* features for all segments, where X is all palatalized consonants. Each segment rhymes only with itself except that /j/ rhymes with all palatalized consonants. This avoids the triangular equality issue because, for example, /j/ would be close to /l′/ by sharing a `1` value on the “rhymes with /l′/” vector, and close to /n′/ by sharing a value on the “rhymes with /n′/” axis, but /l′/ and /n′/ would not share any additional features.

