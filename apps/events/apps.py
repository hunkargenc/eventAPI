from rest_framework import generics
# from rest_framework import PageNumberPagination
from rest_framework.response import Response
from .serializers import sessionSerializer, eventSerializer
from .models import session, event
# from .paginations import eventPagination

# Session API
# class sessionApi(generics.ListAPIView):
#     queryset = session.objects.all()
#     serializer_class = sessionSerializer

class sessionCreateApi(generics.CreateAPIView):
    queryset = session.objects.all()
    serializer_class = sessionSerializer
    

class sessionUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = session.objects.all()
    serializer_class = sessionSerializer

class sessionDeleteApi(generics.DestroyAPIView):
    queryset = session.objects.all()
    serializer_class = sessionSerializer

# Event API
# class eventApi(generics.ListAPIView):
#     queryset = event.objects.all()
#     serializer_class = eventSerializer

class eventCreateApi(generics.CreateAPIView):
    queryset = {event.objects.filter()}
    serializer_class = eventSerializer
    

class eventUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = {event.objects.all()}
    serializer_class = eventSerializer

class eventDeleteApi(generics.DestroyAPIView):
    queryset = event.objects.all()
    serializer_class = eventSerializer