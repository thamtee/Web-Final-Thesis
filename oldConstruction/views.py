from django.shortcuts import render
from oldConstrution.models import OldConstruction
from oldConstrution.serializer import OldConstructionSerializer

from rest_framework import generics
from django.contrib.auth.models import User

class OldConstructionList(generics.ListCreateAPIView):
	queryset = OldConstruction.objects.all()
	serailizer_class = OldConstructionSerializer

class OldConstructionDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = OldConstruction.objects.all()
	serailizer_class = OldConstructionSerializer
		