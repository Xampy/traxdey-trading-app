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

CHART_DATA_PERIODS = {
	"P_M1"	:	("min", 1), 
	"P_M5"	: 	("min", 5), 
	"P_M15"	: 	("min", 15),
	"P_M30"	: 	("min", 30), 
	"P_H1"	: 	("hour", 1),
	"P_H4"	: 	("hour", 4), 
	"P_D1"	:	("day", 1)
}

class TOnlineChartModel(TAbstractChartModel):
	"""docstring for TChartDataModel"""
	def __init__(self, mt5Client=None):
		super(TOnlineChartModel, self).__init__()


		self._mt5Client = mt5Client



	def readOneData(self):
		"""
			Read a sigle line of data
		"""

		if self._mt5Client is not None:
			datas = self._mt5Client.getData()

			if datas is not None:
				PERIOD = int(self._config['data']['predict'])
				HALF_PERIOD = int(PERIOD/2)

				data = []

				#Time Got
				self._LAST_PERIOD_PREDICTED_END = datas['time']

				#time open high low close tick_volume spread real_
				#Switch the price type calucation

				w_p = self._config['data']['price']
				v = 0

				if(w_p == CHART_PRICES_TYPE['O']):
					v = float(datas['open']) 

				elif(w_p == CHART_PRICES_TYPE['C']):
					
					v = float(datas['close']) 

				elif(w_p == CHART_PRICES_TYPE['H']):
					
					v = float(datas['high'])

				elif(w_p == CHART_PRICES_TYPE['L']):

					v = float(datas['low']) 

				elif(w_p == CHART_PRICES_TYPE['HL/2']):
					v = ( float(datas['low']) + float(datas['high']) ) /2
				
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








		