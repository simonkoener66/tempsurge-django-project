"""
Note that this particular filename contain _views to avoid overriding 'temps' module containing the file!
"""

import operator
import urllib
from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from accounts.decorators import group_required
from temps.models import AssignmentRestriction, ACHBankAccount, PayCardAccount
from agencies.forms import SearchUserForm, SearchTempForm, SearchBranchForm, SearchRepForm, SearchInterestCodeForm
from accounts.forms import UserForm, ProfileForm
from temps.forms import TempForm, TransportationForm, AssignmentRestrictionForm, ElectronicPaymentForm, ACHBankAccountForm, PayCardAccountForm

@group_required('agencies')
def listing(request):
    # Search Query
    user_form = SearchUserForm(request.GET)
    temp_form = SearchTempForm(request.GET)
    rep_form = SearchRepForm(request.GET)
    branch_form = SearchBranchForm(request.GET)
    interest_code_form = SearchInterestCodeForm(request.GET)

    query = dict()

    # ID
    if request.GET.get('id'):
        query['id'] = request.GET['id']

    # First Name
    if request.GET.get('first_name'):
        query['first_name__iexact'] = request.GET['first_name']

    # Last Name
    if request.GET.get('last_name'):
        query['last_name__iexact'] = request.GET['last_name']

    # SSN
    if request.GET.get('ssn'):
        query['temp__ssn'] = request.GET['ssn']

    # Active/All Records
    if request.GET.get('active') is None or request.GET.get('active') == 'active':
        query['temp__active'] = True

    # Rep
    if request.GET.get('rep'):
        query['temp__rep'] = request.GET['rep']

    # Branch
    if request.GET.get('branch'):
        query['temp__branch__id'] = request.GET['branch']

    # Interest Code
    if request.GET.get('interest_code'):
        interest_code_seq = request.GET['interest_code'].split(',')

        interest_codes = reduce(operator.or_, (Q(temp__interest_codes__name__icontains=ic) for ic in interest_code_seq))
    else:
        interest_codes = Q()

    user_list = User.objects.filter(
        interest_codes,
        groups__name='Temps',
        userprofile__agency=request.user.userprofile.agency,
        **query
    )

    # Pagination
    paginator = Paginator(user_list, 50)

    page = request.GET.get('page')
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        users = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        users = paginator.page(paginator.num_pages)

    # Query String
    # Avoid &page=N&page=N&page=N... when going to next pages
    get_request = request.GET.copy()

    if 'page' in get_request:
        del get_request['page']

    url_encoded = urllib.urlencode(get_request)

    query_string = '?' + url_encoded

    if url_encoded:
        query_string += "&"

    if not query_string:
        query_string = '?'

    # Serve Template
    return render(request, 'agencies/temps/listing.html', {
        'users': users,
        'user_form': user_form,
        'temp_form': temp_form,
        'rep_form': rep_form,
        'branch_form': branch_form,
        'interest_code_form': interest_code_form,
        'query_string': query_string
    })


@group_required('agencies')
def show(request, identifier):
    u = get_object_or_404(User.objects.select_related('temp', 'temp__branch'), id=identifier, userprofile__agency=request.user.userprofile.agency)

    return render(
        request,
        'agencies/temps/show.html',
        {
            'user': u,
        }
    )


@group_required('agencies')
def form(request, identifier=None):
    if identifier is not None:
        u = get_object_or_404(User, pk=identifier, userprofile__agency=request.user.userprofile.agency)
        p = u.userprofile
        t = u.temp
    else:
        u = None
        p = None
        t = None

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=u)
        profile_form = ProfileForm(request.POST, request.FILES, instance=p)
        temp_form = TempForm(request.POST, instance=t)

        if user_form.is_valid() and profile_form.is_valid() and temp_form.is_valid():
            # uf = user_form.save(commit=False)
            # uf.save()

            uf = user_form.save()

            # Assign created user to Temps usergroup
            g = Group.objects.get(name='Temps')
            g.user_set.add(uf)

            pf = profile_form.save(commit=False)
            pf.agency = request.user.userprofile.agency
            pf.user = uf
            pf.save()

            tf = temp_form.save(commit=False)
            tf.user = uf

            temp_form.save_m2m()

            if not identifier:
                tf.entered_by_rep = request.user
                tf.ActivationDate = datetime.now()
                tf.DateCreated = datetime.now()

            tf.save()

            messages.success(request, 'The employee details has been successfully saved.', extra_tags="temp_saved")

            return redirect('agencies_temps_show', identifier=uf.id)
    else:
        user_form = UserForm(instance=u)
        profile_form = ProfileForm(instance=p)
        temp_form = TempForm(instance=t)

    return render(request, 'agencies/temps/form.html', {
        'user': u,
        'user_form': user_form,
        'profile_form': profile_form,
        'temp_form': temp_form,
        'identifier': identifier
    })


@group_required('agencies')
def delete(request, identifier):
    u = get_object_or_404(User, pk=identifier, userprofile__agency=request.user.userprofile.agency)
    u.delete()

    messages.success(request, 'The employee has been successfully deleted.', extra_tags="temp_deleted")

    return redirect('agencies_temps_listing')


