##########################################################################
#
#
#  Chart data model
#
########################################################################


import math

from PyQt5.QtCore import QThreadPool

from .data_science import correlation, getLinearRegressionEquationYeX, mean
from .TTime.TPeriodInterval import TTimePeriodHandler


CHART_PRICES_TYPE = {
						"O":"Open", "C": "Close", 
						"H": "High", "L": "Low", "HL/2": "(Hight, Low)/2"}

"""CHART_DATA_PERIODS = {"P_M1":("min", 1), "P_M5": ("min", 5), "P_M15": ("min", 15),
						"P_M30": ("min", 30), "P_H1": ("hour", 1), "P_H4": ("hour", 4), "P_D1":("day", 1)}"""





CHART_DATA_PERIODS = {
	"P_M1"	:	("min", 1), 
	"P_M5"	: 	("min", 5), 
	"P_M15"	: 	("min", 15),
	"P_M30"	: 	("min", 30), 
	"P_H1"	: 	("hour", 1),
	"P_H4"	: 	("hour", 4), 
	"P_D1"	:	("day", 1)
}





class TAbstractChartModel(object):
	"""docstring for TChartDataModel"""
	def __init__(self):
		super(TAbstractChartModel, self).__init__()


		###############################################################
		#
		##

		self._observers = []

		##
		#
		################################################################

		################################################################
		# To manage thread
		##

		self.threadpool = QThreadPool()

		##
		#
		################################################################
		

		#Plotting configuration 
		#and data setup 
		self._config = {
							'data': {
								'symbol'  : None,
								'period'  : None,
								'price'   : None,
								'predict' : None
							},
							'color': {
								'price'   : 'white',
								'SMA'     : 'blue',
								'P_SMA'   : 'red'
							}
						}

		#FileLines
		#If we are using file
		self._LINES = []

		#Plotting data
		self._GLOBAL_DATA =[]
		self._TEMPORARY_GLOBAL_DATA = []
		self._XAXIS =[]
		self._NORMAL_SMA = []

		self._PREDICTED_SMA = []
		self._LINEAR_REGRESSION_DATA = []
		self._JOINED_LINEAR_REGRESSION_DATA = []
		self._SMOOTHED_LINEAR_REGRESSION_DATA = []


		#For improve the linear regression line
		self._IMPROVED_TOP_SMOOTHED_LINEAR_REGRESSION_DATA = []
		self._IMPROVED_BOTTOM_SMOOTHED_LINEAR_REGRESSION_DATA = []
		self._LAST_IMPROVED_VALUE = 1



		self._LAST_PERIOD_PREDICTED_END = None



	def resetPlotData(self,):
		"""
			Reset plot data
		"""

		#FileLines
		#If we are using file
		self._LINES = []

		#Plotting data
		self._GLOBAL_DATA =[]
		self._TEMPORARY_GLOBAL_DATA = []
		self._XAXIS =[]
		self._NORMAL_SMA = []

		self._PREDICTED_SMA = []
		self._LINEAR_REGRESSION_DATA = []
		self._JOINED_LINEAR_REGRESSION_DATA = []
		self._SMOOTHED_LINEAR_REGRESSION_DATA = []


		#For improve the linear regression line
		self._IMPROVED_TOP_SMOOTHED_LINEAR_REGRESSION_DATA = []
		self._IMPROVED_BOTTOM_SMOOTHED_LINEAR_REGRESSION_DATA = []
		self._LAST_IMPROVED_VALUE = 1



		self._LAST_PERIOD_PREDICTED_END = None






	def setParams(self, params: dict):
		self._config = params


		#Notify the chart view to prventthepricebar to change color
		self.notify(msg={
							'prices' :{
								'colors': {
									'RP': self._config['color']['price'],
									'RS': self._config['color']['SMA'],
									'FS': self._config['color']['P_SMA']
								}
							},

							#Notify the chart info
							'chart':{
								'infos': {
									'ST': "0",
									"ET": "0",
									"BC": self._config['data']['predict']
								}
							}
							
						}
		)

	def handlePeriodResult(self, result):
		"""
			A period endthread calculation has been make 

			then handle the result here
		"""

		#Notify the chart view to prventthepricebar to change color
		self.notify(msg={
							#Notify the chart info
							'chart':{
								'infos': {
									'ST': str(self._LAST_PERIOD_PREDICTED_END),
									"ET": result, #TTime.convertToDateHour(),
									"BC": self._config['data']['predict']
								}
							}
							
						}
		)
		#print("\n"*10, result)

	def getConfig(self):
		return self._config






	def readOneData(self):
		"""
			Read a sigle line of data

			Virtual methodto have been overrwritten
		"""
		pass


	def addGlobalData(self):
		

		PERIOD = int(self._config['data']['predict'])
		HALF_PERIOD = int(PERIOD/2)


		#Read single line data here
		data = self.readOneData()


		for i in range(len(self._NORMAL_SMA), len(self._NORMAL_SMA) + len(data)):
			#We can calculate a SMA
			value = 0

			if (i - PERIOD > 0):
				value = sum(self._GLOBAL_DATA[i - PERIOD + 1: i+1]) /PERIOD
				self._NORMAL_SMA.append( value )
			else:
				value = sum(self._GLOBAL_DATA[0: i+1]) /(i+1)
				self._NORMAL_SMA.append( value )


			self.notify(msg={
								'prices': {
									'values': {
											'RS': str(value/100000)
									} 
									
								} 
							} 
			)




			##########################################################################
		#
		#     Predictaed value of SMA
		#
		#############################################################################


		if(len(self._TEMPORARY_GLOBAL_DATA) % HALF_PERIOD == 0 and len(self._TEMPORARY_GLOBAL_DATA) > 0):
			#print("\n###########Periode atteint.##")

			START = len(self._TEMPORARY_GLOBAL_DATA) - HALF_PERIOD


			################################################
			#   Make time thread calcul here
			##


			


			p = TTimePeriodHandler(
				)

			self.threadpool.start(
				p.run(
					func=self.handlePeriodResult,
					s_date_time=str(self._LAST_PERIOD_PREDICTED_END),
					_period= CHART_DATA_PERIODS[self._config['data']['period']][0],
					_p_type=CHART_DATA_PERIODS[self._config['data']['period']][1],
					_count=int(int(self._config['data']['predict']))/2 )
			)

			##
			#
			################################################			
			#
			################################################

			
			TEMP_PREDICTED_AVERAGE = []

			while START < len(self._TEMPORARY_GLOBAL_DATA):
				
				

				#########################################################
				#
				#  Predicted vlaue
				#
				###############################


				#Calculate regression coefficient here
				coeff = getLinearRegressionEquationYeX(
					[i for i in range(HALF_PERIOD)], self._GLOBAL_DATA[START: START + HALF_PERIOD])

				#print("\n\nGet regression coeff : ", coeff)
				for i in range(HALF_PERIOD):
					value = i * coeff[0] + coeff[1]
					self._LINEAR_REGRESSION_DATA.append(value)



					self.notify(msg={
										'prices': {
											'values': {
												'FS': str(value/100000)
											}
										} 
									} 
					)



				#Joinning the first and the last value to have a line
				if len(self._LINEAR_REGRESSION_DATA) > HALF_PERIOD:
					u, v = 0, self._LINEAR_REGRESSION_DATA[START-1] #coeff[1]
					u_, v_ = HALF_PERIOD - 1, self._LINEAR_REGRESSION_DATA[-1] # (HALF_PERIOD - 1) * coeff[0] + coeff[1]

					a = (v_ - v)/(u_ - u)


					for i in range(0, HALF_PERIOD):
						value = i * a + v

						self._JOINED_LINEAR_REGRESSION_DATA.append(value)

						j = len(self._JOINED_LINEAR_REGRESSION_DATA) - 1

						if len(self._JOINED_LINEAR_REGRESSION_DATA) > HALF_PERIOD:

							value_2 = sum(self._JOINED_LINEAR_REGRESSION_DATA[j - HALF_PERIOD + 1: j+1]) /HALF_PERIOD
							self._SMOOTHED_LINEAR_REGRESSION_DATA.append(value_2)
						else:
							value_2 = sum(self._JOINED_LINEAR_REGRESSION_DATA[0: j+1]) /(j+1)
							self._SMOOTHED_LINEAR_REGRESSION_DATA.append(value_2)






					#Here we calculate the correalation value and update it
					if len(self._SMOOTHED_LINEAR_REGRESSION_DATA) > HALF_PERIOD :

						#Get the latest hal value of the smoothed data
						#and the corresponding normal average data
						l = len(self._SMOOTHED_LINEAR_REGRESSION_DATA)
						n = len(self._NORMAL_SMA)

						r =correlation(
											self._SMOOTHED_LINEAR_REGRESSION_DATA[l - 2*HALF_PERIOD + 1: l - HALF_PERIOD],
											self._NORMAL_SMA[n-HALF_PERIOD + 1:] )


						self.notify(msg={
											#Notify the chart info
											'chart':{
												'infos': {
													'AC': "{:.2f}%".format(abs(r *100)) 
												}
											}
							
										}
						)





				


				#########################################
				#
				# Better Smoothing the predicted values
				#
				#############################################################
				"""for j in range(START,  START + HALF_PERIOD):
					if j > HALF_PERIOD:
						value_ = sum(PREDICTED_SMA_AVERAGE[j - HALF_PERIOD + 1: j+1]) /HALF_PERIOD 
						#value = sum(data[START: j+1]) /(j - START + 1)
						SMOOTHED_PREDICTED_SMA_AVERAGE.append(value_)

						value_2 = sum(self._LINEAR_REGRESSION_DATA[j - HALF_PERIOD + 1: j+1]) /HALF_PERIOD
						self._SMOOTHED_LINEAR_REGRESSION_DATA.append(value_2)
					else:
						value_ = sum(PREDICTED_SMA_AVERAGE[0: j+1]) /(j+1)
						SMOOTHED_PREDICTED_SMA_AVERAGE.append(value_)


						value_2 = sum(self._LINEAR_REGRESSION_DATA[0: j+1]) /(j+1)
						self._SMOOTHED_LINEAR_REGRESSION_DATA.append(value_2)"""








				####################################################
				#
				# Improved 
				#
				##################

				"""if len(self._SMOOTHED_LINEAR_REGRESSION_DATA) > HALF_PERIOD :

					self._LAST_IMPROVED_VALUE =  mean(
						[
							(x-y) for x, y in zip(
														self._SMOOTHED_LINEAR_REGRESSION_DATA[
																START - HALF_PERIOD: START],
														self._NORMAL_SMA[START: START + HALF_PERIOD]
														)
						]
						
					)


					#########################################
					#
					# Better Smoothing with improved value the predicted values
					#
					#############################################################
					for j in range(START,  START + HALF_PERIOD):
						value = self._SMOOTHED_LINEAR_REGRESSION_DATA[j]

						self._IMPROVED_TOP_SMOOTHED_LINEAR_REGRESSION_DATA.append(
							(self._LAST_IMPROVED_VALUE) + value 
						)

						self._IMPROVED_BOTTOM_SMOOTHED_LINEAR_REGRESSION_DATA.append(
							( self._LAST_IMPROVED_VALUE) - value
						)"""


				########################
				#
				#
				########################################################










				START += HALF_PERIOD



	def getGlobalData(self):
		return self._GLOBAL_DATA
	def getNormalSMA(self):
		return self._NORMAL_SMA
	def getPredictedSMA(self):
		return self._LINEAR_REGRESSION_DATA
	def getPredictedJoinSMA(self):
		return self._JOINED_LINEAR_REGRESSION_DATA
	def getSmoothedPredictedSMA(self):
		return self._SMOOTHED_LINEAR_REGRESSION_DATA
	def getImprovedTopSmoothedPredictedSMA(self):
		return self._IMPROVED_TOP_SMOOTHED_LINEAR_REGRESSION_DATA
	def getImprovedBottomSmoothedPredictedSMA(self):
		return self._IMPROVED_BOTTOM_SMOOTHED_LINEAR_REGRESSION_DATA
	def getXAxisData(self):
		return self._XAXIS





	#############################################################
	# Period caluculator
	###



	def addObserver(self, obs):
		if obs not in self._observers:
			self._observers.append(obs)


	def notify(self, msg):

		for observer in self._observers:
			observer.update(msg)









