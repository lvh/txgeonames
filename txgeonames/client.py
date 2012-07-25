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
        Looks up locations fitting this postal code.

        :param countryCode: ISO 3166-1 country code, eg u"PL" for Poland
        :type countryCode: ``unicode``
        :param postalCode: Localized postal code, eg u"30-015" for Krakow
        :type postalCode: ``unicode``
        :returns: The list of locations matching this postal code.

        Upstream documentation on this method:
        http://www.geonames.org/export/web-services.html#postalCodeLookupJSON

        Returns the value for the "postalcodes" key in the response.
        """
        params = {"country": countryCode, "postalcode": postalCode}
        d = self._call("postalCodeLookupJSON", params)
        d.addCallback(operator.itemgetter("postalcodes"))
        return d