@group_required('agencies')
def form_transportation(request, identifier):
    u = get_object_or_404(User, pk=identifier, userprofile__agency=request.user.userprofile.agency)
    p = u.userprofile
    t = u.temp

    if request.method == 'POST':
        transportation_form = TransportationForm(request.POST, instance=t)

        if transportation_form.is_valid():
            tf = transportation_form.save()

            messages.success(request, 'The employee details has been successfully saved.', extra_tags="temp_saved")

            return redirect('agencies_temps_show', identifier=tf.user.id)
    else:
        transportation_form = TransportationForm(instance=t)

    return render(request, 'agencies/temps/details/transportation/form.html', {
        'user': u,
        'profile': p,
        'temp': t,
        'transportation_form': transportation_form,
        'identifier': identifier
    })


@group_required('agencies')
def assignment_restrictions_list(request, identifier):
    u = get_object_or_404(User, pk=identifier, userprofile__agency=request.user.userprofile.agency)
    p = u.userprofile
    t = u.temp

    restrictions_by_employee = AssignmentRestriction.objects.filter(temp=u, employee_dna_customer=True)
    restrictions_by_client = AssignmentRestriction.objects.filter(temp=u, customer_dna_employee=True)

    return render(request, 'agencies/temps/details/assignment_restrictions/list.html', {
        'user': u,
        'profile': p,
        'temp': t,
        'restrictions_by_employee': restrictions_by_employee,
        'restrictions_by_client': restrictions_by_client,
    })


@group_required('agencies')
def assignment_restrictions_form(request, user_id, identifier=None, by_who=None):
    u = get_object_or_404(User, pk=user_id, userprofile__agency=request.user.userprofile.agency)
    p = u.userprofile
    t = u.temp

    if identifier is not None:
        ar = get_object_or_404(AssignmentRestriction, pk=identifier, temp__userprofile__agency=request.user.userprofile.agency)
    else:
        ar = None

    if request.method == 'POST':
        form = AssignmentRestrictionForm(request.POST, instance=ar)

        if form.is_valid():
            arf = form.save(commit=False)
            arf.temp = u
            arf.save()

            messages.success(request, 'The employee assignment restriction has been successfully saved.', extra_tags="assignment_restriction_saved")

            return redirect('agencies_temps_assignment_restrictions_list', u.id)
    else:
        initial = None

        if identifier is None:
            if by_who == 'cde':
                initial = {'customer_dna_employee': True}
            elif by_who == 'edc':
                initial = {'employee_dna_customer': True}

        form = AssignmentRestrictionForm(instance=ar, initial=initial)

    return render(request, 'agencies/temps/details/assignment_restrictions/form.html', {
        'user': u,
        'form': form,
        'identifier': identifier
    })


@group_required('agencies')
def assignment_restrictions_delete(request, identifier):
    ar = get_object_or_404(AssignmentRestriction, pk=identifier, temp__userprofile__agency=request.user.userprofile.agency)
    ar.delete()

    messages.success(request, 'The employee assignment restriction has been successfully deleted.', extra_tags="assignment_restriction_deleted")

    return redirect('agencies_temps_assignment_restrictions_list', ar.temp.id)


@group_required('agencies')
def electronic_pay_form(request, identifier):
    u = get_object_or_404(User, pk=identifier, userprofile__agency=request.user.userprofile.agency)
    p = u.userprofile
    t = u.temp

    try:
        ach = u.achbankaccount
    except ACHBankAccount.DoesNotExist:
        ach = ACHBankAccount.objects.create(user=u)

    try:
        paycard = u.paycardaccount
    except PayCardAccount.DoesNotExist:
        paycard = PayCardAccount.objects.create(user=u)

    if request.method == 'POST':
        electronicpay_form = ElectronicPaymentForm(request.POST, instance=t)
        # 'prefix' because both forms share same field names (account_number and perhaps other in the future.)
        achbankaccount_form = ACHBankAccountForm(request.POST, instance=ach, prefix="achbankaccount")
        paycardaccount_form = PayCardAccountForm(request.POST, instance=paycard, prefix="paycardaccount")

        if electronicpay_form.is_valid() and achbankaccount_form.is_valid() and paycardaccount_form.is_valid():
            electronicpay_form.save()
            achbankaccount_form.save()
            paycardaccount_form.save()

            messages.success(request, 'The employee electronic pay setup has been successfully saved.', extra_tags="electronic_pay_saved")

            return redirect('agencies_temps_show', identifier=u.id)
    else:
        electronicpay_form = ElectronicPaymentForm(instance=t)
        achbankaccount_form = ACHBankAccountForm(instance=ach, prefix="achbankaccount")
        paycardaccount_form = PayCardAccountForm(instance=paycard, prefix="paycardaccount")

    return render(request, 'agencies/temps/pay_setup/electronic_pay/form.html', {
        'user': u,
        'profile': p,
        'temp': t,
        'electronicpay_form': electronicpay_form,
        'achbankaccount_form': achbankaccount_form,
        'paycardaccount_form': paycardaccount_form,
        'identifier': identifier
    })