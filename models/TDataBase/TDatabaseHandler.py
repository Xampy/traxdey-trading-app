###################################################
#
#
#   Database Handler
#
#
###################################################


import sqlite3




class TDataBaseHandler(object):
	"""docstring for TDataBaseHandler"""
	def __init__(self):
		super(TDataBaseHandler, self).__init__()
		

		self.__dataBaseName = "traxdey.db"
		self.__tabLeName = "user_info"


		#Try to open the database
		try:
			db = open(self.__dataBaseName, 'r')
			print("Data base exists")

			self.__connection= sqlite3.connect(self.__dataBaseName)
			self.__cursor = self.__connection.cursor()

		except FileNotFoundError as e:

			#The database does not exist
			#Create the database
			print("File not found")

			#db = open(self.__dataBaseName, 'w')


			self.__connection= sqlite3.connect(self.__dataBaseName)
			self.__cursor = self.__connection.cursor()



			create_request = "CREATE TABLE " + self.__tabLeName + "(id INTEGER NOT NULL, active INTEGER DEFAULT(0) );"
			#Execute the request
			self.__cursor.execute(create_request)


			#Insert data
			insert_request = "INSERT INTO " +self.__tabLeName + " (id, active) VALUES(1, 0);"
			#Execute the request
			self.__cursor.execute(insert_request)


			#Save the data
			self.__connection.commit()



	def changeUserSignedState(self):
		"""
			Change the user signed in state
			by default user is not signed in 
		"""

		select_request = "SELECT * FROM " + self.__tabLeName + ";"#

		#Execute the request
		result = self.__cursor.execute(select_request).fetchall()
		print(result)

		#Result must be only one row
		if len(result) != 1:
			print("\nError on dataBase\n")
		else:

			#Here we can threat the data
			update_request = "";

			#Check the user state
			if result[0][1] == 1:
				update_request ="UPDATE " + self.__tabLeName + " SET active=0 WHERE id=1;"
			elif result[0][1] == 0:
			 	update_request ="UPDATE " + self.__tabLeName + " SET active=1 WHERE id=1;"



			if update_request != "":

				try:
					self.__cursor.execute(update_request)
					self.__connection.commit()

					self.close()
				except Exception as e:

					self.close()
					
					raise e

	def readUserActiveSatae(self):
		"""
			Check if the user is already signed in with account or not
		"""


		select_request = "SELECT * FROM " + self.__tabLeName + ";"#

		#Execute the request
		result = self.__cursor.execute(select_request).fetchall()
		print(result)

		#Result must be only one row
		if len(result) != 1:
			print("\nError on dataBase\n")
			self.close()
			raise Exception("DataBase has been modified...")
		else:
			return result[0][1]

		return None
				

	def close(self):
		self.__cursor.close()
		self.__connection.close()





class TDataBaeManager(object):
	"""docstring for TDataBaeManager"""
	def __init__(self, arg):
		super(TDataBaeManager, self).__init__()
		self.arg = arg
		
			  






t = TDataBaseHandler()
t.changeUserSignedState()
t.close()
		
