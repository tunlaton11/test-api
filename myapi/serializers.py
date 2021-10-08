from rest_framework import serializers
from .models import Musician

class MusicianSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Musician
        fields = ('name', 'age', 'born', 'country')