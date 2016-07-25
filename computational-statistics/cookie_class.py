#!/usr/bin/python
# -*- coding: utf-8 -*-

from thinkbayes import Pmf

class Cookie(Pmf):
	
	def __init__(self, bowls):
		Pmf.__init__(self)
		self.bowls = bowls
		for hypo in bowls.keys():
			self.Set(hypo, 1)
		self.Normalize()

	def Update(self, prior):
		for hypo in self.Values():
			likelihood = self.Likelihood(prior, hypo)
			self.Mult(hypo, likelihood)
		self.Normalize()	

	def Likelihood(self, prior, hypo):
		bowl = self.bowls[hypo]
		likelihood = bowl[prior]
		return likelihood		

if __name__ == '__main__':
	#define data
	bowls = {
			'bowl_1': {
				'vanilla': 0.75,
				'chocolate': 0.25
			},
			'bowl_2': {
				'vanilla': 0.5,
				'chocolate': 0.5
			}
		}

	#initialize constructor
	pmf = Cookie(bowls)

	#set likelihood of each hypothesis
	#prior = 'vanilla'
	priors = ['vanilla', 'chocolate', 'vanilla']
	for prior in priors:
		pmf.Update(prior)

	for hypo, prob in pmf.Items():
		print 'Probability of %s given %s cookie: %f' % (hypo, prior, prob)

