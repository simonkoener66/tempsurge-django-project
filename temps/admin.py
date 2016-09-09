from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from temps.models import InterestCode, InterestCodeSynonym, TransportationType, AssignmentRestriction, Adjustment, AdjustmentRule, Temp

# admin.site.register(InterestCode, MPTTModelAdmin)


class InterestCodeSynonymInline(admin.StackedInline):
    model = InterestCodeSynonym
    extra = 3


class InterestCodeAdmin(MPTTModelAdmin):
    list_display = ('name',)
    inlines = (InterestCodeSynonymInline,)


admin.site.register(InterestCode, InterestCodeAdmin)


class TransportationTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(TransportationType, TransportationTypeAdmin)


class AssignmentRestrictionAdmin(admin.ModelAdmin):
    list_display = ('description', 'branch', 'temp')


admin.site.register(AssignmentRestriction, AssignmentRestrictionAdmin)


class AdjustmentRuleInline(admin.StackedInline):
    model = AdjustmentRule
    extra = 3


class AdjustmentAdmin(admin.ModelAdmin):
    list_display = ('description', 'active', 'frequency', 'adjustment')
    inlines = (AdjustmentRuleInline,)


admin.site.register(Adjustment, AdjustmentAdmin)
