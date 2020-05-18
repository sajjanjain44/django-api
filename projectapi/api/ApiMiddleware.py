import json
from datetime import datetime

from django.http import HttpResponse

from projectapi import settings


class ApiMiddleware:
    def __init__(self, get_response):
        # print("get_response")
        self.get_response = get_response

    def process_request(self, request):
        # print("sajjan")
        # return HttpResponse(request)
        pass

    def __call__(self, request):
        # print(request, "sajjan")
        # data = json.loads(request.body)

        body_unicode = request.body.decode('utf-8')
        # body = json.loads(body_unicode)
        # content = body['content']
        print("-----------")
        print((request.body.username))
        print("-----------")

        request.timestamp = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        response = self.get_response(request)
        print(response)
        return response
