#! /usr/bin/env python
# coding: utf-8

import json
import unicodedata


class CleanQuery:
    wordlist = []

    def __init__(self, query):
        self.strquery = query

        with open('pappyapp/static/files/stopwords.json') as json_data:
            self.wordlist = json.load(json_data)

    def strip_accents(self, s):
        """ Remove accents from a string """
        return ''.join(c for c in unicodedata.normalize('NFD', s)
                       if unicodedata.category(c) != 'Mn')

    def clean(self):
        """ This method is used to 
            strip accents of a string
            put a string in lower caracteres
            take off words of a string found in a stop words list

            return a string without words found in stop words
        """
        self.strquery = self.strip_accents(self.strquery)
        self.query = self.strquery.lower().split()
        queryCleaned = []

        for e in self.query:
            if e not in self.wordlist:
            	queryCleaned.append(e)

        return " ".join(queryCleaned)
