# -*- coding: utf-8 -*-

from thinkbayes import Pmf
import string
from stopwords import stopwords

#initialze constructor
pmf = Pmf()

#generate word list from text
fname = 'data/aristotle.txt'
words = []
stopwords = stopwords('data/stopwords.txt')
with open(fname) as f:
	for line in f:
		processed = line.strip().translate(None, string.punctuation).split()
		for word in processed:
			if word.lower() in stopwords:
				continue
			words.append(word.lower())

#generate unique word set
u_words = set(words)

#count words
for word in words:
	pmf.Incr(word, 1)

#normalize word freqeuncies as probabilities
pmf.Normalize()

#print probabilities
for u_word in u_words:
	print 'Probability of the word \'%s\': %f' % (u_word,  pmf.Prob(u_word))

