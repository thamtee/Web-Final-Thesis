from rest_framework import serializers
from django.contrib.auth.models import User

from reportConstruction.models import ReportConstruction

class ReportConstructionSerailizer(serializers.ModelSerializer):
	class Meta:
		model = ReportConstruction
		fields = ('id', 'name', 'companyName', 'contractNumber', 'endDate', 'startDate', 'duration',
				  'budgets', 'engineerName', 'province', 'district', 'subDistrict', 'villageNo',
				  'street', 'etc', 'latitude', 'longitude')
		serializers.ReadOnlyField(source='owner.username')

class UserSerializer(serializers.ModelSerializer):
		consturction = serializers.PrimaryKeyRalatedField(many=True, queryset=ReportConstruction.objects.all())

		class Meta:
			model = User
			fields = {'id', 'username', 'email','consturction'}