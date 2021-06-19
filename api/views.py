from django.shortcuts import render
# from django.http import HttpResponse
from rest_framework import generics
from .serializers import RoomSerializer
from .models import Room

# Create your views here.
# holds all endpoints e.g website.com/endpoint

class RoomView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer