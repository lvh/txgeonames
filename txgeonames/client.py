# -*- coding: utf-8 -*-
"""
An API client for the Geonames API.
"""
import json
import operator
import urllib
import urlparse

from twisted.web import client


class GeonamesClient(object):
    """
    A client for the Geonames API.

    See ``txgeonames.interface.IGeonamesClient``.
    """
    _host = "api.geonames.org"
    _getPage = staticmethod(client.getPage)

    def __init__(self, username=u"demo"):
        self._username = username


    def _call(self, method, params):
        params["username"] = self._username
        parts = "http", self._host, method, urllib.urlencode(params), ""
        d = self._getPage(urlparse.urlunsplit(parts))
        d.addCallback(json.loads)
        return d


    def postalCodeLookup(self, countryCode, postalCode):
        """
        Looks up locations for this country and postal code.
        """
        params = {"country": countryCode, "postalcode": postalCode}
        d = self._call("postalCodeLookupJSON", params)
        d.addCallback(operator.itemgetter("postalcodes"))
        return d
