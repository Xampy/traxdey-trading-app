##########################################################################
#
#
#  Time thread : for calculate the next time 
#				of the endof the prediction
#
########################################################################


from .TTime import TTime
from .TTimeWorkers import TTimeWorker


from PyQt5.QtCore import QThreadPool



class PeriodInterval(TTimeWorker):
	"""
		docstring for PeriodInterval

		It tooks starter date and give the finished date time
	"""
	def __init__(self, got_result_fn=None, **kwargs):

		#funct = ; (time_start=None, period="min", p_type=1, count=0):
		#print(self.funct, self.funct(time_start="2020.05.09 00:56", period="min", p_type=1, count=1))


		super(PeriodInterval, self).__init__(func=self.exec_funct, **kwargs)



		if got_result_fn != None :
			self.signals.result.connect(got_result_fn)
		else:
			self.signals.result.connect(self.manage_result)

		self.signals.finished.connect(self.thread_complete)
		self.signals.progress.connect(self.progress_fn)


	def exec_funct(self, **kwargs):
		return TTime.addPeriod(**kwargs)


	def manage_result(self, result):
		"""
			Call the launcher to upadte his information with result
		"""
		#print("Result: ", result)
		pass


	def thread_complete(self, t):
		"""
			Call the launcher to upadte his information with result
		"""
		print("Done", t)
		pass


	def progress_fn(self):
		"""

		"""

		print("In progress...")
		pass



class TTimePeriodHandler(object):
	"""
		docstring for TTimePeriodHandler


		handle a periodcalculation

	"""
	def __init__(self, owner=None):
		super(TTimePeriodHandler, self).__init__()
		self.__owner = owner



	def run(self, func, s_date_time: str, _period="min", _p_type=1, _count=1):
		"""
			Begin here
		"""


		try:
			p = PeriodInterval(
									got_result_fn=func,
									time_start=str(s_date_time),
									period=_period,
									p_type=_p_type, 
									count=_count)
			return p
		except Exception as e:
			raise e
		#The runnable
		
		

		


#t = QThreadPool()
"""p = PeriodInterval(time_start="2020.05.09 00:56", period="min", p_type=1, count=1)

t.start(p)
"""