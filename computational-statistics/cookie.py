# -*- coding: utf-8 -*-

from thinkbayes import Pmf

bowls = {
	'bowl_1': {
		'prior': 0.5, 
		'likelihood': 0.75
	},
	'bowl_2': {
		'prior': 0.5, 
		'likelihood': 0.5
	}
}

#initialize constructor
pmf = Pmf()

#set prior and likelihood of each hypothesis
for bowl, probs in bowls.items():
	pmf.Set(bowl, probs['prior'])
	pmf.Mult(bowl, probs['likelihood'])

#divide by normalizing constant
pmf.Normalize()

for bowl in bowls:
	print 'Probability of %s given vanilla cookie: %f' % (bowl, pmf.Prob(bowl))

