########################################################
#
#
#    Main Model
#
#
####################################################


from models.TTestChartModel import TTestChartModel
from models.TOnlineChartModel import TOnlineChartModel
from models.TNetwork.MetaTraderClient import  MQT5Client
from models.TLoginModel import TLoginModel


from views.TDialogGui.TDialogErrorWidgets import  TDialogErrorWidget



class TMainModel(object):

	def __init__(self, _db=None):
		object.__init__(self)

		self._models = {}
		self._models["chart_test"] = TTestChartModel()

		err = TDialogErrorWidget(error="Make sure MetaTrader5 is intalled and check your internet connection...")
		self._models["chart_online"] = TOnlineChartModel(mt5Client = MQT5Client(error_dialog=err))
		self._models["login"] = TLoginModel()



	def getModelByName(self, name):
		'Get a model by a name if setted'

		if name in self._models.keys():
			return self._models[name]