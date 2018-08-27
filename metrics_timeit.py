#!/usr/bin/env python3
"""Speed testing functions for gathering lyric's metrics."""

from timeit import timeit
import metrics

ITERS=100000

#remove punctuation from word
rmv_punc = timeit("metrics.remove_punctuation('can!')", number=ITERS, globals=globals())
print("remove punctuation; 'can!' ::", rmv_punc)

#remove whitespace from two words
rmv_wsp = timeit("metrics.remove_whitespace_from_word('can do')", number=ITERS, globals=globals())
print("remove whitespace; 'can do' ::", rmv_wsp)



