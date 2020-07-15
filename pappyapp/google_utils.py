#! /usr/bin/env python
# coding: utf-8

import json
import requests
import config
import os

class ApiGoogle:

    GOOGLE_URL = config.GOOGLE_API_URL
    GOOGLE_KEY = ""
    PLACE_FOUND = False
    CITY = ""
    LAT = ""
    LNG = ""

    def __init__(self, adress):
        self.adress = adress
        self.GOOGLE_KEY = os.getenv("GOOGLE_KEY")

    @property
    def params_url(self):
        return {"address": self.adress.replace(" ", "+"),
                "key": self.GOOGLE_KEY}

    def geocode(self):
        self.PLACE_FOUND = False
        self.CITY = ""
        self.LAT = ""
        self.LNG = ""

        res = requests.get(self.GOOGLE_URL, params=self.params_url)

        if res.status_code == 200:
            if res.json()['status'] != 'ZERO_RESULTS':
                response = res.json()["results"][0]
                self.PLACE_FOUND = True
                self.CITY = response['formatted_address']
                self.LAT = response["geometry"]["location"]["lat"]
                self.LNG = response["geometry"]["location"]["lng"]

    @property
    def found(self):
        return self.PLACE_FOUND

    @property
    def city(self):
        return self.CITY

    @property
    def lat(self):
        return self.LAT

    @property
    def lng(self):
        return self.LNG

            