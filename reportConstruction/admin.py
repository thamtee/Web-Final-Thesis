from django import forms
from django.contrib import admin

from .models import ReportConstruction
from oldConstruction.models import OldConstruction
# Register your models here.

class ReportAdmin(admin.ModelAdmin):
	fields = ('name', 'endDate', 'viewMap')

	ordering = ('create', )

	list_display = ('create', 'name', 'endDate', 'viewMap',)
	list_display_links = ('name', 'endDate', 'viewMap',)

	list_filter = (
					'endDate',
					'name', 
					('viewMap', admin.BooleanFieldListFilter),
					)

	empty_value_display = 'unknown'

	actions = ['make_view']

	def make_view(self, request, queryset):
		rows_updated = queryset.update(viewMap = True)
		if rows_updated == 1:
			message_bit = "1 consturction was"
		else:
			message_bit = "%s consturction were" % rows_updated
		self.message_user(request, "%s successfully marked as map." % message_bit)
	make_view.short_description = "Selected Construction to pin on map"


class OldConAdmin(admin.ModelAdmin):
	list_display = ('create', 'name', 'endDate', 'viewMap')
	list_display_links = ('name',)

	empty_value_display = 'unknown'

admin.site.register(ReportConstruction, ReportAdmin)
admin.site.register(OldConstruction, OldConAdmin)