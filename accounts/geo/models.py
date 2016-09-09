from django.db import models

from agencies.models import StaffingAgency


class Country(models.Model):
    name = models.CharField(max_length=50)
    alpha_2_code = models.CharField("Alpha-2 code", max_length=2, unique=True)
    alpha_3_code = models.CharField("Alpha-3 code", max_length=3, unique=True)
    numeric_code = models.PositiveSmallIntegerField("Numeric code", max_length=3, unique=True)
    order = models.SmallIntegerField(max_length=3)
    agency = models.ForeignKey(StaffingAgency)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['order']
        verbose_name_plural = 'Countries'


class State(models.Model):
    name = models.CharField(max_length=50)
    country = models.ForeignKey(Country)
    agency = models.ForeignKey(StaffingAgency)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']


class County(models.Model):
    name = models.CharField(max_length=50)
    state = models.ForeignKey(State)
    agency = models.ForeignKey(StaffingAgency)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Counties'


class City(models.Model):
    name = models.CharField(max_length=50)
    country = models.ForeignKey(Country)
    agency = models.ForeignKey(StaffingAgency)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Cities'