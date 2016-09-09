import datetime
import re
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.forms import extras
from accounts.models import UserProfile
from temps.models import Temp
from geo.models import City
from geo.widgets import CityChoiceWidget
from mptt.forms import TreeNodeMultipleChoiceField
from temps.models import InterestCode


class UserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(required=False, widget=forms.PasswordInput(attrs={'class': 'form-control'}), min_length=6, max_length=128)
    password_confirmation = forms.CharField(required=False, widget=forms.PasswordInput(attrs={'class': 'form-control'}), min_length=6, max_length=128)
    email = forms.EmailField(required=False, max_length=75, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password', 'email')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        username = username.lower()

        # Username can contains only alphanumeric and dashes.  This condition is check in the next if but we still need to show the exact error message.
        if not re.match("^[a-z0-9-.]*$", username):
            raise forms.ValidationError('The username can contains only alphanumeric characters and dashes')

        # This regular expression does only allow hyphens to separate sequences of one or more characters of [a-zA-Z0-9]
        # if not re.match("^[a-zA-Z0-9]+(-[a-zA-Z0-9]+)*$", username):
        #     raise forms.ValidationError('The username must not being or end with a dash and must not contain two dashes one after the other.')

        if username and User.objects.filter(username=username).exclude(pk=self.instance.id).count():
            raise forms.ValidationError('The username is already inuse.')

        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if email and User.objects.filter(email=email).exclude(pk=self.instance.id).count():
            raise forms.ValidationError('The email is already inuse.')
        return email

    def clean_password_confirmation(self):
        password = self.cleaned_data.get('password')
        password_confirmation = self.cleaned_data.get('password_confirmation')

        if password != password_confirmation:
            raise forms.ValidationError('Passwords do not match.')

        return password_confirmation


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(max_length=75, widget=forms.TextInput(attrs={'dir': 'ltr', 'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if email and User.objects.filter(email=email).exclude(pk=self.instance.id).count():
            raise forms.ValidationError('This email is inuse by another account.')

        # Check whether the email was change or not
        if self.instance.email != email:
            # To not change the email in our database until the new one is verified
            return self.instance.email

        return email

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].required = True

        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].required = True


class ProfileForm(forms.ModelForm):
    phone = forms.CharField(required=False, max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))
    address_line_1 = forms.CharField(required=False, max_length=250, widget=forms.TextInput(attrs={'class': 'form-control'}))
    address_line_2 = forms.CharField(required=False, max_length=250, widget=forms.TextInput(attrs={'class': 'form-control'}))
    biography = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 8, 'class': 'form-control'}))
    date_of_birth = forms.DateField(required=False, widget=extras.SelectDateWidget(years=range(1900, datetime.datetime.now().year + 1), attrs={'class': 'form-control'}))
    # city = forms.ModelChoiceField(City.objects, widget=CityChoiceWidget(attrs={'class': 'form-control'}), required=False)

    class Meta:
        model = UserProfile
        fields = ('initial', 'gender', 'date_of_birth', 'cell_phone', 'country', 'state', 'county', 'city', 'zip', 'address_line_1', 'address_line_2', 'phone', 'biography')
        # 'photo'

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')

        phone = re.sub(r'[-+ ]', '', phone)

        if not phone.isdigit() and phone != "":
            raise forms.ValidationError('Invalid phone format.')

        return phone

    # def clean_photo(self):
    #     photo = self.cleaned_data['photo']
    #
    #     if photo != self.instance.photo:
    #         if not photo.content_type in ['image/png', 'image/jpeg', 'image/gif']:
    #             raise forms.ValidationError('Accepted image formats are PNG, JPEG or GIF.')
    #
    #         # w, h = get_image_dimensions(photo)
    #         # if w < 150 or h < 150:
    #         #    raise forms.ValidationError('Image dimension are not valid.')
    #
    #         return photo

    # def clean_city(self):
    #     country = self.cleaned_data['country']
    #     city = self.cleaned_data['city']
    #
    #     # This is an important validation to prevent selecting a city from a different country.  The exception is raised but the specific error is not displayed which is not intended but I think this is a good bug!
    #     # city.id != 1 is to allow unselected city to be considered a valid option.
    #     if city.id != 1 and City.objects.filter(pk=city.id, country=country).count() == 0:
    #         raise forms.ValidationError('City do not belong to country.')
    #
    #     return city

    def __init__(self, *args, **kwargs):
        """
        We need access to the country field in the city widget, so we have to associate the form instance with the widget.
        """
        super(ProfileForm, self).__init__(*args, **kwargs)

        self.fields['gender'].required = False
        self.fields['date_of_birth'].required = False

        # self.fields['gender'].widget.attrs['class'] = 'form-control'
        # self.fields['city'].widget.form_instance = self
        self.fields['country'].widget.attrs['class'] = 'form-control'
        self.fields['state'].widget.attrs['class'] = 'form-control'
        self.fields['county'].widget.attrs['class'] = 'form-control'
        self.fields['city'].widget.attrs['class'] = 'form-control'


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), min_length=6, max_length=128)


class PasswordRecoveryForm(forms.Form):
    email = forms.EmailField(max_length=75, widget=forms.TextInput(attrs={'class': 'form-control'}), error_messages={'invalid': u'Enter a valid email'})


class PasswordForm(forms.ModelForm):
    password = forms.CharField(required=False, widget=forms.PasswordInput(attrs={'class': 'form-control'}), min_length=6, max_length=128)
    password_confirmation = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), min_length=6, max_length=128)

    class Meta:
        model = User
        fields = ('password',)

    def clean_password(self):
        password = self.cleaned_data.get('password')
        password = make_password(password)

        return password

    def clean_password_confirmation(self):
        password = self.cleaned_data.get('password')
        password_confirmation = self.cleaned_data.get('password_confirmation')

        # if password != password_confirmation:
        #     raise forms.ValidationError("Passwords do not match.")

        return password_confirmation


class PasswordResetForm(PasswordForm):
    def __init__(self, *args, **kwargs):
        super(PasswordResetForm, self).__init__(*args, **kwargs)
        self.fields['password'].required = True
        self.fields['password'].label = 'New Password'