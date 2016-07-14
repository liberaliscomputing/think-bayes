# -*- coding: utf-8 -*-

from thinkbayes import Pmf

#initialize constructor
pmf = Pmf()

#create dice
dice = range(1, 7)

#set probability of each face
for face in dice:
	pmf.Set(face, 1/6.0)

print pmf

