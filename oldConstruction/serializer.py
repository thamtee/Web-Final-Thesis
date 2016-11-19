from rest_framework import serializers

from oldConsturction.models import OldConstruction

class OldConstructionSerializer(serializers.ModelSerializer):
	class Meta:
		model = OldConstruction
		fields = ('id', 'name', 'companyName', 'contractNumber', 'endDate', 'startDate', 'duration',
				  'budgets', 'engineerName', 'province', 'district', 'subDistrict', 'villageNo',
				  'street', 'etc', 'latitude', 'longitude')