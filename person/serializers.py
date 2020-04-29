from rest_framework import serializers
from . import models


class Personserializer(serializers.ModelSerializer):
    class Meta:
        model = models.Person
        fields = ('given_name', 'family_name', 'job_title', 'address', 'email_address', 'telephone')
