#! /usr/bin/env python
# coding: utf-8

import json
import unicodedata

class CleanQuery:
	wordlist = []
	query = []

	def __init__(self, query):
		self.strquery = query
		

		with open('pappyapp/static/files/stopwords.json') as json_data:
			self.wordlist = json.load(json_data)

	def strip_accents(self, s):
	   return ''.join(c for c in unicodedata.normalize('NFD', s)
	                  if unicodedata.category(c) != 'Mn')

	def clean(self):

		self.strquery = self.strip_accents(self.strquery)
		self.query = self.strquery.lower().split()
		queryCleaned = []

		for e in self.query:
			if e not in self.wordlist:
				queryCleaned.append(e)

		return " ".join(queryCleaned)
