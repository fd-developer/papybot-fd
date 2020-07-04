from flask import Flask, render_template, url_for, request, jsonify
from datetime import datetime
from .wiki_utils import *
from .google_utils import *
import json
import googlemaps

app = Flask(__name__)

app.config.from_object('config')

@app.route('/')
@app.route('/index/')
def index():
	return render_template('index.html')

@app.route('/question', methods=['GET', 'POST'])
def query():	
	gps = "??"
	response = ""

	# Récupérer la question
	adress = request.form["query-text-form"]
	# Nettoyer la question

	# Géocoder la question
	#gps = ApiGoogle.geocode(adress)
	gmaps = googlemaps.Client(key='AIzaSyAQgzsxS1Qlzo_kX2nuSE7QP5WKYa_HBkU')
	geocode_result = gmaps.geocode(adress)

	if geocode_result:
	 	adress = geocode_result[0]['formatted_address']
	 	gps = geocode_result[0]['geometry']['bounds']['northeast']

		# Interroger Wikipedia
		# pages = ask_wikipedia_by_gps(gps)
			
		# 	response += "Voici la liste des 10 premières villes à moins de 10 km de " + adress + " : "
			
		# 	for v in pages:
		# 		#response += str(v['title']) + " : " + str(ask_wikipedia_by_title(str(v['title']))) + " : "
		# 		response += str(v['title']).split(',')[0] + ", "
		# else:
		# 	response = "Je n'ai pas trouvé d'information pertinente sur " + adress

	return {
             "adress": adress,
             "response": gps
         }

if __name__ == "__main__":
    app.run()
