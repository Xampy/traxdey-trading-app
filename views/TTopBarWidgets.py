########################################################################
#
#
#  Main Window Top bar
#
#
########################################################################




from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


import qstylizer.style
import sys


MIN_WIDTH = 1050
MIN_HEIGHT = 40

class TTopBarWidget(QWidget):
	"""docstring for TTopBarWidget"""
	def __init__(self, parent=None):
		super(TTopBarWidget, self).__init__(parent)
		self.parent = parent



		layout = QHBoxLayout()
		self.setLayout(layout)
		title = QLabel("Traxdey")

		t_css = qstylizer.style.StyleSheet()
		t_css.setValues(
			color="white",
			fontSize="20px",

		)
		title.setStyleSheet(t_css.toString())
		layout.addWidget(title)


		_title = QLabel("")
		_title.setMaximumWidth(20)
		_title.setMaximumHeight(20)
		_title.setMinimumHeight(20)
		t_css = qstylizer.style.StyleSheet()
		t_css.setValues(
			color="white",
			fontSize="20px",
			width="20px",
			height="20px",
			backgroundColor="red",
			borderRadius="10px"

		)
		_title.setStyleSheet(t_css.toString())
		layout.addWidget(_title)



		self.setMinimumWidth(MIN_WIDTH)
		self.setMinimumHeight(MIN_HEIGHT)
		#self.setMaximumWidth(MIN_WIDTH)
		#self.setMaximumHeight(MIN_HEIGHT)
		#self.setWindowFlags(Qt.Window)




		css = qstylizer.style.StyleSheet()
		css.setValues(
			backgroundColor="#11182A"
		)

		self.setStyleSheet(css.toString())





		self.__isOnline = False



	def toggleOnlineState(self):
		"""
			Observe the network change state
			and update the component
		"""
		pass




"""
app = QApplication(sys.argv)

screen = TTopBarWidget()
screen.show()

sys.exit(app.exec_())
"""
		