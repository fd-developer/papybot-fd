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

    """ Retrieve the formulary question """
    query = request.form["query_text_form"]

    """ Clean up the question """
    query = CleanQuery(query).clean()
    print(query)

    """ Geocoding the question to find GPS coordinates """
    place = ApiGoogle(query)
    place.geocode()

    if place.found:
        """ Query Wikipedia with GPS coordinates """
        response = "Je me souviens avoir visité un endroit vers <strong>" + \
            place.city + "</strong>.<br>"

        wiki = ApiWikimedia()
        pages = wiki.search_pages_by_gps(place.lat, place.lng)

        for v in pages:
            page = ApiWikimedia()
            if idPlaceFound == 0:
                """ find history of the first place """
                idPlaceFound = v['pageid']
                response += "<br>" + page.search_data_by_pageid(
                    idPlaceFound, 'history')
                otherplaces = "Il y a aussi plein d'autres choses à voir à \
                    moins de 10 km de cet endroit, par exemple : <br><br>"

            """ Addition of url places of the first 9 places close to the
            one found """
            if v['pageid'] != idPlaceFound:
                otherplaces += str(v['title']).split(',')[0] + \
                    "<a href='" + page.search_data_by_pageid(
                    v['pageid'], 'url')\
                    + "' target=_blanck> (Voir)</a><BR>"
    else:
        """ if Google don't find the place """
        response = "Je suis désolé mais je n'ai jamais visité cet endroit.<br>\
            Es-tu bien sûr que tu l'as bien écrit ?<br>\
            Si oui, je te propose de réessayer tout de suite avec un autre \
            endroit ..."

    return {
        "response": response,
        "lat": place.lat,
        "lng": place.lng,
        "otherplaces": otherplaces
    }

if __name__ == "__main__":
    app.run()
