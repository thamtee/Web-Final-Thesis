from rest_framework import serializers

from consturction.models import OldConstruction

class OldConstructionSerializer(serializers.ModelSerializer):
	class Meta:
		model = OldConstruction
		fields = ('id', 'name', 'companyName', 'contractNumber', 'endDate', 'startDate', 'duration',
				  'budgets', 'engineerName', 'province', 'district', 'subDistrict', 'villageNo',
				  'street', 'etc', 'latitude', 'longitude')