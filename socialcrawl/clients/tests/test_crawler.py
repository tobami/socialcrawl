from django.test import TestCase

from socialcrawl.networks.models import Profile
from socialcrawl.clients.crawler import CachedTwitterClient, CachedFacebookClient


class TestCachedTwitterClient(TestCase):

    def setUp(self):
        """Sets up a cached twitter client"""
        super(TestCachedTwitterClient, self).setUp()
        self.client = CachedTwitterClient()

    def test_profile_not_cached(self):
        """Should fetch from twitter and save to DB when profile not found in DB"""
        # First Cache an object from a different network
        p = Profile(username='twitter', network='F', description='Cached in DB')
        p.save()
        profile = self.client.get_profile('twitter')
        expected_description = u'Your official source for news, updates and tips from Twitter, Inc.'
        self.assertEqual(profile['description'], expected_description)
        p = Profile.objects.get(username='twitter', network='T')
        self.assertEqual(p.name, 'Twitter')
        self.assertEqual(p.network, 'T')
        self.assertEqual(p.description, expected_description)

    def test_profile_already_cached(self):
        """Should load from DB and not fetch from Twitter when when profile is found in DB"""
        p = Profile(username='twitter', network='T', description='Cached in DB')
        p.save()
        profile = self.client.get_profile('twitter')
        self.assertEqual(profile['description'], u'Cached in DB')


class TestCachedFacebookClient(TestCase):

    def setUp(self):
        """Sets up a cached facebook client"""
        super(TestCachedFacebookClient, self).setUp()
        self.client = CachedFacebookClient()

    def test_profile_not_cached(self):
        """Should fetch from Facebook and save to DB when profile not found in DB"""
        profile = self.client.get_profile('zuck')
        expected_description = u''
        self.assertEqual(profile['description'], expected_description)
        p = Profile.objects.get(username='zuck')
        self.assertEqual(p.name, u'Mark Zuckerberg')
        self.assertEqual(p.network, 'F')
        self.assertEqual(p.description, expected_description)

    def test_profile_already_cached(self):
        """Should load from DB and not fetch from Facebook when when profile is found in DB"""
        p = Profile(username='zuck', network='F', description='Cached in DB')
        p.save()
        profile = self.client.get_profile('zuck')
        self.assertEqual(profile['description'], u'Cached in DB')
