import json

from django.test import TestCase
from django.test.client import Client

from socialcrawl.networks.models import Profile


class BaseTest(TestCase):

    def setUp(self):
        super(BaseTest, self).setUp()
        self.client = Client()


class TestNotFound(BaseTest):

    def test_not_found(self):
        """Should return a JSON error message when URL not found"""
        resp = self.client.get('/api/badurl/')
        self.assertEqual(resp.status_code, 404)
        self.assertEqual(resp.content, json.dumps({'error': 'Not Found'}))


class TestNetworks(BaseTest):

    def test_network_list(self):
        """Should return a list of supported networks when calling /networks"""
        resp = self.client.get('/api/v1/networks')
        self.assertEqual(resp.status_code, 200)
        data = json.loads(resp.content)
        self.assertEqual(len(data), len(Profile.SOCIAL_NETWORKS))