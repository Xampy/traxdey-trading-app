###################################################
#
#
#   Tools for authenticating user with firebase
#
#
###################################################



import pyrebase


var firebaseConfig = {
    'apiKey': "AIzaSyBNk03e_zgCTmiShGJenKSqYX69V36AEds",
    'authDomain': "traxdey-app.firebaseapp.com",
    'databaseURL': "https://traxdey-app.firebaseio.com",
    'projectId': "traxdey-app",
    'storageBucket': "traxdey-app.appspot.com",
    'messagingSenderId': "674144929082",
    'appId': "1:674144929082:web:58a50f50f6e93203347c03",
    'measurementId': "G-MFNX7R0RN5"
  };

class TFirebase(object):
	"""docstring for TFirebase"""
	def __init__(self, firebase=None):
		super(TFirebase, self).__init__()
		
		#Here we initilize the firebase application
		assert firebase is not None, "firebase arg muqt be not null"

		self.__firebase = 
		





	@staticmethod
	def signInUser(email, password):
		"""
			This sign in method will be called the first login time 
			and each time when it required to 
			fill account with money
		"""
		
		firebase.auth().sign_in_with_eamil_and_password(email, password)
