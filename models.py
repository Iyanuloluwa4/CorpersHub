from django.db import models
from django.contrib.auth.models import User

class WebPages(models.Model):
    name = models.CharField(max_length=20)
    link = models.CharField(max_length=60, unique=True)
    date_uploaded = models.DateTimeField(unique=True)

    def __str__(self):
        return self.name

class Connect(models.Model):
    client = models.CharField(max_length=220)
    client_location = models.CharField(max_length=1000)
    job_title = models.CharField(max_length=220)
    job_description = models.TextField(max_length=2000)
    job_requirement = models.TextChoices
    due_delivery_time = models.DateTimeField()
    type_of_job = models.TextChoices
    verification_status = models.TextChoices
    link = models.CharField(max_length=60, unique=True)
    date_uploaded = models.DateTimeField(unique=True)

    def __str__(self):
        return self.client