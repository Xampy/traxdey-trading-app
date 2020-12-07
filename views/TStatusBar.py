##########################################################################
#
#
#  Left Dockable gui
#
#
########################################################################



from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


import qstylizer.style



import sys

class TBottomStatusWidget(QWidget):
	"""docstring for LoggingWidget"""
	def __init__(self, parent=None):
		super(TBottomStatusWidget, self).__init__(parent)

		self.__parent = parent

		layout =  QBoxLayout(QBoxLayout.LeftToRight)
		self.setLayout(layout)

		self.setMinimumHeight(40)
		self.setMaximumHeight(40)




		layout.setContentsMargins(0, 0, 0, 0)
		self.setLayout(layout)


		


		#The text todisplay
		self.__statusText = QLabel("Status : status text")
		self.__statusText.setAlignment(Qt.AlignVCenter)
		layout.addWidget(self.__statusText)


		text_css = qstylizer.style.StyleSheet()
		text_css.setValues(
			color="white",
			paddingTop="5px",
			paddingBottom='5px',
			paddingLeft="10px"
		)

		self.__statusText.setStyleSheet(text_css.toString())

		

"""
app = QApplication(sys.argv)

screen = TBottomStatusWidget()
screen.show()

sys.exit(app.exec_())"""