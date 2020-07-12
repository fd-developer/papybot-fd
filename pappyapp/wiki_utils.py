#! /usr/bin/env python
# coding: utf-8

import json
import requests
import config

class ApiWikimedia:

	def search_pages_by_gps(self, gps):
		self.gps = gps
		WIKI_URL = config.WIKI_API_URL
		WIKI_PARAMS = config.WIKI_PARAMS_GPS + str(self.gps['lat']) + "|" + str(self.gps['lng'])

		R = requests.get(url = WIKI_URL, params = WIKI_PARAMS)
		data = R.json()

		return data['query']['geosearch']

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

	def search_data_by_pageid(self, pageid, datatype):
		self.pageid = str(pageid)
		WIKI_URL = config.WIKI_API_URL

		if datatype == 'history':
			WIKI_PARAMS = config.WIKI_PARAMS_HISTORY_PAGEID + self.pageid
			key = 'extract'
		else:
			WIKI_PARAMS = config.WIKI_PARAMS_PAGEID + self.pageid
			key = 'fullurl'

		R = requests.get(url = WIKI_URL, params = WIKI_PARAMS)
		data = R.json()			

		return data['query']['pages'][str(self.pageid)][key]