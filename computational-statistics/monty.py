class Monty(Pmf):

	def __init__(self, hypos):
		Pmf.__init__(self)
		for hypo in hypos:
			self.Set(hypo, 1)
		self.Normalize()
