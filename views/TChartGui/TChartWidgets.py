##########################################################################
#
#
#  Chart Gui
#
#
########################################################################





from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *



import matplotlib

#Setting the matplolib for using Qt5 app widget
matplotlib.use('Qt5Agg')

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation


import qstylizer.style


import sys
import math



from .TChartDataWidgets import TChartInfoWidget
from .TPricesBarWidgets import TPricesBarWidget




class ChartCanvasDrawingWidget(FigureCanvasQTAgg):
	"""docstring for ChartDrawingWidget"""
	def __init__(self, parent=None, width=6,height=3.125,dpi=100):

		self.parent = parent


		self.fig = Figure(figsize=(width,height), dpi=dpi)
		#self.fig.subplots_adjust(bottom=0, top=1, left=1, right=0)
		self.fig.set_facecolor('#171E31')
		self.fig.set_edgecolor('#171E31')
		self.axes = self.fig.add_subplot(1, 1, 1)
		self.axes.set_facecolor('#171E31')
		self.axes.spines['top'].set_color('#171E31')
		self.axes.spines['right'].set_color('#171E31')
		self.axes.spines['bottom'].set_color('#171E31')
		self.axes.spines['left'].set_color('#171E31')
		self.axes.tick_params(axis='x', colors='w', labelsize=5)
		self.axes.tick_params(axis='y', colors='w', labelsize=5)
		super(ChartCanvasDrawingWidget, self).__init__(self.fig)

		css = qstylizer.style.StyleSheet()
		css.setValues(
			backgroundColor="#171E31"
		)
		self.setStyleSheet(css.toString())


		self.__pricesBar = TPricesBarWidget(parent=self)
		self.__pricesBar.move(0, 0)



	def getPricesBar(self):
		return self.__pricesBar







#######################################################################
#
#
#
#
#
#

CHART_DATA_PERIODS = {
	"P_M1":("min", 1), "P_M5": ("min", 5), "P_M15": ("min", 15),
	"P_M30": ("min", 30), "P_H1": ("hour", 1), "P_H4": ("hour", 4), "P_D1":("day", 1)}


		




