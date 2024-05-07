from rest_framework import fields, serializers
from meteo.models import React

class ReactSerializer(serializers.ModelSerializer):
    class Meta:
        model= React
        fields =('Lieu',
                'Date',
                'temp',
                'vent',
                'precepitation',
                'humidite')

class CreateReactSerializer(serializers.ModelSerializer):
    class Meta:
        model = React
        fields =('Lieu',
                'Date',
                'temp',
                'vent',
                'precepitation',
                'humidite')