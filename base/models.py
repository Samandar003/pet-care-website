from django.db import models
import datetime
from datetime import date
from datetime import time
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Booking(models.Model):
    SERVICE = (
        ("Service 1", "Service 1"),
        ("Service 2", "Service 2"),
        ("Service 3", "Service 3"),

    )
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=50)
    reservation_date = models.DateField(default=date.today)
    reservation_time = models.TimeField(default=timezone.now)
    service = models.CharField(choices=SERVICE, max_length=200)
    def __str__(self):
        return self.name


class Newsletter(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.name

