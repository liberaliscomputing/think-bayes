# -*- coding: utf-8 -*-

from thinkbayes import Pmf

#initialze constructor
pmf = Pmf()

#generate word list from text
fname = ''
word_list = []

#count words
for word in word_list:
	pmf.Incr(word, 1)

#normalize word freqeuncies as probabilities
pmf.Normalize()

