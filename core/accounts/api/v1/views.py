from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .serializers import (
    ProfileSerializer,
    RegisterSerializer,
)
from accounts.models import Profile, User
from rest_framework import viewsets


class RegisterModelViewSet(viewsets.ModelViewSet):
    """Creates new user with the given info and credentials"""
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class ProfileModelViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, user=self.request.user)
        return obj
