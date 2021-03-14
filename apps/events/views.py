from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from . models import event, session
from .serializers import eventSerializer, sessionSerializer

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.decorators import api_view


class JSONResponse(HttpResponse):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index.html'

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content,**kwargs)

def index(request):
    return HttpResponse('<h3>Welcome to Event API</h3>')
    # return render(request,"apps/events/index.html")

@api_view(['GET'])
def events(request):
        events = event.objects.all()
        serializer = eventSerializer(events, many=True)
        return Response(serializer.data)

   
@api_view(['GET'])
def sessions(request):
        sessions = session.objects.all()
        serializer = sessionSerializer(sessions, many=True)
        return Response(serializer.data)
    
