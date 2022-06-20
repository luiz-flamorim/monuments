from django.shortcuts import render
from spmap.models import Monument
from django.contrib.auth.models import User
from spmap.serializers import UserSerializer, MonumentSerializer, MonumentGeneric
from rest_framework import generics, permissions, viewsets
from spmap.permissions import IsOwnerOrReadOnly

class MonumentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Monument.objects.all()
    serializer_class = MonumentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    
    def get_serializer_class(self):
        if self.request.user.is_authenticated:
            return MonumentSerializer
        else:
            return MonumentGeneric
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
    # https://www.django-rest-framework.org/api-guide/viewsets/
    # class UserViewSet(viewsets.ViewSet):

    # def list(self, request):
    #     pass

    # def create(self, request):
    #     pass

    # def retrieve(self, request, pk=None):
    #     pass

    # def update(self, request, pk=None):
    #     pass

    # def partial_update(self, request, pk=None):
    #     pass

    # def destroy(self, request, pk=None):
    #     pass
    
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer