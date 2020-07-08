#! /usr/bin/env python
# coding: utf-8

import json
import requests
import config

class ApiGoogle:

    GOOGLE_URL = config.GOOGLE_API_URL
    GOOGLE_KEY = config.GOOGLE_API_KEY

    def __init__(self, adress):
        self.adress = adress

    @property
    def params_url(self):
        return {"address": self.adress.replace(" ", "+"),
                "key": self.GOOGLE_KEY}

    def geocode(self):
        reqRes = False
        lat = ""
        lng = ""
        city = "?"

        res = requests.get(self.GOOGLE_URL, params=self.params_url)

        if res.status_code == 200:
            if res.json()['status'] != 'ZERO_RESULTS':
                response = res.json()["results"][0]
                reqRes = True
                city = response['formatted_address']
                lat = response["geometry"]["location"]["lat"]
                lng = response["geometry"]["location"]["lng"]

        return {
            "reqRes": reqRes,
            "city": city,
            "lat": lat,
            "lng": lng
            }