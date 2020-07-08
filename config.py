import os

GOOGLE_API_KEY = 'AIzaSyAQgzsxS1Qlzo_kX2nuSE7QP5WKYa_HBkU'
GOOGLE_API_URL = 'https://maps.googleapis.com/maps/api/geocode/json'

WIKI_API_URL = "https://fr.wikipedia.org/w/api.php"
WIKI_PARAMS = "action=query&prop=extracts\
		&list=geosearch&gsradius=10000&gslimit=10&format=json&gscoord="

#WIKI_PARAMS = "action=query&format=json&list=geosearch&gsradius=10000&gslimit=10&gscoord="
# doc sur : https://www.mediawiki.org/wiki/API:Nearby_places_viewer
