from django.contrib import admin
from .models import session, event

admin.site.register(session)
admin.site.register(event)