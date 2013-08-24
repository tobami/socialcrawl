from socialcrawl.clients.crawler import CachedTwitterClient, CachedFacebookClient
from socialcrawl.networks.models import Profile
from socialcrawl.networks.api import APIResponse

SUPPORTED_NETWORKS = [n[1].lower() for n in Profile.SOCIAL_NETWORKS]

CLIENTS = {
    'twitter': CachedTwitterClient(),
    'facebook': CachedFacebookClient(),
}

def notfound(request):
    return APIResponse({'error': 'Not Found'}, status=404)


def networks(request):
    data = [{'name': n} for n in SUPPORTED_NETWORKS]
    return APIResponse(data)


def profiles(request, network, username=None):
    if network not in SUPPORTED_NETWORKS:
        return APIResponse({'error': 'Network Not Supported'}, status=404)
    else:
        network_key = network[0].upper()
    if username:
        try:
            data = Profile.objects.get(username=username, network=network_key)
        except:
            data = CLIENTS[network].get_profile(username)
        return APIResponse(data)
    else:
        data = Profile.objects.filter(network=network_key)
        return APIResponse(data)
