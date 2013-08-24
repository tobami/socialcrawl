from socialcrawl.networks.models import Profile
from socialcrawl.networks.api import APIResponse

SUPPORTED_NETWORKS = [n[1].lower() for n in Profile.SOCIAL_NETWORKS]


def notfound(request):
    return APIResponse({'error': 'Not Found'}, status=404)


def networks(request):
    data = [{'name': n} for n in SUPPORTED_NETWORKS]
    return APIResponse(data)


def profile_list(request, network):
    if network not in SUPPORTED_NETWORKS:
        APIResponse({'error': 'Network Not Supported'}, status=404)
    else:
        network = network[0].upper()
    profiles = Profile.objects.filter(network=network)
    return APIResponse(profiles)
