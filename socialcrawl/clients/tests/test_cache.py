from datetime import datetime

from django.test import TestCase
from django.utils import timezone

from socialcrawl.networks.models import Profile
from socialcrawl.clients.cache import CachedClient


class TestCachedClient(TestCase):

    def setUp(self):
        """Sets up the cached client"""
        super(TestCachedClient, self).setUp()
        self.client = CachedClient()
        self.client.network = 'T'

    def test_get_profile_not_cached(self):
        """Should raise NotImplementedError when profile not found in DB"""
        self.assertRaises(NotImplementedError, self.client.get_profile, 'twitter')

    def test_get_profile_already_cached(self):
        """Should load from DB and not fetch from network when when profile is found in DB"""
        p = Profile(username='twitter', network='T', description='Cached in DB')
        p.save()
        profile = self.client.get_profile('twitter')
        self.assertEqual(profile['description'], u'Cached in DB')

    def test_load_profile(self):
        """Should load profile from DB when it can be found"""
        p = Profile(username='twitter', network='T', description='Cached in DB')
        p.save()
        data, timestamp = self.client.load_profile_from_db('twitter')
        self.assertEqual(data['description'], 'Cached in DB')

    def test_load_profile_not_found(self):
        """Should return None when profile not found"""
        p = Profile(username='twitter', network='F', description='Cached in DB')
        p.save()
        data, timestamp = self.client.load_profile_from_db('twitter')
        self.assertEqual(data, None)

    def test_save_profile(self):
        """Should save profile to DB when passing required arguments and fields"""
        profile_data = {'name': 'Twitter Inc.', 'description': u'foobar', 'popularity': 1}
        self.client.save_profile('twitter', profile_data)
        p = Profile.objects.get(username='twitter')
        self.assertEqual(p.description, u'foobar')

    def test_uptodate_current(self):
        """Should return True when timestamp is up-to-date"""
        self.assertTrue(self.client._uptodate(timezone.now()))

    def test_uptodate_old(self):
        """Should return False when timestamp is too old"""
        old_timestamp = timezone.make_aware(datetime(year=2013, month=5, day=30), timezone.get_default_timezone())
        self.assertFalse(self.client._uptodate(old_timestamp))
