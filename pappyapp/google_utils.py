#! /usr/bin/env python
# coding: utf-8

import requests
import googlemaps

class ApiGoogle:

	def init(self):
		self.adress = ""
		self.gps = ""

	def geocode(self, adress):
		self.adress = adress

		gmaps = googlemaps.Client(key='AIzaSyAQgzsxS1Qlzo_kX2nuSE7QP5WKYa_HBkU')
		geocode_result = gmaps.geocode(self.adress)

		if geocode_result:
			self.adress = geocode_result[0]['formatted_address']
			self.gps = geocode_result[0]['geometry']['bounds']['northeast']

		return self.gps

	@property
	def gps(self):
		return self.gps

