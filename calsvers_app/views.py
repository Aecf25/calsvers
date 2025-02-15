from django.shortcuts import render
from rest_framework import generics
from .models import UserModel
from .serializer import UserSerializer

class UserList(generics.ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

class UserDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer