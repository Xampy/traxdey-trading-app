########################################################################
#
#
#  Dialog window gui
#
#
########################################################################





from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


import qstylizer.style
import sys


COLORS = ["white", "blue", "red", "yellow", "orange", "gray", "black"]
PRICES_TYPE = ["Open", "Close", "High", "Low", "(Hight, Low)/2"]
DATA_PERIODS = ["P_M1", "P_M5", "P_M15", "P_M30", "P_H1", "P_H4", "P_D1"]
PREDICT_BARS_COUNTS = ["20", "120", "200", "1000"]




from .TAbstractDialogWidgets import TOkCancelDialogWidget
from .TDialogErrorWidgets import  TDialogErrorWidget
from .TDialogCore import TDialogLineEditWidget,\
						TDialogComboBoxWidget, TDialogFieldTitle


class TNewChartDialogWidget(TOkCancelDialogWidget):
	"""
		AddChartDialogWidget

		Get inputs from the user to paramate
		plot configuration
	"""

	def __init__(self, parent=None, run_test=False, _controller=None):
		super(TNewChartDialogWidget, self).__init__(parent=parent, title_text="New Chart")
		
		self.parent = parent
		self.is_runningTest = run_test
		self.__dataFilename = None
		self._controller = _controller


		self.setWindowModality(Qt.ApplicationModal)



		########################################################################
		#
		#

		self._buttonBox.accepted.connect(self.onOkButtonClicked)


		#
		#
		#############################################################################


		#######################################################################
		#
		#

		self.__observers = []  #Only the menu is an observer

		#
		#
		#######################################################################





		#self.setWindowFlags(Qt.Dialog)

		setting_layout = QHBoxLayout()

		#The symbol choice
		main_layout = QGridLayout()
		main_layout.setHorizontalSpacing(5)
		main_layout.setVerticalSpacing(5)

		#Main setting
		#The sub title
		main_layout.addWidget(
			TDialogFieldTitle(
				parent=self, title="Data Settings",
				font_size="15px", bold="bold", color="white"
			)
			, 0, 0)


		#The symbol
		self._symbolCombobox = TDialogComboBoxWidget(
			parent=self,
			str_items= 
				[
					"EUR - USD",
					"EUR - CAD"

				]
		)
		main_layout.addWidget(
			TDialogFieldTitle(title="Symbol"), 1, 0)
		main_layout.addWidget(self._symbolCombobox, 2, 0)

		#Period
		period = QLabel("Period")
		self._periodComboBox = TDialogComboBoxWidget(
			parent=self,
			str_items=DATA_PERIODS
		)

		main_layout.addWidget(
			TDialogFieldTitle(title="Data Period"), 1, 1)
		main_layout.addWidget(self._periodComboBox, 2, 1)




		#Data type on which will be sma calculated
		self._priceComboBox = TDialogComboBoxWidget(
			parent=self,
			str_items=PRICES_TYPE
		)
		main_layout.addWidget(
			TDialogFieldTitle(title="Price"), 3, 0)
		main_layout.addWidget(self._priceComboBox, 4, 0)


		#Prediction bar
		self._predictCountComboBox = TDialogComboBoxWidget(
			parent=self,
			str_items=PREDICT_BARS_COUNTS
		)

		main_layout.addWidget(
			TDialogFieldTitle(title="Prediction Bars Count"), 5, 0)
		main_layout.addWidget(self._predictCountComboBox, 6, 0)
		main_layout.addWidget(QLabel(), 7, 0)


		#Add file choosing dialog if weare running test

		if(self.is_runningTest):

			main_layout.addWidget(
				TDialogFieldTitle(title="You are Running Test mode",color="white"), 8, 0)

			main_layout.addWidget(
				TDialogFieldTitle(title="Choose File (.csv)",), 9, 0)


			self.__choosingFileBtn = QPushButton("Choose")
			self.__choosingFileBtn.clicked.connect(self.chooseFile)
			main_layout.addWidget(
				self.__choosingFileBtn, 9, 1)
			





		setting_layout.addLayout(main_layout)




		#Coloringsetting

		#The normal data
		line_color_layout = QGridLayout()
		line_color_layout.setHorizontalSpacing(5)
		line_color_layout.setVerticalSpacing(5)


		#The sub title
		line_color_layout.addWidget(
			TDialogFieldTitle(
				parent=self, title="Color Settings",
				font_size="15px", bold="bold", color="white"
			)
			, 0, 0)


		#Color Setting
		self._priceColorComboBox = TDialogComboBoxWidget(
			parent=self,
			str_items=COLORS
		)
		line_color_layout.addWidget(
			TDialogFieldTitle(title="Price"), 1, 0)
		line_color_layout.addWidget(
			self._priceColorComboBox, 2, 0)

		#The normal SMA color
		self._SMAColorComboBox = TDialogComboBoxWidget(
			parent=self,
			str_items=COLORS
		)

		line_color_layout.addWidget(
			TDialogFieldTitle(title="Price SMA"), 1, 1)
		line_color_layout.addWidget(self._SMAColorComboBox, 2, 1)


		#Predicted SMA
		self._PSMAColorComboBox = TDialogComboBoxWidget(
			parent=self,
			str_items=COLORS
		)

		line_color_layout.addWidget(
			TDialogFieldTitle(title="Predicted SMA"), 3, 0)
		line_color_layout.addWidget(self._PSMAColorComboBox, 4, 0)
		line_color_layout.addWidget(QLabel(), 5, 0)
		line_color_layout.addWidget(QLabel(), 6, 0)
		line_color_layout.addWidget(QLabel(), 7, 0)




		if(self.is_runningTest):
			line_color_layout.addWidget(QLabel(), 8, 0)
			line_color_layout.addWidget(QLabel(), 9, 0)

		

		setting_layout.addSpacing(100)
		setting_layout.addLayout(line_color_layout)


		self.layout.addLayout(setting_layout)

		self.finish()




	def chooseFile(self):

		file_name = QFileDialog.getOpenFileName(self,
			'Choose File',
			'c:\\',
			"CSV or Text files(*.csv *.txt)")

		#print("Have choosed : ", file_name)

		"""[Output]
			Have choosed :  ('', '')
			Have choosed :  ('D:/test.txt', 'CSV or Text files(*.csv *.txt)')
		"""

		self.__dataFilename = file_name[0]




	def onOkButtonClicked(self):
		"""
			Wen the user press ok button
			We check if there is a correct data
			if not we showan error dialog
		"""


		if self.is_runningTest:

			#It's a test

			result = self._controller.setModelFile(self.__dataFilename)
			if result:
				#Proceed data and set the model

				#Construct the datamodel config here
				chart_config  = {
									'data': {
										'symbol'  : self._symbolCombobox.currentText(),
										'period'  : self._periodComboBox.currentText(),
										'price'   : self._priceComboBox.currentText(),
										'predict' : self._predictCountComboBox.currentText()
									},
									'color': {
										'price'   : self._priceColorComboBox.currentText(),
										'SMA'     : self._SMAColorComboBox.currentText(),
										'P_SMA'   : self._PSMAColorComboBox.currentText()
									}
								}


				#print("Chart config \n", chart_config)

				#Notify the model to choose test model
				#Notify the observers
				self.notify(msg={
									'chart': 
										{
											'type': 'test'
										}
									}
							)

				#Set the model file name here
				try:
					model = self._controller.getModel()
				except Exception as e:
					raise e
				
				result = model.readData(filename=self.__dataFilename)

				if result:

					#Set plotting configuration
					model.setParams(chart_config)


					
					#Notify the observers
					self.notify(msg={'chart': 
											{'test':
												{'data': 'OK'} 
											}
										}
								)

				self.accept()
			else:

				error = TDialogErrorWidget(parent=self, error="File name is empty..")
				error.exec_()


		else:
			###########################################
			#
			#  Here we are on real data
			#
			########
			

			#Construct the datamodel config here
			chart_config  = {
								'data': {
									'symbol'  : self._symbolCombobox.currentText(),
									'period'  : self._periodComboBox.currentText(),
									'price'   : self._priceComboBox.currentText(),
									'predict' : self._predictCountComboBox.currentText()
								},
								'color': {
									'price'   : self._priceColorComboBox.currentText(),
									'SMA'     : self._SMAColorComboBox.currentText(),
									'P_SMA'   : self._PSMAColorComboBox.currentText()
								}
							}


			#print("Chart config \n", chart_config)
			#Set the model file name here
			model = self._controller.getModel()
			
			#Set plotting configuration
			model.setParams(chart_config)


			#Notify the observers
			self.notify(msg={'chart': 
									{'test':
										{'data': 'OK'} 
									}
								}
						)



			self.accept()

	def addObserver(self, obs):
		self.__observers.append(obs)


	def notify(self, msg):

		for observer in self.__observers:
			observer.update(msg)
			

		




"""

app = QApplication(sys.argv)

screen = TNewChartDialogWidget()
screen.show()

sys.exit(app.exec_())
"""