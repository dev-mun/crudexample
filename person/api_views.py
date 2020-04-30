from rest_framework import viewsets, mixins
from . import models
from . import serializers
from rest_framework.permissions import IsAdminUser


# class PeopleViewset(generics.ListCreateAPIView):
#     queryset = models.Person.objects.all()
#     serializer_class = serializers.Personserializer
#
# class PersonDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = models.Person.objects.all()
#     serializer_class = serializers.

class PeopleViewset(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = models.Person.objects.all()
    serializer_class = serializers.Personserializer
    permission_classes = [IsAdminUser]

    def get(self, request):
        return self.list(request)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
