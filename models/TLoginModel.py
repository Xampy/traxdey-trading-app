##########################################################################
#
#
#  Login Model
#
#     Rhisis to handle more resuest abou logging
#          on server 
#
########################################################################


import math
from .TNetwork.TJsonHandler import TJsonHandler

class TLoginModel(object):
	"""docstring for TLoginModel"""
	def __init__(self, database_manager=None):
		super(TLoginModel, self).__init__()
		

		#By default user is not logged
		self.__alreadyLogged = False
		self.__datataBaseManager = database_manager 

		self.__email = None
		self.__password = None



		#####################################################
		#
		#
		##

		self.__observers = []

		##
		#
		#####################################################


	def setEmail(self, email, password):
		self.__email = email
		self.__password = password


		self.checkUser()

	def checkUser(self):
		"""
			Check the user logging state

			Application will provide an encrypted identifier
			for facilitate the authehtification
		"""

		#Check if wehave already this crypted key
		#This key is also generated on the server side



		url = "http://127.0.0.1:8000/check_user"


		try:



			#We got a data with information
			if self.__email == "root@root.com" and self.__password == "root":
				self.notifyObservers(msg={
											'login' : {
												'success': "OK",
												'content': None
											}
										}
				)
			else:
				self.notifyObservers(msg={
										'login' : {
											'error': "Error : login data are incorrect"
										}
									}
				)



			"""req = TJsonHandler.injectJson(url=url, 
													action="get",
													payload={
														"email": self.__email,
														"key":"ze" 
													} 
					)"""

			#Check if we have a 200 response with required value

			"""if req.status_code == 200:

				try:
					#Convert text into a dict object
					data = dict(eval(req.text))

					#We got a data with information
					if len(data.keys()) > 0 and 'name' in data.keys():
						self.notifyObservers(msg={
													'login' : {
														'success': "OK",
														'content': data
													}
												}
						)
					else:
						self.notifyObservers(msg={
												'login' : {
													'error': "Error while parsing data"
												}
											}
						)

				except Exception as e:
					self.notifyObservers(msg={
											'login' : {
												'error': "Error on server"
											}
										}
					)

			else:
				self.notifyObservers(msg={
											'login' : {
												'error': "Error on server bad response"
											}
										}
				)"""

		except Exception as e:
			self.notifyObservers(msg={
										'login' : {
											'error': "Check your internet connection"
										}
									}
			)



	def addObserver(self, observer):
		self.__observers.append(observer)


	def notifyObservers(self, msg):

		for obs in self.__observers:
			obs.update(msg)
		


l = TLoginModel()
l.checkUser()
