import requests

class ApiWikipedia:

	def ask_by_gps(self, gps):
		self.gps = gps

		S = requests.Session()
		URL = "https://en.wikipedia.org/w/api.php?" \
		"action=query&format=json&list=geosearch&gscoord="\
		+ str(self.gps['lat']) + "|" + str(self.gps['lng']) + "&gsradius=10000&gslimit=10"

		R = S.get(url=URL)
		data = R.json()

		return data['query']['geosearch']

	def ask_by_title(self, title):
		self.title = title

		S = requests.Session()
		URL = "https://en.wikipedia.org/wiki/" + self.title

		# URL = "https://en.wikipedia.org/w/api.php?action=parse&page="\
		# + title + "&prop=text&formatversion=2"

		R = S.get(url=URL)
		#data = R.json()

		return URL
