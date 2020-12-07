########################################################################
#
#
#  Error Dialog Notify
#
#
########################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


import qstylizer.style
import sys




from .TAbstractDialogWidgets import TOkDialogWidget

class TDialogErrorWidget(TOkDialogWidget):
	"""docstring for TDialogErrorWidget"""
	def __init__(self, parent=None, error="error"):
		super(TDialogErrorWidget, self).__init__(parent)
		self.parent = parent
		self.setWindowModality(Qt.ApplicationModal)


		e = QLabel(error)
		e.setAlignment(Qt.AlignHCenter)
		css = qstylizer.style.StyleSheet()
		css.setValues(
			color="white",
			paddingTop="20px",
			paddingBottom="20px"
		)
		e.setStyleSheet(css.toString())
		self.layout.addWidget(e)


		self.finish()
		