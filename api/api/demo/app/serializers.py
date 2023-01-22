from rest_framework import serializers
from app.models import City

class CitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=City
        fields="__all__"