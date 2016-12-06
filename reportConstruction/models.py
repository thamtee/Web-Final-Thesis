from django.db import models
import datetime

# Create your models here.
class ReportConstruction(models.Model):

	STATUS = (
				('W', 'Working'),
				('F', 'Finish'),
				('L', 'Leave'),
				('U', 'Unknown'),
			 )

	CONSTURCTION_TYPE = (('ถนน', 'ถนน'),
						 ('สะพาน', 'สะพาน'),
						 ('รถไฟ', 'รถไฟ'), 
						 ('อาคาร', 'อาคาร'), 
						 ('วางท่อระบายน้ำ', 'วางท่อระบายน้ำ'), 
						 ('เขื่อน', 'เขื่อน'), 
						 ('อ่างเก็บน้ำ', 'อ่างเก็บน้ำ'), 
						 ('บ่อบำบัดน้ำ', 'บ่อบำบัดน้ำ'),
						 ('คลอง', 'คลอง'),
						 )

	create = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=100, default='')
	companyName = models.CharField(max_length=50, default='')
	contractNumber = models.CharField(max_length=30, blank=True, default='')
	endDate = models.CharField(max_length=20, default='')
	startDate = models.CharField(max_length=20, blank=True, default='')
	duration = models.CharField(max_length=20, default='')
	budgets = models.IntegerField(default=0)
	engineerName = models.CharField(max_length=30, blank=True, default='')
	category = models.CharField(max_length=30, default='', choices=CONSTURCTION_TYPE)
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

	# owner = models.ForeignKey('auth.User', related_name='reportContruction', on_delete=models.CASCADE)

	status_construction = models.CharField(max_length=5, choices=STATUS, default='')

	class Meta:
		ordering = ('create',)