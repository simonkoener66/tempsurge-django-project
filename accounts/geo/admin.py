from django.contrib import admin

from accounts.geo.models import Country, State, County, City


class CountryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'order', 'agency']}),
        ('ISO 3166-1', {'fields': ['alpha_2_code', 'alpha_3_code', 'numeric_code']}),
    ]
    list_display = ('name', 'order')
    list_editable = ('order',)
    search_fields = ['name', 'alpha_2_code', 'alpha_3_code']
    ordering = ('order',)
    list_per_page = 10

admin.site.register(Country, CountryAdmin)


class StateAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    list_filter = ['country']
    search_fields = ['name']
    ordering = ('country', 'name',)

admin.site.register(State, StateAdmin)


class CountyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']
    ordering = ('name',)

admin.site.register(County, CountyAdmin)


class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    list_filter = ['country']
    search_fields = ['name']
    ordering = ('country', 'name',)

admin.site.register(City, CityAdmin)