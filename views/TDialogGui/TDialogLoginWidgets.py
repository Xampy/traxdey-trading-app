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


from .TDialogCore import TDialogLineEditWidget, TDialogFieldTitle
from .TAbstractDialogWidgets import TOkCancelDialogWidget
from .TDialogErrorWidgets import  TDialogErrorWidget


class TDialogLoginWidget(TOkCancelDialogWidget):
	"""
	docstring for TDialogLoginWidget
	"""
	def __init__(self, parent=None, _controller=None):
		super(TDialogLoginWidget, self).__init__(parent=parent, title_text="Login")


		self.__controller = _controller
		self.__controller.getModel().addObserver(self)

		self.setMinimumWidth(500)		
		self.setWindowModality(Qt.ApplicationModal)

		main_layout = QGridLayout()
		#main_layout.setPadding(100, 100, 100, 0)
		self.__email = TDialogLineEditWidget(parent=self)

		main_layout.addWidget(
			TDialogFieldTitle(title="Email"), 0, 0)
		main_layout.addWidget(self.__email, 1, 0)



		self.__pass = TDialogLineEditWidget(parent=self)
		self.__pass.setEchoMode(QLineEdit.Password)

		main_layout.addWidget(
			TDialogFieldTitle(title="Password"), 2, 0)
		main_layout.addWidget(self.__pass, 3, 0)


		main_layout.addWidget(
			TDialogFieldTitle(title=""), 4, 0)




		self.layout.addLayout(main_layout)
		self.finish()


		self._buttonBox.accepted.connect(self.onOkButtonClicked)



	def onOkButtonClicked(self):
		
		#print("Want to check email...")

		#The the emailand the password
		e = self.__email.text()
		p = self.__pass.text()
		if len(e) > 0 and len(p) > 0:

			#print("email " + e + " password " + p)


			#Validate the email
			if self.__controller.validateEmail(email=e, password=p):
				pass
			else:
				error = TDialogErrorWidget(parent=self, error="Your email is invalid...")
				error.exec_()
		else:
			error = TDialogErrorWidget(parent=self, error="Check your email and password ...")
			error.exec_()


	def update(self, msg: dict):
		"""
			Update information provide from the model
		"""

		#print("(TLogin) => Got message ", msg)
		if 'login' in msg.keys():
			if 'error' in ( msg['login'] ).keys():
				error = TDialogErrorWidget(parent=self, error=msg['login']['error'])
				error.exec_()

			if 'success' in ( msg['login'] ).keys():
				self.accept()


"""
app = QApplication(sys.argv)

screen = TDialogLoginWidget()
#screen.finish()
screen.show()

sys.exit(app.exec_())"""
