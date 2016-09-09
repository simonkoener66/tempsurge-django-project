from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from agencies.models import CompanyType, Company, BankAccount, Branch, Authority, AdjustmentCategory, Adjustment, TimeEntry, Check


class CompanyTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


admin.site.register(CompanyType, CompanyTypeAdmin)


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Company, CompanyAdmin)


class BankAccountAdmin(admin.ModelAdmin):
    list_display = ('bank_name',)


admin.site.register(BankAccount, BankAccountAdmin)

admin.site.register(Branch, MPTTModelAdmin)


class AuthorityAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Authority, AuthorityAdmin)


class AdjustmentCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'agency')


admin.site.register(AdjustmentCategory, AdjustmentCategoryAdmin)


class AdjustmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'category', 'agency')


admin.site.register(Adjustment, AdjustmentAdmin)


class TimeEntryAdmin(admin.ModelAdmin):
	list_display = ('assignment','hours_regular', 'hours_overtime', 'bill_rate', 'pay_rate', 'status')

admin.site.register(TimeEntry, TimeEntryAdmin)

class CheckAdmin(admin.ModelAdmin):
	list_display = ('timeentry', 'checkdate')

admin.site.register(Check, CheckAdmin)
