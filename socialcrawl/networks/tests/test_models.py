from django.test import TestCase
from django.core.exceptions import ValidationError

from socialcrawl.networks.models import Profile


class TestModels(TestCase):

    def test_required_fields(self):
        """Should create a Profile entry when all required fields are given"""
        p = Profile(username='twitter', network='T')
        p.save()
        p = Profile.objects.get(username='twitter')
        self.assertEqual(p.username, 'twitter')
        self.assertEqual(p.network, 'T')
        self.assertEqual(p.name, u'')

    def test_missing_username(self):
        """Should raise ValidationError when creating a profile without username"""
        p = Profile(network='T')
        self.assertRaises(ValidationError, p.save)
        self.assertEqual(0, len(Profile.objects.all()))

    def test_missing_network(self):
        """Should raise ValidationError  when creating a profile without network"""
        p = Profile(username='twitter')
        self.assertRaises(ValidationError, p.save)
        self.assertEqual(0, len(Profile.objects.all()))
