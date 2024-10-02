# users/views.py
from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny
from .models import User  # Import the custom User model

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]  
    serializer_class = UserSerializer
