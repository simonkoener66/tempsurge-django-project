from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from accounts.decorators import group_required
from django.forms.models import modelformset_factory
from temps.models import AssignmentRestriction, Adjustment, AdjustmentRule
from temps.forms import AssignmentRestrictionForm, AdjustmentForm, AdjustmentRuleForm, AdjustmentRuleFormSetHelper


@group_required('agencies')
def adjustments_listing(request, identifier):
    u = get_object_or_404(User, pk=identifier, userprofile__agency=request.user.userprofile.agency)

    adjustments = Adjustment.objects.filter(user=u)

    return render(request, 'agencies/temps/pay_setup/adjustments/list.html', {
        'user': u,
        'adjustments': adjustments,
    })


@group_required('agencies')
def adjustments_form(request, user_id, identifier=None):
    u = get_object_or_404(User, pk=user_id, userprofile__agency=request.user.userprofile.agency)

    if identifier is not None:
        a = get_object_or_404(Adjustment, pk=identifier, user__userprofile__agency=request.user.userprofile.agency)
    else:
        a = None

    if request.method == 'POST':
        form = AdjustmentForm(request.POST, instance=a)

        if form.is_valid():
            f = form.save(commit=False)
            f.user = u
            f.save()

            return redirect('agencies_temps_pay_setup_adjustment_rules_form', u.id, f.id)
    else:
        form = AdjustmentForm(instance=a)

    return render(request, 'agencies/temps/pay_setup/adjustments/form.html', {
        'user': u,
        'form': form,
        'identifier': identifier
    })


@group_required('agencies')
def adjustments_delete(request, adjustment_id):
    a = get_object_or_404(Adjustment, pk=adjustment_id, user__userprofile__agency=request.user.userprofile.agency)
    a.delete()

    messages.success(request, 'The employee adjustment has been successfully deleted.', extra_tags="adjustment_deleted")

    return redirect('agencies_temps_pay_setup_adjustments_list', a.user.id)


@group_required('agencies')
def adjustment_rules_form(request, user_id, adjustment_id):
    u = get_object_or_404(User, pk=user_id, userprofile__agency=request.user.userprofile.agency)
    a = get_object_or_404(Adjustment, pk=adjustment_id, user__userprofile__agency=request.user.userprofile.agency)

    AdjustmentRuleFormSet = modelformset_factory(AdjustmentRule, form=AdjustmentRuleForm, extra=1, can_delete=True)

    if request.method == 'POST':
        formset = AdjustmentRuleFormSet(request.POST, queryset=AdjustmentRule.objects.filter(adjustment=a))

        if formset.is_valid():
            instances = formset.save(commit=False)

            for instance in instances:
                instance.adjustment = a
                instance.save()

            messages.success(request, 'The employee adjustment has been successfully saved.', extra_tags="adjustment_saved")

            if 'add-another-btn' in request.POST:
                return redirect('agencies_temps_pay_setup_adjustment_rules_form', u.id, a.id)
            elif 'finish-btn' in request.POST:
                return redirect('agencies_temps_pay_setup_adjustments_list', u.id)
    else:
        formset = AdjustmentRuleFormSet(queryset=AdjustmentRule.objects.filter(adjustment=a))

    adjustment_rule_helper = AdjustmentRuleFormSetHelper()

    return render(request, 'agencies/temps/pay_setup/adjustments/form_rules.html', {
        'user': u,
        'adjustment': a,
        'formset': formset,
        'adjustment_rule_helper': adjustment_rule_helper
    })