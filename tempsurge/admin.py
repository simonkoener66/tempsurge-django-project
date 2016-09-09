from django.contrib import admin

from agencies.models import StaffingAgency


class StaffingAgencyAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(StaffingAgency, StaffingAgencyAdmin)