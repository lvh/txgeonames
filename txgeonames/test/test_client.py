"""
Tests for the Geonames client.
"""
import urlparse

from twisted.internet import defer
from twisted.trial import unittest

from txgeonames import client


class _ClientTestCase(unittest.TestCase):
    """
    Superclass that sets up a mocked out client.
    """
    def setUp(self):
        self.client = client.GeonamesClient()
        self.url = None

        def fakeGetPage(url):
            self.url = url
            return defer.succeed(self.response)

        self.client._getPage = fakeGetPage
        self.client._host = "testhost"


    def checkURL(self, command, expectedQueryParams):
        """
        Checks the URL that was accessed.
        """
        _, netloc, path, query, _ = urlparse.urlsplit(self.url)
        self.assertEqual(netloc, self.client._host)
        self.assertEqual(path.lstrip("/"), command)

        queryParams = dict(urlparse.parse_qsl(query))
        expectedQueryParams["username"] = self.client._username
        self.assertEqual(queryParams, expectedQueryParams)



class CallTests(_ClientTestCase):
    """
    Tests that the call method behaves correctly.
    """
    response = "[{}, {}]"

    def test_call(self):
        command, queryParams = "Command", {"x": "y"}
        d = self.client._call(command, queryParams)
        self.checkURL(command, queryParams)

        @d.addCallback
        def chekcResult(result):
            self.assertEqual(result, [{}, {}])

        return d


class PostalCodeLookupTests(_ClientTestCase):
    """
    Tests that postal code lookup works correctly.
    """
    response = """{"postalcodes": [{}, {}]}"""

    def test_lookup(self):
        countryCode, postalCode = "XX", "12345"
        d = self.client.postalCodeLookup(countryCode, postalCode)
        params = {"country": countryCode, "postalcode": postalCode}
        self.checkURL("postalCodeLookupJSON", params)

        @d.addCallback
        def checkResult(result):
            self.assertEqual(result, [{}, {}])

        return d
