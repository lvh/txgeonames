from zope import interface


class IGeonamesClient(interface.Interface):
    """
    A client for the Geonames API.
    """
    def postalCodeLookup(countryCode, postalCode):
        """
        Looks up matching locations for this country and postal code.

        :param countryCode: ISO 3166-1 country code, eg u"PL" for Poland
        :type countryCode: ``unicode``
        :param postalCode: Localized postal code, eg u"30-015" for Krakow
        :type postalCode: ``unicode``
        :returns: The list of locations matching this postal code.

        Upstream documentation on this method:
        http://www.geonames.org/export/web-services.html#postalCodeLookupJSON

        Returns the value for the "postalcodes" key in the response.
        """
