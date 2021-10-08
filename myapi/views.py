from django.shortcuts import render
from rest_framework import viewsets

from .serializers import MusicianSerializer
from .models import Musician

# Create your views here.
class MusicianViewSet(viewsets.ModelViewSet):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer