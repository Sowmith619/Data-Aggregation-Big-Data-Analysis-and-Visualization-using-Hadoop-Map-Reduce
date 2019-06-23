#!/usr/bin/env python
import sys, re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import sys
import re
import nltk
#from nltk.corpus import stopwords

#Top 10 words found in NYTimes Data
top_words = ['one', 'first', 'team', 'three', 'league', 'game', 'monday', 'people', 'season', 'win']	

#The context for the co ocurrance in nytimes data is article. Each article is present in separate file and each file has single line.
for line in sys.stdin:
	no_SpecialCharacters = re.sub('[^a-zA-Z ]','',line).lower()
	stop_words = set(stopwords.words('english'))
	word_tokens = word_tokenize(no_SpecialCharacters)
	filtered_sentence = [w for w in word_tokens if not w in stop_words]
	TokenizedOutput = ' '.join(filtered_sentence)
	    # remove leading and trailing whitespace
	TokenizedOutput = TokenizedOutput.strip()
	    # split the line into words
	words = line.split()
	list_of_words = list()
	for word in words:
		if(word not in stopwords.words('english')):
                	list_of_words.append(word)
	for index, word1 in enumerate(list_of_words):	
		for word2 in list_of_words[(index+1):]:		
			if(word2 == word1): continue
			pair = word1+"|"+word2
			if(word1 in top_words or word2 in top_words):
				print('%s\t%s' % (pair, 1))
	
        
                
	         
	        
            
                        


	
	
	
	
	
