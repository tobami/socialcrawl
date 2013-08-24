from celery import task

from socialcrawl.clients.crawler import CachedTwitterClient, CachedFacebookClient

CLIENTS = {
    'twitter': CachedTwitterClient(),
    'facebook': CachedFacebookClient(),
}


@task()
def fetch(username, network):
    data = CLIENTS[network].fetch_profile(username)
    CLIENTS[network].save_profile(username, data)
