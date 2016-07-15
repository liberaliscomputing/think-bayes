# -*- coding: utf-8 -*-

from thinkbayes import Pmf

def dice_prob(num_face):
	#initialize constructor
	pmf = Pmf()

	#create dice
	dice = range(1, num_face + 1)

	#set probability of each face
	for face in dice:
		pmf.Set(face, 1/float(num_face))

	#print probabilities
	for i in dice:
		print 'Probability of face %d of dice: %f' % (i,  pmf.Prob(i))

	return pmf

if __name__ == '__main__':
	num_face = 6
	pmf = dice_prob(num_face)

