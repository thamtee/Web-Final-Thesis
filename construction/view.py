from constrution.models import OldConstruction, ReportConstruction
from constrution.serializer import OldConstructionSerializer, ReportConstructionSerializer
from rest_framework import generics

class OldConstructionList(generics.ListCreateAPIView):
	queryset = OldConstruction.objects.all()
	serailizer_class = OldConstructionSerializer

class OldConstructionDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = OldConstruction.objects.all()
	serailizer_class = OldConstructionSerializer

class ReportConstructionList(generics.ListCreateAPIView):
	queryset = ReportConstruction.objects.all()
	serailizer_class = ReportConstructionSerializer

class ReportConstructionDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = ReportConstruction.objects.all()
	serailizer_class = ReportConstructionSerializer
		
		