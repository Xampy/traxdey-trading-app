##########################################################################
#
#
#  mAIN WINDOW gui
#
#
########################################################################





from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


import qstylizer.style



from .TTopBarWidgets import TTopBarWidget
from .TStatusBar import TBottomStatusWidget
from .TMenu import TSideMenuWiget
from .TChartGui.TChartWidgets import  TChartWidget
from .TDialogGui.TDialogLoginWidgets import TDialogLoginWidget



import sys

MIN_WIDTH = 1050
MIN_HEIGHT = 500


class TMainWindow(QWidget):
	"""docstring for MainWindow"""
	def __init__(self, _controller=None, app=None):
		QWidget.__init__(self)


		self.parent = app
		self._controller = _controller

		self.setWindowFlags(Qt.FramelessWindowHint)
		self.setWindowIcon(QIcon('images/logo.png')) 



		self.setWindowTitle("Traxdey")
		self.resize(MIN_WIDTH, MIN_HEIGHT)
		self.setMinimumWidth(MIN_WIDTH)
		self.setMinimumHeight(MIN_HEIGHT)
		self.setMaximumWidth(MIN_WIDTH)
		self.setMaximumHeight(MIN_HEIGHT)
		self.setWindowFlags(Qt.Window)


		css = qstylizer.style.StyleSheet()
		css.setValues(
			backgroundColor="#11182A"
		)

		self.setStyleSheet(css.toString())






		#The main Layout
		layout = QBoxLayout(QBoxLayout.TopToBottom)
		layout.setContentsMargins(0, 0, 0, 0)
		self.setLayout(layout)





		#The main windw is divided into Two BigWidget

		#Top we have the main widget 
		#and at bottom have astatus bar

		######################################################
		#
		#  Top Widget 
		#
		#################################


		self.__topBar = TTopBarWidget(parent=self)
		layout.addWidget(self.__topBar)


		###################################################################

		main_widgetLayout = QBoxLayout(QBoxLayout.LeftToRight)
		main_widgetLayout.setContentsMargins(0, 0, 0, 0)
		layout.addLayout(main_widgetLayout)




		##############################################################
		#########" The side menu
		self.__sideMenu = TSideMenuWiget(parent=self, _controller=self._controller.getControllerByName('chart'))
		main_widgetLayout.addWidget(self.__sideMenu)


		###############################################################
		#########" The chart view"
		self.__chart = TChartWidget(
			parent=self, 
			_controller=self._controller.getControllerByName('chart')
		)
		main_widgetLayout.addWidget(self.__chart)


		####################
		#
		#  The bottom status bar
		#
		######################
		self.__bottomStatusBar = TBottomStatusWidget(parent=self)
		layout.addWidget(self.__bottomStatusBar)





		#Take observers control
		self.__sideMenu.addObserver(self.__chart) 




		######################################################
		#
		#  Login asking here for first time
		#     
		##

		self.__loginCheck = TDialogLoginWidget(
			parent=self,
			_controller=self._controller.getControllerByName('login')
		)


		#If user click cancelwe close the application
		self.__loginCheck._buttonBox.rejected.connect(self.onCancelButtonClicked)
		#Check
		self.__loginCheck.exec()

		##
		#
		#
		#######################################################






	def onCancelButtonClicked(self):
		"""
		"""
		print("Don't want to log in")

		if self.parent is not None:
			self.parent.close()

		


"""
app = QApplication(sys.argv)

screen = TMainWindow()
screen.show()

sys.exit(app.exec_())
		
		"""