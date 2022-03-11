from statistics import mode
from django.db import models
from django.contrib.auth.models import User

class Detail(models.Model):
    name = models.CharField(max_length=100)
    regNO = models.IntegerField(default=0, null=False, blank=False)
    post = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    period = models.IntegerField(default=0, null=True, blank=True)
    salary = models.FloatField(default=0, null=False, blank=False)

    def __str__(self):
        return self.name