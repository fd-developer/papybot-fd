#! /usr/bin/env python
# coding: utf-8

import json
import requests
import config


class ApiWikimedia:
    WIKI_URL = config.WIKI_API_URL

    def search_pages_by_gps(self, lat, lng):
        self.lat = lat
        self.lng = lng
        WIKI_PARAMS = config.WIKI_PARAMS_GPS
        WIKI_PARAMS['gscoord'] = str(self.lat) + "|" + str(self.lng)

        R = requests.get(url=self.WIKI_URL, params=WIKI_PARAMS)
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

        R = requests.get(url=self.WIKI_URL, params=WIKI_PARAMS)
        data = R.json()

        return data['query']['pages'][str(self.pageid)][key]
