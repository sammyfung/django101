from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Event(models.Model):
    code = models.CharField("Code", max_length=40, null=True, blank=True)
    name = models.CharField("Name", max_length=100)
    start_time = models.DateTimeField("Start Time", null=True, blank=True)
    end_time = models.DateTimeField("End Time", null=True, blank=True)
    active = models.BooleanField("Active ?", default=True)

    def __str__(self):
        return self.name


class Participant(models.Model):
    # on_delete is now required field for ForeignKey in django 2.0
    event = models.ForeignKey(Event, on_delete=models.CASCADE, verbose_name="Event")
    code = models.CharField("Code", max_length=40, null=True, blank=True)
    first_name = models.CharField("First Name", max_length=60)
    last_name = models.CharField("Last Name", max_length=60, null=True, blank=True)
    company = models.CharField("Company", max_length=100, null=True, blank=True)
    email = models.EmailField("Email", null=True, blank=True)
    phone = models.CharField("Phone", max_length=60, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name="User", null=True, blank=True)

    def __str__(self):
        if self.last_name is None or self.last_name == '':
            return self.first_name
        else:
            return "%s %s" % (self.first_name, self.last_name)

# After adding Event and Participant classes:
# 1. 'eventmgr' must be added to INSTALLED_APPS in settings.py
# 2. make migrations file for db changes and then do migrate
# ./manage.py makemigrations
# ./manage.py migrate
