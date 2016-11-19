from reportConstruction.models import ReportConstruction
from reportConstruction.serializer import ReportConstructionSerializer, UserSerializer

from rest_framework import generics
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.

class ReportConstructionList(generics.ListCreateAPIView):
	queryset = ReportConstruction.objects.all()
	serailizer_class = ReportConstructionSerializer

class ReportConstructionDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = ReportConstruction.objects.all()
	serailizer_class = ReportConstructionSerializer
		
class UserList(generics.ListAPIView):
	queryset = User.objects.all()
	serailizer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
	queryset = User.objects.all()
	serailizer_class = UserSerializer
		