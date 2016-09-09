from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from accounts.models import UserProfile, SecurityQuestion, Language
from temps.models import Temp, ACHBankAccount, PayCardAccount
from employers.models import Customer, CustomerBillingInformation, CustomerCreditPayrollInformation, CustomerMiscInformation


# Define an inline admin descriptor for UserProfile model
# which acts a bit like a singleton
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    fieldsets = [
        (None, {'fields': ['prefix', 'initial', 'nickname', 'gender', 'date_of_birth', 'phone', 'cell_phone', 'address_line_1', 'address_line_2', 'zip', 'biography', 'ip_address', 'country', 'state', 'county', 'city', 'photo', 'languages', 'admin_notes', 'agency']}),
    ]
    can_delete = False
    verbose_name_plural = 'profile'


class TempInline(admin.StackedInline):
    model = Temp
    extra = 0
    can_delete = False
    fk_name = 'user'
    verbose_name_plural = 'temp profile'

class CustomerInline(admin.StackedInline):
    model = Customer
    extra = 0
    can_delete = False
    fk_name = 'user'
    verbose_name_plural = 'customer profile'

class ACHBankAccountInline(admin.StackedInline):
    model = ACHBankAccount
    extra = 0
    can_delete = False
    fk_name = 'user'
    verbose_name_plural = 'ACH Bank Account Profile'

class PayCardAccountInline(admin.StackedInline):
    model = PayCardAccount
    extra = 0
    can_delete = False
    fk_name = 'user'
    verbose_name_plural = 'PayCard Account Profile'

class CustomerBillingInformationInline(admin.StackedInline):
    model = CustomerBillingInformation
    extra = 0
    can_delete = False
    fk_name = 'user'
    verbose_name_plural = 'Billing Information'

class CustomerCreditPayrollInformationInline(admin.StackedInline):
    model = CustomerCreditPayrollInformation
    extra = 0
    can_delete = False
    fk_name = 'user'
    verbose_name_plural = 'Credit and Payroll Information'

class CustomerMiscInformationInline(admin.StackedInline):
    model = CustomerMiscInformation
    extra = 0
    can_delete = False
    fk_name = 'user'
    verbose_name_plural = 'Misc Information'


# Define a new User admin
class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'is_activated', 'date_joined', 'last_login')
    inlines = (UserProfileInline, TempInline, CustomerInline, ACHBankAccountInline, PayCardAccountInline, CustomerBillingInformationInline, CustomerCreditPayrollInformationInline, CustomerMiscInformationInline)
    ordering = ('-date_joined',)
    date_hierarchy = 'date_joined'

    def is_activated(self, obj):
        if obj.userprofile.is_activated:
            return '<img src="/static/admin/img/icon-yes.gif" alt="Active">'
        else:
            return '<img src="/static/admin/img/icon-no.gif" alt="Inactive">'

    is_activated.allow_tags = True


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


# Security questions and answers

class SecurityQuestionAdmin(SecurityQuestion):
    class Meta:
        proxy = True
        app_label = 'auth'
        verbose_name = SecurityQuestion._meta.verbose_name
        # verbose_name_plural = SecurityQuestion._meta.verbose_name_plural


admin.site.register(SecurityQuestionAdmin)


# Display language app on it's own in Django Admin
class Language(Language):
    class Meta:
        proxy = True
        app_label = 'languages'


class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    list_editable = ('order',)


admin.site.register(Language, LanguageAdmin)