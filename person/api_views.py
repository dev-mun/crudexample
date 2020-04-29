from rest_framework import viewsets
from . import models
from . import serializers


class PeopleViewset(viewsets.ModelViewSet):
    queryset = models.Person.objects.all()
    serializer_class = serializers.Personserializer

#lass PeopleViewSet(mixins.Li)
