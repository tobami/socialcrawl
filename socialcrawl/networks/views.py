from socialcrawl.networks.tasks import fetch
from socialcrawl.networks.models import Profile
from socialcrawl.networks.api import APIResponse

SUPPORTED_NETWORKS = [n[1].lower() for n in Profile.SOCIAL_NETWORKS]


def notfound(request):
    """JSONified 404"""
    return APIResponse({'error': 'Not Found'}, status=404)


def networks(request):
    """Returns list of supported social networks"""
    data = [{'name': n} for n in SUPPORTED_NETWORKS]
    return APIResponse(data)


def profiles(request, network, username=None):
    """Returns list or detail view for social profiles"""
    if network not in SUPPORTED_NETWORKS:
        return APIResponse({'error': 'Network Not Supported'}, status=404)
    else:
        network_key = network[0].upper()
    if username:
        try:
            data = Profile.objects.get(username=username, network=network_key)
        except Profile.DoesNotExist:
            fetch.delay(username, network)
            return APIResponse({'status': 'processing'}, 202)
        return APIResponse(data)
    else:
        data = Profile.objects.filter(network=network_key)
        return APIResponse(data)
