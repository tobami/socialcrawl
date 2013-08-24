from socialcrawl.networks.models import Profile
from socialcrawl.networks.api import APIResponse

SUPPORTED_NETWORKS = [n[1].lower() for n in Profile.SOCIAL_NETWORKS]


def notfound(request):
    return APIResponse({'error': 'Not Found'}, status=404)


def networks(request):
    data = [{'name': n} for n in SUPPORTED_NETWORKS]
    return APIResponse(data)


def profiles(request, network, username=None):
    if network not in SUPPORTED_NETWORKS:
        APIResponse({'error': 'Network Not Supported'}, status=404)
    else:
        network = network[0].upper()
    if username:
        try:
            data = Profile.objects.get(username=username, network=network)
        except:
            raise
        return APIResponse(data)
    else:
        data = Profile.objects.filter(network=network)
        return APIResponse(data)
