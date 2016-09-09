from django import forms

from mptt.forms import TreeNodeMultipleChoiceField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, HTML

from temps.models import Temp, AssignmentRestriction, ACHBankAccount, PayCardAccount, Adjustment, AdjustmentRule
from temps.models import InterestCode


class TempForm(forms.ModelForm):
    interest_codes = TreeNodeMultipleChoiceField(queryset=InterestCode.objects.all())

    def __init__(self, *args, **kwargs):
        super(TempForm, self).__init__(*args, **kwargs)
        self.fields['ssn'].required = True
        self.fields['branch'].label = 'Branches'
        self.fields['interest_codes'].widget.attrs['class'] = 'chosen-select'
        self.fields['interest_codes'].widget.attrs['style'] = 'width:350px'
        self.fields['interest_codes'].widget.attrs['tabindex'] = '4'

    class Meta:
        model = Temp
        fields = ('ssn', 'federal_exemptions', 'state_exemptions', 'branch', 'interest_codes')


class TransportationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TransportationForm, self).__init__(*args, **kwargs)
        self.fields['license_expire'].widget.attrs['class'] = 'date-picker'
        self.fields['license_expire'].widget.attrs['data-date-format'] = 'yyyy-mm-dd'

    class Meta:
        model = Temp
        fields = ('transportation_available', 'transportation_type', 'transportation_details', 'license_state', 'license_number', 'license_class', 'dmv_check', 'license_expire')


class AssignmentRestrictionForm(forms.ModelForm):
    def clean_employee_dna_customer(self):
        employee_dna_customer = self.cleaned_data.get('employee_dna_customer')
        customer_dna_employee = self.cleaned_data.get('customer_dna_employee')

        if employee_dna_customer is not True and customer_dna_employee is not True:
            raise forms.ValidationError('Must specify either Employee or Customer initiating this restriction.')

        return employee_dna_customer

    # Causes validation error when only EmployeeDNACustomer is selected!
    # def clean_customer_dna_employee(self):
    #     customer_dna_employee = self.cleaned_data.get('customer_dna_employee')
    #     employee_dna_customer = self.cleaned_data.get('employee_dna_customer')
    #
    #     print customer_dna_employee
    #     print employee_dna_customer
    #
    #     if employee_dna_customer is not True and customer_dna_employee is not True:
    #         raise forms.ValidationError('')
    #
    #     return customer_dna_employee

    class Meta:
        model = AssignmentRestriction
        fields = ('description', 'all_departments', 'customer_dna_employee', 'employee_dna_customer', 'branch')


class ElectronicPaymentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ElectronicPaymentForm, self).__init__(*args, **kwargs)
        self.fields['activate_electronic_payments'].widget.attrs['class'] = 'ace ace-switch ace-switch-5'

    class Meta:
        model = Temp
        fields = ('activate_electronic_payments', 'electronic_payment_method')


class ACHBankAccountForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ACHBankAccountForm, self).__init__(*args, **kwargs)
        self.fields['pre_note_sent'].widget.attrs['class'] = 'date-picker'
        self.fields['pre_note_sent'].widget.attrs['data-date-format'] = 'yyyy-mm-dd'
        self.fields['pre_note_approved'].widget.attrs['class'] = 'date-picker'
        self.fields['pre_note_approved'].widget.attrs['data-date-format'] = 'yyyy-mm-dd'
        self.fields['pre_note_disapproved'].widget.attrs['class'] = 'date-picker'
        self.fields['pre_note_disapproved'].widget.attrs['data-date-format'] = 'yyyy-mm-dd'

    class Meta:
        model = ACHBankAccount
        exclude = ('user',)


class PayCardAccountForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PayCardAccountForm, self).__init__(*args, **kwargs)
        self.fields['account_number'].name = 'something'

        self.fields['expiry_date'].widget.attrs['class'] = 'date-picker'
        self.fields['expiry_date'].widget.attrs['data-date-format'] = 'yyyy-mm-dd'
        self.fields['paycard_verify_date'].widget.attrs['class'] = 'date-picker'
        self.fields['paycard_verify_date'].widget.attrs['data-date-format'] = 'yyyy-mm-dd'

    class Meta:
        model = PayCardAccount
        exclude = ('user',)


class AdjustmentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AdjustmentForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.label_class = 'col-sm-4'
        self.helper.field_class = 'col-sm-6'
        self.helper.form_class = 'form-horizontal'

        self.helper.layout = Layout(
            Div(
                Div('adjustment', css_class='col-sm-6'),
                Div('note', css_class='col-sm-6'),
                css_class='row'
            ),
            Div(
                Div('description', css_class='col-sm-6'),
                Div('sequence', css_class='col-sm-6'),
                css_class='row'
            ),
            Div(
                Div('active', css_class='col-sm-offset-2 col-sm-4'),
                Div('date_served', css_class='col-sm-6'),
                css_class='row'
            ),
            Div(
                Div('frequency', css_class='col-sm-6'),
                Div('max_monthly', css_class='col-sm-6'),
                css_class='row'
            ),
            Div(
                Div('start_date', css_class='col-sm-6'),
                Div('max_yearly', css_class='col-sm-6'),
                css_class='row'
            ),
            Div(
                Div('end_date', css_class='col-sm-6'),
                Div('max_lifetime', css_class='col-sm-6'),
                css_class='row'
            ),
            Div(
                Div('authority', css_class='col-sm-6'),
                Div('period_max', css_class='col-sm-6'),
                css_class='row'
            ),
            Div(
                Div('case_number', css_class='col-sm-6'),
                Div('max_after_calc', css_class='col-sm-6'),
                css_class='row'
            ),
            Div(
                Div('deduct_greater_or_lesser', css_class='col-sm-6'),
                css_class='row'
            ),
        )

        self.fields['start_date'].widget.attrs['class'] = 'date-picker'
        self.fields['start_date'].widget.attrs['data-date-format'] = 'yyyy-mm-dd'
        self.fields['end_date'].widget.attrs['class'] = 'date-picker'
        self.fields['end_date'].widget.attrs['data-date-format'] = 'yyyy-mm-dd'
        self.fields['date_served'].widget.attrs['class'] = 'date-picker'
        self.fields['date_served'].widget.attrs['data-date-format'] = 'yyyy-mm-dd'

    class Meta:
        model = Adjustment
        exclude = ('user',)


class AdjustmentRuleForm(forms.ModelForm):
    class Meta:
        model = AdjustmentRule
        exclude = ('adjustment',)


class AdjustmentRuleFormSetHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(AdjustmentRuleFormSetHelper, self).__init__(*args, **kwargs)
        self.form_tag = False
        self.label_class = 'col-sm-2'
        self.field_class = 'col-sm-3'
        self.form_class = 'form-horizontal'

        base_layout = Layout(
            Fieldset(
                'Deduction Amount',
                'deduction_amount',
                'deduction_amount_type',
                'deduction_amount_from_total',
            ),
            Fieldset(
                'Maximum Deduction',
                'set_maximum_deduction',
                'maximum_deduction_amount',
                'maximum_deduction_amount_type',
                'maximum_deduction_from_total',
            ),
            Fieldset(
                'When to apply this rule',
                'when_to_apply',
                'when_to_apply_pay_type',
                'when_to_apply_operator',
                'when_to_apply_amount',
            ),
            Fieldset(
                'Delete Rule',
                'DELETE',
            ),
        )

        self.add_layout(base_layout)
