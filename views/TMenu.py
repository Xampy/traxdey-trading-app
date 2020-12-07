##########################################################################
#
#
#  Side Menu
#
#
########################################################################



from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *



import sys
import qstylizer.style




MENU_ITEMS_NAME = {"A": "Add","T":"Test", "H": "Help", "Ab":"About"}


from .TDialogGui.TChartDialogWidgets import TNewChartDialogWidget


class TSideMenuItem(QWidget):
	"""
		docstring for SideMenuItem

		They are composed with
		an icon and a text 

		@_controller is the chart controller 
		for controlling the data
	"""
	def __init__(self, parent=None, text="item", img_="", _controller=None):
		super(TSideMenuItem, self).__init__(parent)


		self.parent = parent
		self._controller = _controller
		self.setMaximumWidth(75)
		self.setMinimumWidth(75)


		##########################################
		#
		##

		self.__observers = []
		self.addObserver(self._controller)

		##########################
		#
		#############################



		layout = QBoxLayout(QBoxLayout.TopToBottom)
		layout.setContentsMargins(0, 0, 0, 0)
		self.setLayout(layout)



		self.__img = QLabel(parent)
		self.__img.setAlignment(Qt.AlignHCenter)

		self.__img.setPixmap(QPixmap("images/" + img_ + ".png"))
		layout.addWidget(self.__img)

		layout.setSpacing(10)

		self.__btn = QPushButton(parent=parent, text=text)
		self.__btn.setObjectName("menu_btn_" + text)
		layout.addWidget(self.__btn)







		#####################################################""
		#
		#  !! Delete bacground when rendrering final 
		#####################################################
		css = qstylizer.style.StyleSheet()
		css.setValues(
			borderRadius="3px",
			color="#54637A",
			padding="10px",
			fontSize="12px",
			backgroundColor="#11182A"
		)

		self.__btn.setStyleSheet(css.toString())


		self.__btn.clicked.connect(self.onBtnClicked)


	def hide(self):
		self.__btn.hide()
		self.__img.hide()

	def show(self):
		self.__btn.show()
		self.__img.show()


	def getBtn(self):
		return self.__btn


	def onBtnClicked(self):
		

		btnText = self.__btn.text()
		#print("Btn clicked :" , btnText)

		if btnText == MENU_ITEMS_NAME["A"] :



			#here we check if we have subscribed

			#Notify the menu that we will use an online model
			"""self.notify(msg={
								'chart': 
									{
										'type': 'online'
									}
								}
						)

			openNewChart = TNewChartDialogWidget(parent=self.parent, _controller=self._controller)


			

			#Add the parent of menu items which is the menu
			openNewChart.addObserver(self.parent)

			openNewChart.exec_()"""
			pass

		elif btnText == MENU_ITEMS_NAME["T"]:

			#Notify the menu that we will use a test model
			self.notify(msg={
								'chart': 
									{
										'type': 'test'
									}
								}
						)

			openNewChart = TNewChartDialogWidget(parent=self.parent, run_test=True, _controller=self._controller)

			
			#Add the parent of menu items which is the menu
			openNewChart.addObserver(self.parent)
			
			openNewChart.exec_()



	def addObserver(self, obs):

		if obs not in self.__observers:
			self.__observers.append(obs)


	def notify(self,msg):

		for obs in self.__observers:
			obs.update(msg)


	def update(self, msg):
		pass
			
				
		




		
		


class TSideMenuWiget(QWidget):
	"""
		docstring for SideMenuWiget

		The side menu of the whole application
		It gives option for adding new chart on graphics
		and others options

	"""
	def __init__(self, parent=None, _controller=None):
		super(TSideMenuWiget, self).__init__(parent)

		self._controller = _controller
		self.parent = parent

		self.__menuButtons = []


		################################################################""
		# There is only the chart object which oobserve the men Widget
		#

		self.__observers = []

		#
		#
		##################################################################


		ADD_MENU_ITEM_ID = 1
		GRAPHICS_MENU_ITEM_ID = 2
		ABOUT_MENU_ITEM_ID = 3

		self.setMinimumWidth(75)


		self.layout = QBoxLayout(QBoxLayout.TopToBottom)
		self.setLayout(self.layout)


		self.__btnGroup = QButtonGroup()
		self.__btnGroup.setExclusive(False)


		#Create menu items here
		menu_items_text = MENU_ITEMS_NAME.values()
		#print(menu_items_text)
		menu_items_img = ["add_chart","run_test", "help", "about"]

		for index, menu_text in enumerate(menu_items_text):
			item = TSideMenuItem(
				parent=self, text=menu_text,
				img_=menu_items_img[index], _controller=self._controller)


			self.__menuButtons.append(item)

			self.__btnGroup.addButton(item.getBtn(), id= index)
			self.layout.addWidget(item)



		#The stop button 
		self.__stopBtn =  QPushButton(
				parent=self, text="STOP")

		stop_css = qstylizer.style.StyleSheet()
		stop_css.setValues(
			width= "50px",
			height="50px",
			borderRadius="25px",
			color="white",
			padding="5px",
			fontWeight='bold',
			fontSize="15px",
			backgroundColor="red"
		)

		self.__stopBtn.setStyleSheet(stop_css.toString())
		self.__stopBtn.clicked.connect(self.toggleMenus)
		self.__stopBtn.setHidden(True)
		#Just after we show the stop button
		
		self.__itemsHiden = False

		"""for item in self.__menuButtons:
				print(item)"""













	def addObserver(self, obs):
		self.__observers.append(obs)


	def notifyObservers(self, msg):

		for observer in self.__observers:
			observer.update(msg)


	def update(self, msg):
		#print("( TMenu ) => Got update message: ", msg)

		#Check the data for a chart loading data
		if 'chart' in msg.keys():

			#Handle chart updating here

			#Search for atest case or a onternet case

			if 'test' in ( msg['chart'] ).keys():

				if msg['chart']['test']['data'] == "OK":
					#Now we cancall the chart to begin drawing
					self.notifyObservers(msg= {'chart': 
													{'test':
														{'data': 'OK'} 
													}
												}
										)


					self.toggleMenus()





	def toggleMenus(self):
		"""
			Hide the menu items and 
			show the chat plotting hiding plot
		"""

		if self.__itemsHiden :
			#We xant to stop the animation


			#Notify observers for chart stopping
			self.notifyObservers(msg= {'chart': 
											{'animate': 'stop'}
										}
								)

			for item in self.__menuButtons:
				item.show()

			#self.layout.addWidget(self.__stopBtn)
			self.__stopBtn.hide()


			self.__itemsHiden = False
		else:
			#Here the stop button appear

			for item in self.__menuButtons:
				item.hide()

			self.layout.addWidget(self.__stopBtn)
			self.__stopBtn.show()


			self.__itemsHiden = True



		
		



"""
app = QApplication(sys.argv)

screen = TSideMenuWiget()
screen.show()

sys.exit(app.exec_())

"""
		