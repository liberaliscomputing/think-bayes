# -*- coding: utf-8 -*-

from thinkbayes import Pmf

class Cookie(Pmf):

	def __init__(self, hypos):
		Pmf.__init__(self)
		for hypo in phypos:
			self.Set(hypo, 1)
		self.Normalize()

#initialize constructor
pmf = Pmf()

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

#set prior and likelihood of each hypothesis
for bowl, probs in bowls.items():
	pmf.Set(bowl, probs['prior'])
	pmf.Mult(bowl, probs['likelihood'])

#divide by normalizing constant
pmf.Normalize()

for bowl in bowls:
	print 'Probability of %s given cookie: %f' % (bowl, pmf.Prob(bowl))

