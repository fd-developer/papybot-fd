#! /usr/bin/env python
# coding: utf-8

"""wiki_utils module tests with mock"""

import pappyapp.wiki_utils as script
import urllib.request

def test_search_pages_by_gps(monkeypatch):
    """Test search_pages_by_gps"""
    data_search = {'pageid': 5523167, 'ns': 0, 'title': 'Château de Torpes', \
                    'lat': 47.1704778, 'lon': 5.8929861, 'dist': 130.9, 'primary': ''}

    def mockreturn(request):
        return data_search

    monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)

    assert script.ApiWikimedia().search_pages_by_gps(47.169692, 5.891695899999999)[1] == data_search