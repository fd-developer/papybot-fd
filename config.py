import os

GOOGLE_API_KEY = 'AIzaSyAQgzsxS1Qlzo_kX2nuSE7QP5WKYa_HBkU'
GOOGLE_API_URL = 'https://maps.googleapis.com/maps/api/geocode/json'

WIKI_API_URL = "https://fr.wikipedia.org/w/api.php"
WIKI_PARAMS_GPS = "action=query&list=geosearch&gsradius=10000&gslimit=10&format=json&gscoord="

WIKI_PARAMS_PAGEID = "action=query&prop=info&inprop=url&format=json&pageids="

WIKI_PARAMS_HISTORY_PAGEID = "action=query&prop=extracts&format=json&exsentences=5&pageids="

# WIKI_PARAMS_PAGE = {
#     "action": "query",
#     "prop": "extracts",
#     "explaintext": 1,
#     "format": "json",
#     "formatversion": 2,
#     "exlimit": 1,
#     "exsentences": 5,
# }

#https://fr.wikipedia.org/w/api.php?action=query&list=geosearch&gsradius=10000&gslimit=10&format=json&gscoord=47.1699028015|5.89209699631
# Coordonnées GPS Mairie Torpes 25320
# Latitude : 47.1699028015. Longitude : 5.89209699631.