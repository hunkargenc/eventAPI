from django.urls import path
from . import views
from apps.events.views import events, sessions
from .apps import sessionCreateApi, sessionUpdateApi, sessionDeleteApi, eventCreateApi, eventUpdateApi, eventDeleteApi

urlpatterns = [
    path('', views.index),
    path('events/', views.events),
    path('sessions/', views.sessions),
    path('sessions/create', sessionCreateApi.as_view()),
    path('sessions/<int:pk>', sessionUpdateApi.as_view()),
    path('sessions/<int:pk>/delete', sessionDeleteApi.as_view()),
    path('events/create', eventCreateApi.as_view()),
    path('events/<int:pk>', eventUpdateApi.as_view()),
    path('events/<int:pk>/delete', eventDeleteApi.as_view())
]
