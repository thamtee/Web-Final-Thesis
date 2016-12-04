from django.db import models


class OldConstruction(models.Model):
	create = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=30, default='')
	companyName = models.CharField(max_length=50, default='')
	contractNumber = models.CharField(max_length=30, blank=True, default='')
	endDate = models.CharField(max_length=20, default='')
	startDate = models.CharField(max_length=20, blank=True, default='')
	duration = models.CharField(max_length=20, default='')
	budgets = models.IntegerField(default=0)
	engineerName = models.CharField(max_length=30, blank=True, default='')
	category = models.CharField(max_length=30, default='')
	viewMap = models.BooleanField(default=False)

	#MARK: Address

	provice = models.CharField(max_length=30, default='')
	district = models.CharField(max_length=30, default='')
	subDistrict = models.CharField(max_length=30, default='')
	villageNo = models.CharField(max_length=10, blank=True, default='')
	street = models.CharField(max_length=30, blank=True, default='')
	etc = models.CharField(max_length=100, blank=True, default='')

	latitude = models.FloatField(default=0)
	longitude = models.FloatField(default=0)

	class Meta:
		ordering = ('create',)