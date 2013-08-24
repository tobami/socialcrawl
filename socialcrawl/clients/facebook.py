import argparse

import facepy

from socialcrawl.auth import FACEBOOK_ACCESS_TOKEN
from socialcrawl.clients.exceptions import AuthError, ProfileNotFound


class FacebookClient(object):

    def __init__(self, access_token=FACEBOOK_ACCESS_TOKEN):
        self.client = facepy.GraphAPI(access_token)
        self.network = 'F'

    def fetch_profile(self, username):
        """Returns basic profile info for the given username"""
        query = ("SELECT name,about_me,friend_count FROM user WHERE "
                 "username='{0}'".format(username))
        try:
            user = self.client.fql(query)
        except facepy.exceptions.FacepyError as e:
            if 'access token' in e.message:
                raise AuthError(e.message)
            else:
                print e.message
                raise e
        if len(user['data']) == 1:
            return {
                'name': user['data'][0]['name'],
                'description': user['data'][0]['about_me'] or '',
                'popularity': user['data'][0]['friend_count']
            }
        else:
            raise ProfileNotFound


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("username")
    args = parser.parse_args()
    client = FacebookClient()
    print client.fetch_profile(args.username)
