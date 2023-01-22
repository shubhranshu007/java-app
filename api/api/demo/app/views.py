from django.shortcuts import render
from rest_framework import viewsets
from app.models import City
from app.serializers import CitySerializer

# Create your views here.
class CityViewSet(viewsets.ModelViewSet):
    queryset= City.objects.all()
    serializer_class=CitySerializer