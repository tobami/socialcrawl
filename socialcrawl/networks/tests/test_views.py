import json

from django.test import TestCase
from django.test.client import Client


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
