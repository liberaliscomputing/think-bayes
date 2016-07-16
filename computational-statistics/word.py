# -*- coding: utf-8 -*-

from thinkbayes import Pmf
import string

#initialze constructor
pmf = Pmf()

#generate word list from text
fname = 'data/aristotle.txt'
words = []
with open(fname) as f:
	for line in f:
		for word in line.strip().split():
			word = word.translate(None, string.punctuation).lower()
			words.append(word)
u_words = set(words)

#count words
for word in words:
	pmf.Incr(word, 1)

#normalize word freqeuncies as probabilities
pmf.Normalize()

#print probabilities
for u_word in u_words:
	print 'Probability of the word %s: %f' % (u_word,  pmf.Prob(u_word))

