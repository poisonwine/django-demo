from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.views import View
from .models import Message
import json

class DemoView(View):
    def get(self, request):
        """
        Get the messages that users left
        """
        data = serializers.serialize('json', Message.objects.order_by('-created_at').all())
        return HttpResponse(data, content_type='application/json')

    def post(self, request):
        """
        Post a new message
        """
        message = json.loads(request.body)['message']
        Message.objects.create(content=message)
        return HttpResponse(status=201)