class TChartWidget(QWidget):
	"""docstring for ChartWidget"""
	def __init__(self, parent=None, _controller=None):
		super(TChartWidget, self).__init__(parent)
		
		self.parent = parent
		self.__controller = _controller

		layout = QBoxLayout(QBoxLayout.LeftToRight)
		layout.setContentsMargins(0, 0, 0, 0)
		self.setLayout(layout)


		self.setMinimumWidth(975)
		self.setMinimumHeight(350 - 10)


		self._isRunningTest = True




		#################################################################
		#
		#

		self.__observers = []
		self.__observers.append(self.__controller) # Add controller to observers
													# For choosinf test or online model
		self.__observers.append(self) 


		#
		#
		#################################################################

		#l#ayout.addWidget(QLabel("Chart View"))



		self.__chart = ChartCanvasDrawingWidget(parent=self)
		layout.addWidget(self.__chart)


		########################################
		#
		#  Will do this on observing update

		#Add the chart to the chart model
		#self.__controller.getModel(name='test').addObserver(
		#	self.__chart.getPricesBar()
		#)


		self.__chartInfos = TChartInfoWidget(parent=None, controller=self.__controller)
		layout.addWidget(self.__chartInfos)

		#The chart data widget is looking for amodel from
		#The controller
		self.__controller.addObserver(self.__chartInfos)



		css = qstylizer.style.StyleSheet()
		css.setValues(
			backgroundColor="#171E31"
		)

		self.setStyleSheet(css.toString())


		self.plot_reference = None

		

	

		


	def startAnimation(self):

		def updatePlot(i):

			model = self.__controller.getModel()

			model.addGlobalData()
			config = model.getConfig()

			d = model.getGlobalData()
			s = model.getNormalSMA()
			p = model.getPredictedSMA()
			jp = model.getPredictedJoinSMA()
			sp = model.getSmoothedPredictedSMA()
			sp_t = model.getImprovedTopSmoothedPredictedSMA()
			sp_b = model.getImprovedBottomSmoothedPredictedSMA()

			config = model.getConfig()


			#Call the model to update the plot
			self.__chart.axes.clear()


			#Prices
			self.__chart.axes.plot(
				[i for i in range(len(d)) ], d, color=config['color']['price'] #Live the price as it
			)


			"""self.__chart.axes.plot(
				[i + int(config['data']['predict']) for i in range(len(jp)) ], jp, color="red" #Live the price as it
			)"""
			

			"""self.__chart.axes.plot(
				[i + int(config['data']['predict'])/2 for i in range(len(sp)) ], sp,color="green"
			)"""

			self.__chart.axes.plot(
				[i + int(config['data']['predict']) for i in range(len(sp)) ], sp,color="green"
			)



			self.__chart.axes.plot(
				[i for i in range(len(s)) ], s,color=config['color']['SMA']
			)

			"""self.__chart.axes.plot(
				[i - 100 for i in range(len(s)) ], s,color="orange"
			)"""

			"""self.__chart.axes.plot(
				[i - 0*int( int(config['data']['predict']) /2 ) for i in range(len(s)) ], s,color="blue"
			)"""

			"""self.__chart.axes.plot(
				[i + 100 for i in range(len(p)) ], p,color='orange'
			)"""
			
			"""self.__chart.axes.plot(
				[i  + 1 * int( int(config['data']['predict']) /2 ) for i in range(len(p)) ], p,color=config['color']['P_SMA']
			)"""

			"""self.__chart.axes.plot(
				[i  + int( int(config['data']['predict']) ) for i in range(len(sp_b)) ], sp_b,color=config['color']['P_SMA']
			)
			self.__chart.axes.plot(
				[i  + int( int(config['data']['predict']) ) for i in range(len(sp_t)) ], sp_t,color=config['color']['P_SMA']
			)"""



			self.__chart.axes.set_xlim(
				left=max(0, len(model.getGlobalData()) - 5*int(config['data']['predict'])),
				right=len(model.getGlobalData()) + 2*int( int(config['data']['predict'])) )

		#Check if we are on test
		if self.__controller._modelCaller == 'test':
			self.__anim = animation.FuncAnimation(self.__chart.fig, updatePlot, interval=100)
			self .__chart.draw()

		else:
			self.__anim = animation.FuncAnimation(self.__chart.fig, updatePlot, interval=60000)
			self .__chart.draw()


	def startTestAnimation(self):
		pass

	def startOnlineAnimation(self):
		pass

	def stopAnimation(self):

		try:
			self.__anim.event_source.stop()
			self.__chart.axes.clear()

			self.__controller.getModel().resetPlotData()

			#Notify that the animationhas stopper
			#Notify observers for chart stopping
			self.notifyAll(msg= {'chart': 
											{'animate': 'has_stopped'}
										}
								)

		except Exception as e:
			raise e
		




	def addObserver(self, obs):
		self.__observers.append(obs)


	def notifyAll(self, msg):
		
		for observer in self.__observers:
			observer.update(msg)




	def update(self, msg):
		"""
			Message are coded as a dict
			object
			['menu']['choose_file']['correct']
		"""

		#print("\n (TChart) Get Updating messages : ", msg)

		#Handle Message
		#Check the data for a chart loading data
		if 'chart' in msg.keys():

			#Handle chart updating here

			#Search for atest case or a onternet case

			if 'test' in ( msg['chart'] ).keys():

				if msg['chart']['test']['data'] == "OK":
					self.__controller.getModel().addObserver(
						self.__chart.getPricesBar()
					)
					#Start drawing
					self.startAnimation()

			if 'animate' in ( msg['chart'] ).keys():
				if msg['chart']['animate'] == "stop":
					#Start drawing
					self.stopAnimation()
				



"""
app = QApplication(sys.argv)

screen = TChartWidget()
screen.show()

sys.exit(app.exec_())"""