#! /usr/bin/env python
# coding: utf-8

import json
import requests
import config

class ApiWikimedia:

	def ask_by_gps(self, gps):
		self.gps = gps

		WIKI_URL = config.WIKI_API_URL
		WIKI_PARAMS = config.WIKI_PARAMS + str(self.gps['lat']) + "|" + str(self.gps['lng'])

		R = requests.get(url = WIKI_URL, params = WIKI_PARAMS)
		data = R.json()

		#return WIKI_URL+"?"+WIKI_PARAMS 
		return data['query']['geosearch']

	def ask_by_pageid(self, pageid):
		self.pageid = str(pageid)

		WIKI_URL = config.WIKI_API_URL
		WIKI_PARAMS = "action=query&prop=info&pageids="+self.pageid+"&inprop=url&format=json"

		Rep = requests.get(url = WIKI_URL, params = WIKI_PARAMS)
		data = Rep.json()

		#return WIKI_URL+"?"+WIKI_PARAMS 
		return data['query']['pages'][self.pageid]['fullurl']