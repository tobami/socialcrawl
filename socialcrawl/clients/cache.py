from datetime import datetime, timedelta

from django.utils import timezone

from socialcrawl.settings import CACHE_MAX_AGE
from socialcrawl.networks.models import Profile


class CachedClient(object):

    def __init__(self):
        super(CachedClient, self).__init__()
        self.network = None

    def _uptodate(self, timestamp):
        """Returns True if timestamp has not expired, False otherwise"""
        if timestamp < timezone.now() - timedelta(minutes=CACHE_MAX_AGE):
            return False
        else:
            return True

    def load_profile_from_db(self, username):
        """Loads profile from DB, returns None is there is no entry"""
        try:
            p = Profile.objects.get(username=username, network=self.network)
        except Profile.DoesNotExist:
            return None, None
        data = {
            'name': p.name,
            'description': p.description,
            'popularity': p.popularity
        }
        return data, p

    def save_profile(self, username, data, cached=None):
        """Saves profile to the DB with given username and data"""
        p = Profile(
            username=username,
            network=self.network,
            name=data['name'],
            description=data['description'],
            popularity=data['popularity']
        )
        if cached:
            p.id = cached.id
        p.save()

    def get_profile(self, username):
        """Returns basic profile info for the given username
        First tries from cache, if not present or old it fetches data
        directly from twitter and caches it

        """
        data, cached = self.load_profile_from_db(username)
        if data and self._uptodate(cached.updated):
            return data
        else:
            data = self.fetch_profile(username)
            self.save_profile(username, data, cached)
            return data

    def fetch_profile(self, username):
        """To be implemented by the social network client"""
        raise NotImplementedError("You need to subclass CachedClient")
