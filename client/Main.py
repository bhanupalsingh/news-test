import os
import unittest

from newsapi.newsapi_client import NewsApiClient


class NewsApiClientTest(unittest.TestCase):
    def setUp(self):
        key = os.environ.get("news_api_secret")
        self.api = NewsApiClient(key)

    def test_api_top_headline(self):
        # Raise TypeError if Keyword/Phrase param is not of type str
        q = 0
        with self.assertRaises(TypeError):
            self.api.get_top_headlines(q=q)