##########################################################################
#
#
#  Chart data controller
#
########################################################################



class TChartController(object):
	"""docstring for TChartController"""
	def __init__(self, _models=None):
		super(TChartController, self).__init__()

		#########################################
		#  The controller takes two chart model
		#  the test model and the online model
		self._models = {
							'test':_models[0],
							'online': _models[1]
		}


		self._modelCaller = None



		#########################################
		#
		##################
		self._observers = []
		#
		#
		###############################



	def getModel(self): 

		if self._modelCaller is not None:
			return self._models[self._modelCaller]
		else:
			raise Exception("The model caller name is None : see your observers ")


	def setModelFile(self, filename):
		"""
			It takes as input the file and check if it's valid
		"""

		if filename != None and len(filename) > 0:
			return True
		return False



	def notify(self, msg):

		for obs in self._observers:
			obs.update(msg)

	def addObserver(self, obs):

		if obs not in self._observers:
			self._observers.append(obs)



	def update(self, msg):

		if 'chart' in msg.keys():

			if 'type' in ( msg['chart'] ).keys():

				if msg['chart']['type'] == 'test':
					self._modelCaller = 'test'
				elif msg['chart']['type'] == 'online':
					self._modelCaller = 'online'


				#Notify others for a model set
				self.notify(msg={
									'chart' :{
										'model': 'ok'
									}
					}
				)





