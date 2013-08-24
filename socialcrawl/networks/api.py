import json

from django.http import HttpResponse
from django.db.models.query import QuerySet

CONTENT_TYPE = 'application/json'


class APIResponse(HttpResponse):

    def __init__(self, message, status=200):
        if isinstance(message, QuerySet):
            blob = json.dumps(
                [obj.hydrate() for obj in message]
            )
        else:
            blob = json.dumps(message)
        super(APIResponse, self).__init__(blob,
                                          status=status,
                                          content_type=CONTENT_TYPE)
