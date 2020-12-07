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


class TPriceTextWidget(QWidget):
	"""docstring for PriceTextWidget"""
	def __init__(self, parent=None, borderColor='white', textColor='white'):
		super(TPriceTextWidget, self).__init__(parent)
		self.parent = parent


		layout = QBoxLayout(QBoxLayout.TopToBottom)
		self.setLayout(layout)

		self.__text = QLabel('0.000000')
		layout.addWidget(self.__text)


		css = qstylizer.style.StyleSheet()
		css.setValues(
			backgroundColor="#11182A",
			width="200px",
			border="1px solid " + borderColor,
			borderRadius="10px",
			paddingLeft="20px",
			paddingRight="20px",
			paddingTop="5px",
			paddingBottom="5px",
			color=textColor
		)

		self.setStyleSheet(css.toString())


	def setText(self, text):
		self.__text.setText("{:.6f}".format(float(text)))


	def setColor(self, color):
		css = qstylizer.style.StyleSheet()
		css.setValues(
			backgroundColor="#11182A",
			width="200px",
			border="1px solid " + color,
			borderRadius="10px",
			paddingLeft="20px",
			paddingRight="20px",
			paddingTop="5px",
			paddingBottom="5px",
			color=color
		)

		self.setStyleSheet(css.toString())


class TPricesBarWidget(QWidget):
	"""docstring for PricesBarWidget"""
	def __init__(self, parent=None):
		super(TPricesBarWidget, self).__init__(parent)
		self.parent = parent



		###################################################"""
		#
		# Typically only the cchar model look on this

		self.__observers = []

		#
		#
		######################################################

		layout = QBoxLayout(QBoxLayout.LeftToRight)
		self.setLayout(layout)


		self.__realPrice = TPriceTextWidget(parent=self)
		self.__realSMA = TPriceTextWidget(parent=self, borderColor='#1F77B4', textColor='#1F77B4')
		self.__futureSMA = TPriceTextWidget(parent=self, borderColor='#2DAB40', textColor='#2DAB40')


		layout.addWidget(self.__realPrice)
		layout.addWidget(self.__realSMA)
		layout.addWidget(self.__futureSMA)





	def notify(self, msg):
		pass

	def update(self, msg):
		"""
			the message is for three component

		"""

		#print("\n (TPrices) Got msg from ", msg)

		if 'prices' in msg.keys():
			if 'values' in ( msg['prices'] ).keys():
				if 'RP' in ( msg['prices']['values'] ).keys():
					self.__realPrice.setText(msg['prices']['values']['RP'])
				if 'RS' in ( msg['prices']['values'] ).keys():
					self.__realSMA.setText(msg['prices']['values']['RS'])
				if 'FS' in ( msg['prices']['values'] ).keys():
					self.__futureSMA.setText(msg['prices']['values']['FS'])

			if 'colors' in ( msg['prices'] ).keys():

				
				if 'RP' in ( msg['prices']['colors'] ).keys():
					self.__realPrice.setColor(msg['prices']['colors']['RP'])
				if 'RS' in ( msg['prices']['colors'] ).keys():
					self.__realSMA.setColor(msg['prices']['colors']['RS'])
				if 'FS' in ( msg['prices']['colors'] ).keys():
					self.__futureSMA.setColor(msg['prices']['colors']['FS'])
		

"""
app = QApplication(sys.argv)

screen = TPricesBarWidget()
screen.show()

sys.exit(app.exec_())
"""

