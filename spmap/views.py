from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from spmap.serializers import MonumentSerializer
from spmap.models import Monument

class MonumentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Monument.objects.all()
    serializer_class = MonumentSerializer
