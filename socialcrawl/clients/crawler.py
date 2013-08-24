from socialcrawl.clients.cache import CachedClient
from socialcrawl.clients.twitter import TwitterClient
from socialcrawl.clients.facebook import FacebookClient


class CachedTwitterClient(TwitterClient, CachedClient):
    pass


class CachedFacebookClient(FacebookClient, CachedClient):
    pass
