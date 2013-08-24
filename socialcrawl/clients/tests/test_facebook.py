from unittest import TestCase

from socialcrawl.auth import FACEBOOK_ACCESS_TOKEN
from socialcrawl.clients.exceptions import AuthError, ProfileNotFound
from socialcrawl.clients.facebook import FacebookClient


class TestFacebook(TestCase):

    def setUp(self):
        """Sets up the facebook client"""
        self.client = FacebookClient(FACEBOOK_ACCESS_TOKEN)

    def test_bad_access_token(self):
        """Should raise AuthError when facebook access token is wrong"""
        client = FacebookClient('bad_access_token')
        self.assertRaises(AuthError, client.fetch_profile, 'zuck')

    def test_profile_not_found(self):
        """Should raise ProfileNotFound when profile does not exist on facebook
        """
        self.assertRaises(ProfileNotFound, self.client.fetch_profile, 'inexistentuser5555')

    def test_profile_found(self):
        """Should return dictionary with profile info when profile exists on facebook"""
        profile = self.client.fetch_profile('zuck')
        expected_keys = ['popularity', 'name', 'description']
        self.assertTrue(all(key in profile for key in expected_keys))
        self.assertEqual(profile['name'], u'Mark Zuckerberg')
        self.assertEqual(profile['popularity'], None)
