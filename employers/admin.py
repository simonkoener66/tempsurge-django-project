from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from employers.models import WorkOrder
# Register your models here.

class OrderAdmin(admin.ModelAdmin):
	list_display = ('customerdepartment', 'job_title', 'get_ordertype_shortname', 'id', 'pay_rate', 'bill_rate', 'start_date','status', 'capacity_required', 'capacity_assigned')

	def get_ordertype_shortname(self, obj):
		return obj.order_type.shortname
	get_ordertype_shortname.short_description = 'Order Type'

admin.site.register(WorkOrder, OrderAdmin)