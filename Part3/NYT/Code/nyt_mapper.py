#!/usr/bin/env python
import sys, re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# input comes from STDIN (standard input)
for line in sys.stdin:
    no_SpecialCharacters = re.sub('[^a-zA-Z ]','',line).lower()
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(no_SpecialCharacters)
    filtered_sentence = [w for w in word_tokens if not w in stop_words]
    TokenizedOutput = ' '.join(filtered_sentence)
    # remove leading and trailing whitespace
    TokenizedOutput = TokenizedOutput.strip()
    # split the line into words
    words = TokenizedOutput.split()
    # increase counters
    for word in words:
    
    # write the results to STDOUT (standard output);
    # what we output here will be the input for the
    # tab-delimited; the trivial word count is 1
        print('%s\t%s' % (word, 1))
