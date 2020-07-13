#! /usr/bin/env python
# coding: utf-8

import json
import requests
import config

class ApiWikimedia:
	WIKI_URL = config.WIKI_API_URL

	def search_pages_by_gps(self, gps):
		self.gps = gps
		WIKI_PARAMS = config.WIKI_PARAMS_GPS
		WIKI_PARAMS['gscoord'] = str(self.gps['lat']) + "|" + str(self.gps['lng'])

		R = requests.get(url = self.WIKI_URL, params = WIKI_PARAMS)
		data = R.json()

		return data['query']['geosearch']

	def search_data_by_pageid(self, pageid, datatype):
		self.pageid = str(pageid)

		if datatype == 'history':
			WIKI_PARAMS = config.WIKI_PARAMS_HISTORY_PAGEID
			key = 'extract'
		else:
			WIKI_PARAMS = config.WIKI_PARAMS_FULLURL_PAGEID
			key = 'fullurl'

		WIKI_PARAMS['pageids'] = self.pageid
		
		R = requests.get(url = self.WIKI_URL, params = WIKI_PARAMS)
		data = R.json()			

		return data['query']['pages'][str(self.pageid)][key]


	# def search_url_by_pageid(self, pageid):
	# 	self.pageid = str(pageid)
	# 	WIKI_URL = config.WIKI_API_URL
	# 	WIKI_PARAMS = config.WIKI_PARAMS_PAGEID + self.pageid

	# 	Rep = requests.get(url = WIKI_URL, params = WIKI_PARAMS)
	# 	data = Rep.json()

	# 	return data['query']['pages'][str(self.pageid)]['fullurl']

	# def search_history_by_pageid(self, pageid):
	# 	self.pageid = str(pageid)
	# 	WIKI_URL = config.WIKI_API_URL
	# 	WIKI_PARAMS = config.WIKI_PARAMS_HISTORY_PAGEID + self.pageid

	# 	R = requests.get(url = WIKI_URL, params = WIKI_PARAMS)
	# 	data = R.json()

	# 	return data['query']['pages'][str(self.pageid)]['extract']