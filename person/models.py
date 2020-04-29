from django.db import models


# Create your models here.
class Person(models.Model):
    given_name = models.CharField(max_length=32)
    family_name = models.CharField(max_length=32)
    job_title = models.CharField(max_length=64, null=True)
    address = models.CharField(max_length=100)
    email_address = models.EmailField(null=True)
    telephone = models.CharField(max_length=16)

