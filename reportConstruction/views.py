from reportConstruction.models import ReportConstruction
from reportConstruction.serializer import ReportConstructionSerializer
from reportConstruction.permissions import IsOwnerOrReadOnly

from rest_framework import generics
from rest_framework import permissions

from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import ReportConstruction
from oldConstruction.models import OldConstruction

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

def map_api(request):
	report_construction_list = ReportConstruction.objects.filter(viewMap = True).values()
	old_construction_list = OldConstruction.objects.filter(viewMap = True).values()

	context = {
				'report_construction_list': report_construction_list,
				'old_construction_list': old_construction_list
				}

	return render(request, 'construction/map_api.html', context)

def google_varification(request):
	return render(request, 'construction/google86d8366632dc663e.html', {})
		