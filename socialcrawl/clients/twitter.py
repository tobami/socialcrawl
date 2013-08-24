import argparse

import twython

from socialcrawl.auth import TWITTER_ACCESS_TOKEN
from socialcrawl.clients.exceptions import AuthError, ProfileNotFound


class TwitterClient(object):

    def __init__(self, access_token=TWITTER_ACCESS_TOKEN):
        self.client = twython.Twython(access_token=access_token)
        self.network = 'T'

    def fetch_profile(self, username):
        """Fetches given profile from Twitter"""
        try:
            user = self.client.show_user(screen_name=username)
        except twython.exceptions.TwythonError as e:
            if e.error_code == 401:
                raise AuthError(e)
            elif e.error_code == 404:
                raise ProfileNotFound
            else:
                raise e
        return {
            'name': user['name'],
            'description': user['description'] or '',
            'popularity': user['followers_count']
        }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("username")
    args = parser.parse_args()
    client = TwitterClient()
    print client.fetch_profile(args.username)
