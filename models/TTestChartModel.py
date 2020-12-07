##########################################################################
#
#
#  Test Chart data model
#
########################################################################




import math

from PyQt5.QtCore import QThreadPool

from .data_science import correlation, getLinearRegressionEquationYeX, mean
from .TTime.TPeriodInterval import TTimePeriodHandler
from .TAbstractChartModel import TAbstractChartModel


CHART_PRICES_TYPE = {
						"O":"Open", "C": "Close", 
						"H": "High", "L": "Low", "HL/2": "(Hight, Low)/2"}

CHART_DATA_PERIODS = {"P_M1":("min", 1), "P_M5": ("min", 5), "P_M15": ("min", 15),
						"P_M30": ("min", 30), "P_H1": ("hour", 1), "P_H4": ("hour", 4), "P_D1":("day", 1)}

class TTestChartModel(TAbstractChartModel):
	"""docstring for TChartDataModel"""
	def __init__(self):
		super(TTestChartModel, self).__init__()


	
	def readOneData(self):
		"""
			Read a sigle line of data
		"""

		PERIOD = int(self._config['data']['predict'])
		HALF_PERIOD = int(PERIOD/2)

		data = []
		for line in self._LINES[len(self._GLOBAL_DATA):len(self._GLOBAL_DATA) + 1]:
				datas = line.split(',')

				#Time Got
				self._LAST_PERIOD_PREDICTED_END = datas[0]

				#time open high low close tick_volume spread real_
				#Switch the price type calucation

				w_p = self._config['data']['price']
				v = 0

				if(w_p == CHART_PRICES_TYPE['O']):
					v = float(datas[1]) 

				elif(w_p == CHART_PRICES_TYPE['C']):
					
					v = float(datas[4]) 

				elif(w_p == CHART_PRICES_TYPE['H']):
					
					v = float(datas[2])

				elif(w_p == CHART_PRICES_TYPE['L']):

					v = float(datas[3]) 

				elif(w_p == CHART_PRICES_TYPE['HL/2']):
					v = ( float(datas[2]) + float(datas[3]) ) /2
				
				self.notify(msg={
									'prices': {
										'values': {
											'RP': str(v)
										}
									} 
								} 
				)

				data.append(100000 * v ) 

				self._TEMPORARY_GLOBAL_DATA.append(data[-1])

				self._GLOBAL_DATA.append(data[-1])

		return data	



	def readData(self, filename=None):
		"""
			Read the entire data from the entire file

			the formatted form is resuired

			time | open | close | hight | low |  etc...
		"""

		#Renit the lines
		self._LINES.clear()

		with open(filename, 'r') as file:

			d = file.read().split('\n')

			for line in d: #[:DATA_SIZE]:
				self._LINES.append(line)

			file.close()


		if(len(self._LINES)):
			#print("File uploaded ...", len(self._LINES))
			return True
		else:
			return False












		