###########################################################"
#
#
# Abstract MQT5 Client
#
#
#############################################################
from datetime import datetime, timezone, timedelta
import MetaTrader5 as mt5


# display data on the MetaTrader 5 package
print("MetaTrader5 package author: ",mt5.__author__)
print("MetaTrader5 package version: ",mt5.__version__)
 
import pytz
import ntplib



class MQT5Client(object):
	"""docstring for MQT5_Client"""
	def __init__(self, error_dialog=None):
		super(MQT5Client, self).__init__()
		

		# establish connection to MetaTrader 5 terminal
		if not mt5.initialize():
		    #print("initialize() failed, error code =",mt5.last_error())

		    if error_dialog :
		    	error_dialog.exec_()


		    quit()

		# set time zone to UTC
		self._timezone = pytz.timezone("Etc/UTC")

		#create 'datetime' object in UTC time zone to avoid the implementation of a local time zone offset
		self._utc_from = None #:utc_from = datetime.now(timezone.utc)# datetime(2020, 7, 24, tzinfo=self._timezone) #datetime.utcnow()



		#The amount of data that we want
		self._maxCount = 1



		self._params = {
							'symbol': "EURUSD",
							'period': mt5.TIMEFRAME_M1
		}

		self._lastPeriod = None




	def setParameters(self, params: dict):

		assert 'symbol'  in params.keys() and 'period'  in params.keys()
		
		self._params = params



	def getTime(self):
		"""
			Get the utc time
		"""

		#It is the first time we ask for time
		if self._utc_from is None:
			print("Utc is None")
			start = None
			try:
				#Europe time
				x = ntplib.NTPClient()
				start = datetime.utcfromtimestamp(x.request('europe.pool.ntp.org').tx_time)
				print("New Start date ", start);
			except Exception as e:
				#Notify the view for an error
				raise e

			if start is not None:
				#We add 3 hours in order to be in metaTrader5 time
				h =timedelta(hours=3)
				self._utc_from = start + h
			else:
				#Notify for eror
				pass
		else:
			#We just add 1 minute or the timeframe to the
			h =timedelta(minutes=1)
			self._utc_from = self._utc_from + h

		print("New datetime  ", self._utc_from)
		return self._utc_from

	def getData(self):



		#This is the firs attempt
		if True:

			if not mt5.initialize():
			    print("initialize() failed, error code =",mt5.last_error())
			    quit()


			#self._utc_from = datetime.now(timezone.utc)
			self._utc_from = self.getTime()
			print("\n\nDate ", self._utc_from, "\n\n\n")

			rates = mt5.copy_rates_from(
				self._params['symbol'],
				self._params['period'], 
				self.getTime(), self._maxCount)

			
			


			print(rates)
			rates_frame = rates[0]

			self._lastPeriod = 0


			
			result = {

						'time': datetime.strftime(  datetime.fromtimestamp( int( rates_frame[0] ) ) , '%Y.%m.%d %H:%M') , #.replace('-', '.'),
						'open': rates_frame[1],
						'high': rates_frame[2],
						'low': rates_frame[3],
						'close': rates_frame[4]
			}


			print("Result\n\n", result)
			mt5.shutdown()
			                           


			return result


	def shutDown(self):
		mt5.shutdown()


"""m = MQT5Client()
m.getData()"""