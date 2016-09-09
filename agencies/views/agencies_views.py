"""
Note that this particular filename contain _views to avoid overriding 'agencies' module containing the file!
"""

from django.shortcuts import render, redirect, get_object_or_404
from accounts.decorators import group_required
from temps.models import InterestCode
from agencies.forms import InterestCodeForm, InterestCodeSynonymFormset, InterestCodeSynonymFormSetHelper


@group_required('agencies')
def interest_codes_listing(request):
    nodes = InterestCode.objects.filter(agency=request.user.userprofile.agency)

    return render(request, 'agencies/interest_codes/listing.html', {
        'nodes': nodes
    })


@group_required('agencies')
def interest_codes_form(request, identifier=None):
    if identifier:
        interest_code = get_object_or_404(InterestCode, pk=identifier, agency=request.user.userprofile.agency)
    else:
        interest_code = InterestCode()

    form = InterestCodeForm(instance=interest_code)
    interest_code_synonym_formset = InterestCodeSynonymFormset(instance=interest_code)

    if request.method == 'POST':
        form = InterestCodeForm(request.POST, instance=interest_code)
        if form.is_valid():
            # Do not save the interest code unless synonyms are valid and also to assign the code to the agency when addiing it
            interest_code = form.save(commit=False)

            # Assign interest code to agency
            interest_code.agency = request.user.userprofile.agency

            interest_code_synonym_formset = InterestCodeSynonymFormset(request.POST, request.FILES, instance=interest_code)

            if interest_code_synonym_formset.is_valid():
                interest_code.save()
                interest_code_synonym_formset.save()

                return redirect('agencies_interest_codes_listing')

    interest_code_helper = InterestCodeSynonymFormSetHelper()

    return render(request, "agencies/interest_codes/form.html", {
        'identifier': identifier,
        'form': form,
        'interest_code_synonym_formset': interest_code_synonym_formset,
        'interest_code_helper': interest_code_helper,
        'action': "Create"
    })