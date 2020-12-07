###########################################################"
#
#
# Polytnome tools
#
#
#############################################################



class TPolynom(object):
	"""docstring for Polynom"""
	def __init__(self, m):
		super(TPolynom, self).__init__()

		assert m is not None and len(m) > 0

		self.m = m
		self.deg = len(m)


	@staticmethod
	def multiply(pA, pB):

		prod = [0] * (pA.deg + pB.deg - 1)

		for i in range(pA.deg):
			for j in range(pB.deg):
				prod[i + j] += pA.m[i] * pB.m[j]


		return TPolynom(prod)

	def show(self):

		s = ""

		for p, e in enumerate(self.m):
			if p == 0:
				if e < 0:
					f = "-{}".format(e)
				else:
					f = "{}".format(e)

			else:
				if e < 0:
					if p == 1:
						f = "-{}x".format(e)
					else:
						f = "-{}x^{}".format(e, p)
				else:
					if p == 1:
						f = "+{}x".format(e)
					else:
						f = "+{}x^{}".format(e, p)

			s += f

		print(s)
"""
m = TPolynom.multiply(TPolynom([1, 1]), TPolynom([1, 1]))
m.show()"""