from flask import Flask, render_template, url_for, request
import googlemaps
from datetime import datetime
import requests

app = Flask(__name__)

app.config.from_object('config')

@app.route('/')
@app.route('/index/', methods=['GET', 'POST'])
def index():
	adress = "?"
	gps = "?"
	DATA = []
	geocode_result = []
	# {'address_components': [{
	# 'long_name': 'Rue de la Corvée',
	# 'short_name': 'Rue de la Corvée',
	# 'types': ['route']},
	# {'long_name': 'Torpes', 'short_name': 'Torpes', 'types': ['locality', 'political']},
	# {'long_name': 'Doubs', 'short_name': 'Doubs', 'types': ['administrative_area_level_2', 'political']},
	# {'long_name': 'Bourgogne-Franche-Comté', 'short_name': 'Bourgogne-Franche-Comté', 'types': ['administrative_area_level_1', 'political']},
	# {'long_name': 'France', 'short_name': 'FR', 'types': ['country', 'political']},
	# {'long_name': '25320', 'short_name': '25320', 'types': ['postal_code']}
	# ],
	# 'formatted_address': 'Rue de la Corvée, 25320 Torpes, France',
	# 'geometry': {'bounds': {'northeast': {'lat': 47.1693941, 'lng': 5.8921323}, 'southwest': {'lat': 47.1680562, 'lng': 5.888587}}, 'location': {'lat': 47.1683729, 'lng': 5.8901987}, 'location_type': 'GEOMETRIC_CENTER', 'viewport': {'northeast': {'lat': 47.1700741302915, 'lng': 5.8921323}, 'southwest': {'lat': 47.1673761697085, 'lng': 5.888587}}}, 
	# 'place_id': 'ChIJN9tF6LJnjUcRLN2fmdXBFIU', 
	# 'types': ['route']}]

	if 'adr' in request.form:
		adress = request.form['adr']
		gmaps = googlemaps.Client(key='AIzaSyAQgzsxS1Qlzo_kX2nuSE7QP5WKYa_HBkU')
		# Geocoding an address
		geocode_result = gmaps.geocode(adress)
		adress = geocode_result[0]['formatted_address']
		gps = geocode_result[0]['geometry']['bounds']['northeast']

		S = requests.Session()
		URL = "https://en.wikipedia.org/w/api.php"
		PARAMS = {
		    "action": "query",
		    "format": "json",
		    "list": "geosearch",
		    "gscoord": str(gps['lat']) + "|" + str(gps['lng']),
		    "gsradius": "10000",
		    "gslimit": "10"
		    }

		R = S.get(url=URL, params=PARAMS)
		DATA = R.json()
		#PAGES = DATA['query']['geosearch']

		# for k, v in PAGES.items():
		#     print("Latitute: " + str(v['coordinates'][0]['lat']))
		#     print("Longitude: " + str(v['coordinates'][0]['lon']))

	return render_template('index.html',param=adress, lat=gps, lng=gps, txt=DATA)	

@app.route('/result/')
def result():
	return render_template('result.html')

if __name__ == "__main__":
    app.run()