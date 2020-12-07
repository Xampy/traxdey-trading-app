########################################################################
#
#
#  Default dialog Widget
#
#
########################################################################





from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


import qstylizer.style
import sys



class TAbstractDialogWidget(QDialog):
	"""docstring for DialogWidget
		
		An abstract Dialog Widget

		@buttons: allowed value are [O, OC]
	"""
	def __init__(self, parent=None, title_text="Dialog", buttons="O"):
		super(TAbstractDialogWidget, self).__init__(parent)
		self.parent = parent


		#self.setWindowFlags(Qt.WindowPopup)


		if(buttons == "OC"):

			Qbtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

			self._buttonBox = QDialogButtonBox(Qbtn)
			#self._buttonBox.accepted.connect(self.accept)
			self._buttonBox.rejected.connect(self.reject)
		elif (buttons == "O"):
			
			Qbtn = QDialogButtonBox.Ok 

			self._buttonBox = QDialogButtonBox(Qbtn)
			self._buttonBox.accepted.connect(self.accept)
		


		self.layout = QVBoxLayout()
		self.setLayout(self.layout)

		self.__title = QLabel(title_text)
		title_css = qstylizer.style.StyleSheet()
		title_css.setValues(
			color="white",
			fontSize="16px",
			paddingTop="5px",
			paddingBottom="10px"
		)
		self.__title.setStyleSheet(title_css.toString())
		self.layout.addWidget(self.__title)


		css = qstylizer.style.StyleSheet()
		css.setValues(
			backgroundColor="#171E31"
		)
		css.QPushButton.setValues(
			borderRadius="10px",
			border="1px solid white",
			color="white",
			width="100px",
			paddingTop="5px",
			paddingBottom="5px",
		)

		css.QPushButton.hover.setValues(
			backgroundColor="red",
		)

		ok_css = qstylizer.style.StyleSheet()
		ok_css.setValues(
			backgroundColor="red"
		)

		self.setStyleSheet(css.toString())


	def finish(self):
		"""
			Adding th accep and reject button at last
		"""

		self.layout.addWidget(self._buttonBox)


class TOkCancelDialogWidget(TAbstractDialogWidget):
	"""docstring for DialogWidget"""
	def __init__(self, parent=None, title_text="Dialog", layout=None):
		super(TOkCancelDialogWidget, self).__init__(parent=parent, title_text=title_text, buttons="OC")



class TOkDialogWidget(TAbstractDialogWidget):
	"""docstring for DialogWidget"""
	def __init__(self, parent=None, title_text="Error", layout=None):
		super(TOkDialogWidget, self).__init__(parent=parent, title_text="Error", buttons="O")





"""
app = QApplication(sys.argv)

screen = TAbstractDialogWidget()
screen.finish()
screen.show()

sys.exit(app.exec_())

"""
		

