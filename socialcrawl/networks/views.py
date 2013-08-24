import json

from django.http import HttpResponse

CONTENT_TYPE = 'application/json'


def notfound(request):
    message = json.dumps({'error': 'Not Found'})
    return HttpResponse(message, status=404, content_type=CONTENT_TYPE)
