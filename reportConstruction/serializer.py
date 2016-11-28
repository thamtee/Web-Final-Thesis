from rest_framework import serializers
from django.contrib.auth.models import User

from reportConstruction.models import ReportConstruction

class ReportConstructionSerializer(serializers.ModelSerializer):
	class Meta:
		model = ReportConstruction
		fields = ('id', 'name', 'companyName', 'contractNumber', 'endDate', 'startDate', 'duration',
				  'budgets', 'engineerName', 'provice', 'district', 'subDistrict', 'villageNo',
				  'street', 'etc', 'latitude', 'longitude')
		serializers.ReadOnlyField(source='owner.username')
		owner = serializers.ReadOnlyField(source='owner.username')

class UserSerializer(serializers.ModelSerializer):
	reportConsturction = serializers.PrimaryKeyRelatedField(many=True, queryset=ReportConstruction.objects.all())

	class Meta:
		model = User
		fields = {'id', 'username', 'first_name', 'last_name', 'email','reportConsturction'}