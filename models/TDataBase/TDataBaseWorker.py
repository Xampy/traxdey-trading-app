##########################################################################
#
#
#  Data base thread manager
#
########################################################################



import traceback, sys
from PyQt5.QtCore import *
from PyQt5 import QtCore





class TDataBaseWorkerSignals(QObject):
	"""
		docstring for TTimeWorker

		finished: 
					No  data
		error: 
					'tuple' (exctype, value, traceback.format_exec())
		result:
					'object'

		progress:
					'int'  indicating % progress 

	"""
	"""def __init__(self):
		super(TTimeWorker, self).__init__()"""
	

	finished = pyqtSignal(int)
	error    = pyqtSignal(tuple)
	result   = pyqtSignal(str)
	progress = pyqtSignal(int)




class TDataBaseWorker(QRunnable):
	"""
		docstring for TDataBaseWorker
		
		exec task on dataBase

	"""
	def __init__(self, func=None, *args, **kwargs):
		super(TTimeWorker, self).__init__()
		

		self.func = func
		self.args = args
		self.kwargs = kwargs
		self.result = None

		self.signals = TTimeWorkerSignals()


		#Adding the call back to our kwargs
		#self.kwargs['progress_callback'] = self.signals.progress



	@pyqtSlot()
	def run(self):
		print("Running...")
		try:
			#Try to invoke functionon data

			self.result = self.func(*self.args, **self.kwargs)
			print("###############################################\n", self.result)

		except Exception as e:
			traceback.print_exc()
			exctype, value = sys.exc_info()[:2]
			self.signals.error.emit(
										(exctype, value, traceback.format_exc())
			)
		else:
			#We have a result
			self.signals.result.emit(self.result)		
		finally:
			#We have done the task
			self.signals.finished.emit(1)