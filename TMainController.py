########################################################
#
#
#    Main Controller
#  
#
####################################################


from controller.TChartController import TChartController
from controller.TLoginController import TLoginController


class TMainController(object):

	def __init__(self, _model=None):
		object.__init__(self)

		self._controlers = {}

		self._model = _model

		self._controlers["chart"] = TChartController(
			_models= [
						self._model.getModelByName("chart_test"),
						self._model.getModelByName("chart_online"),

					]
			)
		self._controlers["login"] = TLoginController(
			_model=self._model.getModelByName("login")
			)


	def getControllerByName(self, name):
		'Get a controler by a name if setted'

		if name in self._controlers.keys():
			return self._controlers[name]