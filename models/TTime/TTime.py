##########################################################################
#
#
#  Time manager
#
########################################################################


from datetime import datetime, time
import pandas as pd













class TTime(object):
	"""docstring for TTime"""
	def __init__(self):
		super(TTime, self).__init__()



	@staticmethod
	def convertToDataTime(str_date: str) -> float :
		"""
			convert a string date lika

				2020.05.03 00:56

			to a date time object

			datetime(year=2020, month=04, day=03, min=00, second=56)
		"""

		a = str_date.split()

		#print("\n\n\n", a)
		d, t = a[0].split('.'), a[1].split(':')

		return  datetime(
										year=int(d[0]),
										month=int(d[1]), 
										day=int(d[2]),

										hour=int(t[0]),
										minute=int(t[1])
				)  



	@staticmethod
	def convertToSecond(d_t: str) -> str:

		return 	str( (TTime.convertToDataTime(d_t) - datetime(year=1970, month=1, day=1) ).total_seconds() )




	@staticmethod
	def convertToDateHour(string_time) -> str:
		return pd.to_datetime(string_time, unit='s').strftime("%Y.%m.%d %H:%M")


	@staticmethod
	def addPeriod(time_start=None, period="min", p_type=1, count=1):
		"""
			Add an 
		"""


		if time_start is None:
			raise Exception("time_start must be different from Null...")
		else:

			#Convert s to seconds
			s = float( TTime.convertToSecond(time_start) )

			if period not in ["min", "hour", "day"]:
				raise Exception("period mus have value Union[min, hour, day].")
			else:

			    if period == "min":
			    	s += (p_type * 60 *count) #One minute is 60 seconds
			    elif period == "hour":
			    	s += (p_type * ( 60 * 60 ) *count) #One minute is 60*24 seconds
			    elif period == "day":
			    	s += (p_type * ( 60 * 60 * 24 ) *count ) #One minute is 60*24 seconds


			    s = str(s)

			    return TTime.convertToDateHour(string_time=s)




"""
t = TTime.convertToSecond("2020.05.03 00:56")
print(t)


ti = TTime.convertToDateHour(str(t))
print(ti)


ti_ = TTime.addPeriod("1000000000", period="day")
print(ti_)
"""
		