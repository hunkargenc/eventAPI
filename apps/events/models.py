from django.db import models
from django.utils import timezone
from django.db.models.signals import pre_save


class session(models.Model):
    name = models.CharField(max_length = 100)
    startDate = models.DateTimeField(default=timezone.now)
    endDate = models.DateTimeField(default=timezone.now)
    speaker = models.CharField(max_length = 100)

    class Meta:
        verbose_name_plural = "Sessions"

    def __str__(self):
        return self.name

class event(models.Model):
    name = models.CharField(max_length = 300)
    startDate = models.DateTimeField(default=timezone.now)
    endDate = models.DateTimeField(default=timezone.now)
    timezone = models.CharField(max_length = 50)
    # sessions = models.ManyToManyField(session)
    sessions = models.ManyToManyField(session)

    class Meta:
        verbose_name_plural = "Events"

    def __str__(self):
        return self.name

def check_date(sender, instance, *args, **kwargs):
    if instance.startDate > instance.endDate:
        raise ValueError('Start date must be less than end date')

pre_save.connect(check_date, sender=event)
    