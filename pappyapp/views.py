from flask import Flask, render_template, url_for, request, jsonify
from datetime import datetime
from .wiki_utils import *
from .google_utils import *
import json
import requests

app = Flask(__name__)

app.config.from_object('config')

@app.route('/')
@app.route('/index/')
def index():
	return render_template('index.html')

@app.route('/question', methods=['GET', 'POST'])
def query():
	
    # Récupérer la question
    adress = request.form["p1"]
    # Nettoyer la question

    # Géocoder la question
    place = ApiGoogle(adress)
    geocode_result = place.geocode()

    # Interroger Wikipedia
    wiki = ApiWikimedia()
    pages = wiki.ask_by_gps(geocode_result)
    	
    response = "Je me souviens avoir visité un endroit vers " + geocode_result["city"] +".<BR>" \
                "Il y a plein de chose à voir à moins de " \
                "10 km de cet endroit, par exemple : <BR><BR>"
		
    for v in pages:
        page = ApiWikimedia()
        pageUrl = page.ask_by_pageid(v['pageid'])
        response += str(v['title']).split(',')[0] + "<a href='"+pageUrl+"' target=_blanck> (Voir)</a><BR>"

    return {
        "response": response,
        "lat": geocode_result['lat'],
        "lng": geocode_result['lng']
    }

if __name__ == "__main__":
    app.run()
