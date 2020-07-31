#! /usr/bin/env python
# coding: utf-8

import json
import requests
import config


class ApiWikimedia:
    """ this class is used to find a story to tell to the user about an
    adress """
    WIKI_URL = config.WIKI_API_URL

    def search_pages_by_gps(self, lat, lng):
        """ place is found by it's gps coordonates
        return a list of informations in a json string """
        self.lat = lat
        self.lng = lng
        WIKI_PARAMS = config.WIKI_PARAMS_GPS
        WIKI_PARAMS['gscoord'] = str(self.lat) + "|" + str(self.lng)

        R = requests.get(url=self.WIKI_URL, params=WIKI_PARAMS)
        data = R.json()

        return data['query']['geosearch']

    def search_data_by_pageid(self, pageid, datatype):
        """ this method return the history of a place or it's wikipedia url
        you must send a wikipedia pageid (found with serach_pages_by_gps() )
        you must use datatype = history the return th history else it returns
        the wikipedia url à the place """
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
