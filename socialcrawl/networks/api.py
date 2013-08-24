import json

from django.db import models
from django.http import HttpResponse

CONTENT_TYPE = 'application/json'


class APIResponse(HttpResponse):

    def __init__(self, data, status=200):
        if isinstance(data, models.query.QuerySet):
            blob = json.dumps([obj.hydrate() for obj in data])
        elif isinstance(data, models.Model):
            blob = json.dumps(data.hydrate())
        else:
            blob = json.dumps(data)
        super(APIResponse, self).__init__(blob,
                                          status=status,
                                          content_type=CONTENT_TYPE)
