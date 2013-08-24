from socialcrawl.networks.models import Profile
from socialcrawl.networks.api import APIResponse


def notfound(request):
    return APIResponse({'error': 'Not Found'}, status=404)


def networks(request):
    data = [
        {'name': n[1].lower()} for n in Profile.SOCIAL_NETWORKS
    ]
    return APIResponse(data)
