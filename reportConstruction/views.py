from reportConstruction.models import ReportConstruction
from reportConstruction.serializer import ReportConstructionSerializer
from reportConstruction.permissions import IsOwnerOrReadOnly

from rest_framework import generics
from rest_framework import permissions

from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.

class ReportConstructionList(generics.ListCreateAPIView):
	queryset = ReportConstruction.objects.all()
	serializer_class = ReportConstructionSerializer
	# permissions_classes = (permissions.IsAuthenticatedOrReadOnly,)

	# def perform_create(self, serializer):
	# 	serializer.save(owner=self.request.user)

class ReportConstructionDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = ReportConstruction.objects.all()
	serializer_class = ReportConstructionSerializer
	# permissions_classes = (permissions.IsAuthenticatedOrReadOnly,
                      				   # IsOwnerOrReadOnly,)
		
# class UserList(generics.ListAPIView):
# 	queryset = User.objects.all()
# 	serializer_class = UserSerializer

# class UserDetail(generics.RetrieveAPIView):
# 	queryset = User.objects.all()
# 	serializer_class = UserSerializer
		