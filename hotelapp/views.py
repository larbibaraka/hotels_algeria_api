from django.shortcuts import render

from rest_framework import generics
from .serializers import HotelSerializer
from .models import Hotel
# Create your views here.



class ListCreateHotel(generics.ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer




