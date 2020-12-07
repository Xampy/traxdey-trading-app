#########################################################################
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


import sys


class TInfoWidget(QWidget):
	"""docstring for InfoWidget"""
	def __init__(self, parent=None):
		super(TInfoWidget, self).__init__(parent)
		self.parent = parent

		self.setMinimumWidth(100)


		css = qstylizer.style.StyleSheet()
		css.setValues(
			backgroundColor="#1F2531",
			borderRadius="10px",
			padding="20px",
			color="white"
		)

		self.setStyleSheet(css.toString())




class TPeriodInfo(TInfoWidget):
	"""docstring for PeriodInfo"""
	def __init__(self, parent=None):
		super(TPeriodInfo, self).__init__(parent)
		

		layout = QBoxLayout(QBoxLayout.TopToBottom)
		layout.setContentsMargins(0, 0, 0, 0)
		self.setLayout(layout)

		css = qstylizer.style.StyleSheet()
		css.setValues(
			backgroundColor="#1F2531",
			borderRadius="10px",
			paddingTop="20px",
			paddingBottom="20px",
			paddingLeft="10px",
			color="white"
		)

		self.setStyleSheet(css.toString())

		self.__startTimeValue = QLabel(
			"<span style='font-size: 10px; font-weight: bold; color: gray'>S. TIME :</span> 2020-06-17 21:06:05")


		self.__endTimeValue = QLabel(
			"<span style='font-size: 10px; font-weight: bold; color: gray'>E. TIME :</span> 2020-06-17 21:06:05")

		self.__barCountValue = QLabel(
			"<span style='font-size: 10px; font-weight: bold; color: gray'>Bars :</span> 100")



		layout.addWidget(self.__startTimeValue)
		layout.addWidget(self.__endTimeValue)
		layout.addWidget(self.__barCountValue)



	#Set the textfor a given 
	def setInfosText(self, text, info="S"):

		if info in ['S', "E"]:
			#The text is for the start and the ending widget
			form = "<span style='font-size: 10px; font-weight: bold; color: gray'>{:s}. TIME :</span> {:s}"

			if info == "S":
				self.__startTimeValue.setText( form.format("S", text) )
			elif info == "E":
				self.__endTimeValue.setText( form.format("E", text) )


		elif info == 'BC':
			form = "<span style='font-size: 10px; font-weight: bold; color: gray'>Bars :</span> {:s}"
			self.__barCountValue.setText(form.format(text))






	def update(self, msg):

		if 'chart' in msg.keys():

			if 'infos' in ( msg['chart'] ).keys():

				if 'ST' in ( msg['chart']['infos'] ).keys():
					self.setInfosText(
							text=msg['chart']['infos']['ST'],
							info="S"
					)
				if 'ET' in ( msg['chart']['infos'] ).keys():
					self.setInfosText(
							text=msg['chart']['infos']['ET'],
							info="E"
					)
				if 'BC' in ( msg['chart']['infos'] ).keys():
					self.setInfosText(
							text=msg['chart']['infos']['BC'],
							info="BC"
					)






class TDataAccurrancyWidget(QWidget):
	"""docstring for DataAccurrancyWidget"""
	def __init__(self, parent=None):
		super(TDataAccurrancyWidget, self).__init__(parent)
		

		self.parent = parent

		layout = QBoxLayout(QBoxLayout.TopToBottom)
		self.setLayout(layout)

		text = QLabel('Accurancy')
		t_css = qstylizer.style.StyleSheet()
		t_css.setValues(
			color="gray",
			backgroundColor="none",
			fontSize='15px',
			fontWeight='bold',
		)
		text.setStyleSheet(t_css.toString())
		layout.addWidget(text)


		self.__accurancy = QLabel('90%')
		self.__accurancy.setAlignment(Qt.AlignHCenter)
		a_css = qstylizer.style.StyleSheet()
		a_css.setValues(
			color="#2DAB40",
			fontSize='25px',
			fontWeight='bold',
			backgroundColor="none"
		)
		self.__accurancy.setStyleSheet(a_css.toString())
		layout.addWidget(self.__accurancy)



	def update(self, msg):

		if 'chart' in msg.keys():

			if 'infos' in ( msg['chart'] ).keys():

				if 'AC' in ( msg['chart']['infos'] ).keys():
					self.__accurancy.setText(msg['chart']['infos']['AC'])



		



class TTrendWidget(QWidget):
	"""docstring for InfoWidget"""
	def __init__(self, parent=None, _type="UP"):
		super(TTrendWidget, self).__init__(parent)
		self.parent = parent
		self.setMinimumWidth(100)



		layout = QBoxLayout(QBoxLayout.TopToBottom)
		layout.setContentsMargins(0, 0, 0, 0)
		self.setLayout(layout)

		text = QLabel(_type)
		text.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
		css = qstylizer.style.StyleSheet()

		if _type == "UP":
			css.setValues(
				backgroundColor="#2DAB40",
				borderRadius="10px",
				color="white",
				fontSize='25px'
			)
		elif _type == "DOWN":
			css.setValues(
				backgroundColor="#DB4834",
				borderRadius="10px",
				color="white",
				fontSize='25px'
			)

		
		text_css = qstylizer.style.StyleSheet()
		css.setValues(
			padding="10px",
			color="white"
		)
		text.setStyleSheet(text_css.toString())


		layout.addWidget(text)
		self.setStyleSheet(css.toString())


		



class TChartInfoWidget(QWidget):
	"""
		docstring for ChartInfoWidget

		@controller : is themain chart controller

	"""
	def __init__(self, parent=None, controller=None):
		super(TChartInfoWidget, self).__init__(parent)


		self.setMaximumWidth(200)
		

		self.parent = parent
		self._controller = controller




		#################################################
		#
		#
		#########

		self._observers = []

		###############################
		#
		#
		################################################

		layout = QBoxLayout(QBoxLayout.TopToBottom)
		self.setLayout(layout)


		self.__timerInfo = TPeriodInfo(parent=self)
		layout.addWidget(self.__timerInfo)


		self.__accurancyInfo = TDataAccurrancyWidget(parent=None)
		layout.addWidget(self.__accurancyInfo)


		self.__trendUp = TTrendWidget(parent=self, _type="UP")
		layout.addWidget(self.__trendUp)
		self.__trendDown = TTrendWidget(parent=self, _type="DOWN")
		layout.addWidget(self.__trendDown)



		#Adding the timer info to the chartwidgetcontrooler model observer 
		#self._controller.getModel().addObserver(self.__timerInfo)



	def update(self, msg):
		

		if 'chart' in msg.keys():
			if 'model' in msg['chart'].keys():
				if msg['chart']['model'] == "ok":
					#Adding the timer info to the chartwidgetcontrooler model observer 
					self._controller.getModel().addObserver(self.__timerInfo)
					self._controller.getModel().addObserver(self.__accurancyInfo)

	def notify(self, msg):
		pass


	def addObserver(self, obs):

		if obs not in self.__obervers:
			self.__observers.append(obs)

















"""
app = QApplication(sys.argv)

screen = TChartInfoWidget()
screen.show()

sys.exit(app.exec_())
"""		
