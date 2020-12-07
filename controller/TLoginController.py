##########################################################################
#
#
#  Chart data controller
#
########################################################################




class TLoginController(object):
	"""docstring for TLoginController"""
	def __init__(self, _model=None):
		super(TLoginController, self).__init__()
		self._model = _model


	def getModel(self): return self._model


	def validateEmail(self, email, password):
		"""
			Check if the email is only aphanumeric

			if set the model email and password
		"""


		if ("@" in email) and ( "." in email ) : 

			if len(email.split('.')[1]) > 1:
				self._model.setEmail(email, password)
				#print("\nValidator is OKKKK\n")
				return True
			else:
				return False

		return False





