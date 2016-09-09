from django.db import models
from django.contrib.auth.models import User
from agencies.models import StaffingAgency


class SecurityQuestion(models.Model):
    question = models.CharField(max_length=100)
    agency = models.ForeignKey(StaffingAgency)

    def __unicode__(self):
        return self.question


class Language(models.Model):
    name = models.CharField(max_length=20)
    order = models.PositiveSmallIntegerField()
    agency = models.ForeignKey(StaffingAgency)

    def __unicode__(self):
        return "%s -> %s" % (self.agency.name, self.name)

    class Meta:
        ordering = ['order']


class UserProfile(models.Model):
    prefix = models.CharField(max_length=6, blank=True, choices=(
        ('Ms', 'Ms'),
        ('Miss', 'Miss'),
        ('Mrs', 'Mrs'),
        ('Mr', 'Mr'),
    ))
    initial = models.CharField(max_length=30, blank=True)
    nickname = models.CharField(max_length=30, blank=True)
    UNSPECIFIED = 'U'
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = (
        (UNSPECIFIED, 'Unspecified'),
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=UNSPECIFIED)
    date_of_birth = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True)
    cell_phone = models.CharField(max_length=15, blank=True)
    address_line_1 = models.CharField(max_length=250, blank=True)
    address_line_2 = models.CharField(max_length=250, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    biography = models.TextField(blank=True)
    ip_address = models.IPAddressField(default="0.0.0.0", blank=True)
    is_activated = models.BooleanField(default=False)
    activation_key = models.CharField(max_length=16, blank=True)
    password_reset_key = models.CharField(max_length=16, blank=True)
    password_reset_date = models.DateTimeField(null=True, blank=True)
    new_email = models.CharField(max_length=75, blank=True)
    email_change_key = models.CharField(max_length=16, blank=True)
    admin_notes = models.TextField(blank=True)
    photo = models.ImageField(blank=True, upload_to='users')
    languages = models.ManyToManyField(Language, blank=True)
    security_answer = models.CharField(max_length=100, blank=True)
    security_question = models.ForeignKey(SecurityQuestion, default=1)
    country = models.ForeignKey('geo.Country', blank=True, null=True)
    state = models.ForeignKey('geo.State', blank=True, null=True)
    county = models.ForeignKey('geo.County', blank=True, null=True)
    city = models.ForeignKey('geo.City', blank=True, null=True)
    user = models.OneToOneField(User)
    agency = models.ForeignKey(StaffingAgency, null=True)