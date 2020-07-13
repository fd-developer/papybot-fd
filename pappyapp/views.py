from flask import Flask, render_template, url_for, request, jsonify
from .wiki_utils import *
from .google_utils import *
from .clean_query import *

app = Flask(__name__)

app.config.from_object('config')

@app.route('/')
@app.route('/index/')
def index():
	return render_template('index.html')

@app.route('/question', methods=['GET', 'POST'])
def query():
    response = ""
    idPlaceFound = 0
    otherplaces = ""	

    # Récupérer la question
    query = request.form["query_text_form"]

    # Nettoyer la question
    query = CleanQuery(query).clean()
    print(query)

    # Géocoder la question
    place = ApiGoogle(query)
    geocode_result = place.geocode()

    # Interroger Wikipedia
    response = "Je me souviens avoir visité un endroit vers <strong>" + \
    geocode_result["city"] +"</strong>.<br>"
    
    wiki = ApiWikimedia()
    pages = wiki.search_pages_by_gps(geocode_result)   

    for v in pages:
        page = ApiWikimedia()
        if idPlaceFound == 0:
            idPlaceFound = v['pageid']
            response += "<br>" + page.search_data_by_pageid(idPlaceFound,'history')
            otherplaces = "Il y a aussi plein d'autres choses à voir à moins de " \
                "10 km de cet endroit, par exemple : <br><br>"

        # Ajout des 9 premiers endroits proches de celui trouvé
        if v['pageid'] != idPlaceFound:
            otherplaces += str(v['title']).split(',')[0] + \
            "<a href='"+page.search_data_by_pageid(v['pageid'],'url')+"' target=_blanck> (Voir)</a><BR>"

    return {
        "response": response,
        "lat": str(geocode_result['lat']),
        "lng": str(geocode_result['lng']),
        "otherplaces": otherplaces
    }

if __name__ == "__main__":
    app.run()
