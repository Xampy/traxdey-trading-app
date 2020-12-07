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


COLORS = [
					"white",
					"blue",
					"red",
					"yellow",
					"orange",
					"gray",
					"black"

				]


class TDialogLineEditWidget(QLineEdit):
	"""docstring for TDialogLineEditWidget"""
	def __init__(self, parent=None):
		super(TDialogLineEditWidget, self).__init__(parent)
		self.parent = parent


		css = qstylizer.style.StyleSheet()
		css.setValues(
			backgroundColor="#212735",
			borderRadius="5px",
			fontSize="10px",
			color="white",
			paddingBottom="5px",
			paddingTop="5px",
			paddingLeft="5px"
		)

		self.setText("")

		self.setStyleSheet(css.toString())

class TDialogComboBoxWidget(QComboBox):
	"""docstring for TDialogLineEditWidget"""
	def __init__(self, parent=None, str_items=[]):
		super(TDialogComboBoxWidget, self).__init__(parent)
		self.parent = parent


		self.insertItems(0, str_items)


		css = qstylizer.style.StyleSheet()
		css.setValues(
			backgroundColor="#212735",
			borderRadius="5px",
			border="none",
			fontSize="10px",
			color="white",
			paddingBottom="5px",
			paddingTop="5px",
			paddingLeft="5px",
			width="90px"
		)
		css.QComboBox['::drop-down'].setValues(
			border="none",
			backgroundColor="none"
		)

		#print(css.toString())

		self.setStyleSheet(css.toString())

class TDialogFieldTitle(QLabel):
	"""docstring for TDialogLineEditWidget"""
	def __init__(self, parent=None, title="Title", font_size="12px", bold="none", color="gray"):
		super(TDialogFieldTitle, self).__init__(parent)
		self.parent = parent
		self.setText(title)


		css = qstylizer.style.StyleSheet()
		css.setValues(
			color=color,
			fontSize=font_size,
			marginTop="10px",
			fontWeight=bold
		)

		self.setStyleSheet(css.toString())