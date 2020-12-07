##########################################################################
#
#
#   Several time requests will be in JSON format
#  
#    
#
########################################################################




import requests


class TJsonHandler(object):
	"""docstring for TJsonHandler"""
	def __init__(self):
		super(TJsonHandler, self).__init__()
		

	@staticmethod
	def injectJson(url, payload, action="post"):
		"""
			Post a json request

			default @action is post
			
			@url : not null
			@payload can't be null

		"""
		try:
			response = None

			if action == "post":
				response = requests.post(url, json=payload)
			elif action == "get":
				response = requests.get(url, json=payload)

			else:
				raise Exception("action is only 'get' or 'post'")
			
			return response

		except Exception as e:
			raise e

"""
url = "http://127.0.0.1:8000/check_user"

p =  TJsonHandler.injectJson(url=url, payload={"email": "xam@gmail.com", "name": "max", "key":"ze" }, action="get") 
print(p.text)

"""		
		