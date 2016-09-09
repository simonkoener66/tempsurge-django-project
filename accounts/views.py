from datetime import timedelta
import json

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.http import is_safe_url
from django.contrib.auth import login, authenticate, logout
from django.utils.encoding import smart_text
from django.views.decorators.csrf import csrf_exempt

from accounts.forms import LoginForm, PasswordRecoveryForm, PasswordResetForm, UserUpdateForm, ProfileForm
from accounts.decorators import group_required
from geo.models import City
from tempsurge.utils.Email import send_email
from tempsurge.utils.StringHelper import random_string


def sign_in(request):
    if request.user.is_authenticated():
        # return redirect('/')
        return _redirect_to_group_dashboard(request)

    # redirect_to = request.REQUEST.get("next", "/")
    invalid_credentials = False

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            # Ensure the user-originating redirection url is safe.
            # if not is_safe_url(url=redirect_to, host=request.get_host()):
            #     redirect_to = settings.LOGIN_REDIRECT_URL

            username = request.POST['username']
            password = request.POST['password']

            u = authenticate(username=username, password=password)

            if u is not None:
                p = u.get_profile()

                if not u.is_active:
                    # Return a 'disabled account' error message
                    return render(request, "accounts/message.html", {
                        'app': "accounts",
                        'connotation': "danger",
                        'message': "This account has been suspended. This may be caused by either a violation of the Terms of Use or for verification purposes."
                    })
                elif not p.is_activated:
                    # Return a 'account not activated' error message
                    return render(request, "accounts/message.html", {
                        'app': "accounts",
                        'connotation': "warning",
                        'message': "This account has not been activated yet. Please check your email to find the activation instructions."
                    })
                else:
                    login(request, u)

                    # return redirect(redirect_to)
                    return _redirect_to_group_dashboard(request)
            else:
                # Return an 'invalid login' error message.
                invalid_credentials = True
    else:
        form = LoginForm()

    return render(request, "accounts/login.html", {
        'form': form, 'invalid_credentials': invalid_credentials
    })


def _redirect_to_group_dashboard(request):
    group = str(request.user.groups.all()[0])

    if group == 'Agencies':
        return redirect('/agencies/dashboard/')
    elif group == 'Employer Admin' or group == 'Employer Manager':
        return redirect('/employers/dashboard/')
    elif group == 'Temps':
        return redirect('/temps/dashboard/')


def sign_out(request):
    if request.user.is_authenticated():
        logout(request)

    return redirect("/")


def recover(request):
    invalid_email = False

    if request.method == "POST":
        form = PasswordRecoveryForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']

            try:
                u = User.objects.get(email=email)

                if u.is_active:
                    p = u.get_profile()

                    p.password_reset_key = random_string(16)
                    p.password_reset_date = timezone.now()

                    p.save()

                    send_email(
                        "Password reset at Tempsurge",
                        "accounts/emails/recover",
                        settings.FROM_EMAIL,
                        u.email,
                        {'password_reset_url': "http://tempsurge.com/accounts/reset/" + str(u.id) + "/" + p.password_reset_key}
                    )

                    return render(request, "accounts/message.html", {
                        'app': "accounts",
                        'message': "Please check your email to reset your password."
                    })
                else:
                    # Return a 'disabled account' error message
                    return render(request, "accounts/message.html", {
                        'app': "accounts",
                        'connotation': "danger",
                        'message': "This account has been suspended. This may be caused by either a violation of the Terms of Use or for verification purposes."
                    })
            except User.DoesNotExist:
                # Return an 'invalid email' error message.
                invalid_email = True
    else:
        form = PasswordRecoveryForm()

    return render(request, "accounts/recover.html", {
        'form': form, 'invalid_email': invalid_email
    })


