#!/usr/bin/env python
import sys
#import os
sys.path.append('./')

from sklearn.feature_extraction.stop_words import ENGLISH_STOP_WORDS
ENGLISH_STOP_WORDS =  set(ENGLISH_STOP_WORDS ) # BECAUSE IT IS A FROZENSET WHEN IMPORTED


import subprocess
cat = subprocess.Popen(["hadoop", "fs", "-cat", "/shakespeare/NLTK/english"], stdout=subprocess.PIPE)
for line in cat.stdout:
    ENGLISH_STOP_WORDS.add(line)

#os.chdir('/shakespeare/spacy/')
from stop_words import STOP_WORDS # python file that was git cloned
# SPACY set of stop words is called STOP_WORDS


ENGLISH_STOP_WORDS = ENGLISH_STOP_WORDS.union( STOP_WORDS  )

#318 sklearn
#179 nltk
#378 sklearn + nltk

#326 spacy stop words

#409 sklearn + nltk + spacy


# get all lines from stdin
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # split the line into words; splits on any whitespace
    words = line.split()

    # output tuples (word, 1) in tab-delimited format
    for word in words:
	if word not in ENGLISH_STOP_WORDS:
        	print '%s\t%s' % (word, "1")
