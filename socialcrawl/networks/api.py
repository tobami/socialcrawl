import json

from django.http import HttpResponse

CONTENT_TYPE = 'application/json'


class APIResponse(HttpResponse):

    def __init__(self, message, status=200):
        super(APIResponse, self).__init__(json.dumps(message),
                                          status=status,
                                          content_type=CONTENT_TYPE)
