# -*- coding: utf-8 -*-

from thinkbayes import Pmf

def dice_prob(number_of_face):
	#initialize constructor
	pmf = Pmf()

	#create dice
	dice = range(1, number_of_face + 1)

	#set probability of each face
	for face in dice:
		pmf.Set(face, 1/float(number_of_face))

	#print probabilities
	for i in dice:
		print 'Probability of face %d of dice: %f' % (i,  pmf.Prob(i))

	return pmf

if __name__ == '__main__':
	pmf = dice_prob(6)

