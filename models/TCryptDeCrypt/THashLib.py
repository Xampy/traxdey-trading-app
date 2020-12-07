###########################################################"
#
#
# Polytnome Hash Tools
#
#
#############################################################

from TPolynom import TPolynom





def getAplhabets(string):
	_alphabets = []


	for c in string:
		if c not in _alphabets:
			_alphabets.append(c)

	return _alphabets



def getPolynoms(string, _alphabets):

	result = []
	polynoms = []


	for a in _alphabets:

		t = []
		for c in string:
			if c == a:
				t.append(1)
			else:
				t.append(0)

		result.append(t)


	
	for c, p in enumerate(result):
		polynoms.append( TPolynom( [c] + p ) )


	for p in polynoms:
		#p.show()
		pass


	return polynoms






class THashLib(object):
	"""docstring for THashLib"""
	def __init__(self):
		super(THashLib, self).__init__()
	




	


	@staticmethod
	def thash(string):
		"""
			Hash the given string
		"""

		#Get alphabets
		alphabets = getAplhabets(string)
		polynoms = getPolynoms(string, alphabets)

		t_hash = ""

		h = polynoms[0]
		for p in polynoms[1:]:
			h = TPolynom.multiply(h, p)


		#h.show()
		v = [1] + h.m   #Get the list of monome of the result polynom
		for i in v:
			t_hash += str(i)


		#Removing ending zero
		#########################################
		#
		#   In next version
		#
		#########################################

		#print("Key : ", t_hash)

		return (t_hash, alphabets)


	@staticmethod
	def check_thash(alphabets, string, t_hash):
		"""
			Check if the THash od @string is equal to @t_hash
		"""

		polynoms = getPolynoms(string, alphabets)

		ct_hash = ""

		h = polynoms[0]
		for p in polynoms[1:]:
			h = TPolynom.multiply(h, p)


		#h.show()
		v = [1] + h.m   #Get the list of monome of the result polynom
		for i in v:
			ct_hash += str(i)


		#Removing ending zero
		#########################################
		#
		#   In next version
		#
		#########################################

		print("Calculated Key : ", ct_hash)

		return ct_hash == t_hash




"""
string = "maxime@gmail.com"

h = THashLib.thash(string)
al = h[1]

print("Hashed : ", h)


print("Checking hashed : ", THashLib.check_thash(h[1], string, h[0]))
"""