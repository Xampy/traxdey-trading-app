########################################################################
#
#
#  Application Main
#
#
########################################################################

import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *



try:
    # Include in try/except block if you're also targeting Mac/Linux
    from PyQt5.QtWinExtras import QtWin
    myappid = 'xampy.trade_robot.traxdey.1'
    QtWin.setCurrentProcessExplicitAppUserModelID(myappid)    
except ImportError:
    pass

# ..or..
# import ctypes
# myappid = 'mycompany.myproduct.subproduct.version'
# ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)



from views.TMainWindow import TMainWindow
from TMainController import TMainController
from TMainModel import TMainModel


import ressource

#https://colorlib.com/preview/#nexus

class Traxdey(QApplication):

	"""
		A Room for student
	"""

	def __init__(self):
		QApplication.__init__(self, sys.argv)

		self.setWindowIcon(QIcon(':/icons/logo_ico'))

		try:

			self._traxdeyModel = TMainModel()

			self._traxdeyController = TMainController(
				_model = self._traxdeyModel
			)

			self._mainWindow = TMainWindow(_controller=self._traxdeyController, app=self)


			self._mainWindow.show()

			sys.exit(self.exec_())

		except Exception as err:
			print(err)



	def close(self):
		QApplication.quit()
		sys.exit()

if __name__ == "__main__":
	Traxdey()