def reset(request, id, key):
    # Make sure user exists and is active, reset key not expired and the provided key is valid
    try:
        u = User.objects.get(pk=id)

        if u.is_active:
            p = u.get_profile()

            # Did the request expire?
            if p.password_reset_date < timezone.now() - timedelta(days=1):
                return render(request, "accounts/message.html", {
                    'app': "accounts",
                    'connotation': "warning",
                    'message': 'This password reset request has been expired.'
                })

            # Is the key correct?
            if p.password_reset_key != key:
                # Avoid too much duplication and details so we show a unified error for incorrect reset key and user not found
                raise User.DoesNotExist
        else:
            # Return a 'disabled account' error message
            return render(request, "accounts/message.html", {
                'app': "accounts",
                'connotation': "danger",
                'message': "This account has been suspended. This may be caused by either a violation of the Terms of Use or for verification purposes."
            })
    except User.DoesNotExist:
        return render(request, "accounts/message.html", {
            'app': "accounts",
            'connotation': "danger",
            'message': 'Invalid password reset link.'
        })

    # Validate form and reset password
    if request.method == 'POST':
        form = PasswordResetForm(request.POST, instance=u)
        if form.is_valid():
            # For an unknown reason -yet- commenting out the following line has no effect.  The password will still be saved.
            # However, commenting out p.save() below prevent the profile fields from being updated!
            form.save()

            p.password_reset_key = ""
            p.save()

            u.backend = "django.contrib.auth.backends.ModelBackend"
            login(request, u)

            return render(request, "accounts/message.html", {
                'app': "accounts",
                'connotation': "success",
                'message': 'Your password has been reset successfully. <a href="/accounts/login/">Proceed to login</a>.'
            })
    else:
        form = PasswordResetForm()

    return render(request, "accounts/reset.html", {
        'form': form
    })

@group_required('Agencies', 'Employer Admin', 'Employer Manager', 'Temps')
def profile(request):
    u = request.user
    p = u.get_profile()

    if request.method == 'POST':
        previous_email = u.email

        user_form = UserUpdateForm(request.POST, instance=u)
        profile_form = ProfileForm(request.POST, request.FILES, instance=p)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            # Check if email change was requested
            # Note: request.POST['email'] should be safe below since it's a valid email
            if u.email != request.POST['email']:
                p.new_email = request.POST['email']
                p.email_change_key = random_string(16)
                p.save()

                send_email(
                    "Action required to change your email at TempSurge",
                    "accounts/emails/email_change",
                    settings.FROM_EMAIL,
                    p.new_email,
                    {'change_email_url': "http://tempsurge.com/accounts/change-email/" + str(u.id) + "/" + p.email_change_key}
                )

                return render(request, "accounts/message.html", {
                    'app': "accounts",
                    'connotation': "warning",
                    'message': "Please check your email (%s) and follow the reactivation instructions." % p.new_email
                })

            messages.success(request, "Your profile has been successfully updated.", extra_tags="profile_updated")

            return redirect("/accounts/profile/")
    else:
        user_form = UserUpdateForm(instance=u)
        profile_form = ProfileForm(instance=p)

    return render(request, 'accounts/profile.html', {
        'user': u,
        'profile': p,
        'user_form': user_form,
        'profile_form': profile_form,
        'random': random_string()
    })


class JSONResponse(HttpResponse):
    def __init__(self, data):
        super(JSONResponse, self).__init__(
            json.dumps(data), mimetype='application/json')


@csrf_exempt
def cities_of_country(request):
    if request.is_ajax() and request.GET and 'country_id' in request.GET:
        objs = City.objects.filter(country=request.GET['country_id'])
        return JSONResponse([{'id': o.id, 'name': smart_text(o)}
                             for o in objs])
    else:
        return JSONResponse({'error': 'Not Ajax or no GET'})


@group_required('Agencies', 'Employer Admin', 'Employer Manager', 'Temps')
def settings(request):
    u = request.user
    p = u.get_profile()

    # if request.method == 'POST':
    #     previous_email = u.email
    #
    #     user_form = UserUpdateForm(request.POST, instance=u)
    #     profile_form = ProfileForm(request.POST, request.FILES, instance=p)
    #
    #     if user_form.is_valid() and profile_form.is_valid():
    #         user_form.save()
    #         profile_form.save()
    #
    #         # Check if email change was requested
    #         # Note: request.POST['email'] should be safe below since it's a valid email
    #         if u.email != request.POST['email']:
    #             p.new_email = request.POST['email']
    #             p.email_change_key = random_string(16)
    #             p.save()
    #
    #             send_email(
    #                 "Action required to change your email at TempSurge",
    #                 "accounts/emails/email_change",
    #                 settings.FROM_EMAIL,
    #                 p.new_email,
    #                 {'change_email_url': "http://tempsurge.com/accounts/change-email/" + str(u.id) + "/" + p.email_change_key}
    #             )
    #
    #             return render(request, "accounts/message.html", {
    #                 'app': "accounts",
    #                 'connotation': "warning",
    #                 'message': "Please check your email (%s) and follow the reactivation instructions." % p.new_email
    #             })
    #
    #         messages.success(request, "Your profile has been successfully updated.", extra_tags="profile_updated")
    #
    #         return redirect("/accounts/profile/")
    # else:
    #     user_form = UserUpdateForm(instance=u)
    #     profile_form = ProfileForm(instance=p)

    return render(request, 'accounts/settings.html', {
    })