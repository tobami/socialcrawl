import unittest

from socialcrawl.auth import TWITTER_ACCESS_TOKEN
from socialcrawl.clients.exceptions import AuthError, ProfileNotFound
from socialcrawl.clients.twitter import TwitterClient


class TestTwitterClient(unittest.TestCase):

    def setUp(self):
        """Sets up the twitter client"""
        super(TestTwitterClient, self).setUp()
        self.client = TwitterClient(TWITTER_ACCESS_TOKEN)

    def test_bad_access_token(self):
        """Should raise AuthError when twitter access token is wrong"""
        client = TwitterClient('bad_access_token')
        self.assertRaises(AuthError, client.fetch_profile, 'twitter')

    def test_profile_not_found(self):
        """Should raise ProfileNotFound when profile does not exist on twitter
        """
        self.assertRaises(ProfileNotFound, self.client.fetch_profile, 'inexistentuser5555')

    def test_profile_found(self):
        """Should return dictionary with profile info when profile exists on twitter"""
        profile = self.client.fetch_profile('twitter')
        expected_keys = ['popularity', 'name', 'description']
        self.assertTrue(all(key in profile for key in expected_keys))
        self.assertEqual(profile['name'], u'Twitter')
        self.assertTrue(profile['popularity'] > 20000000)
