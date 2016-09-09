// Deduction Amount
// ------------------------------

// 'Amount Type' selects
var deduction_amount_amount_type_select = $("select[name*='-deduction_amount_type']");

// Disable on load
deduction_amount_amount_type_select.each(function () {
    // If 'Amount Type' is set to 'Dollars'
    if ($(this).val() == 'd') {
        // Disable next 'Deduct from total' select & reset it value
        $(this).closest("div.form-group").next("div.form-group").find("select[name*='-deduction_amount_from_total']").prop('disabled', true);

    }
});

// If Changed
deduction_amount_amount_type_select.change(function () {
    var next_deduct_from_total_select = $(this).closest("div.form-group").next("div.form-group").find("select[name*='-deduction_amount_from_total']")

    if ($(this).val() == 'd') {
        // Disable next 'Deduct from total' select & reset it value
        next_deduct_from_total_select.val('').prop('disabled', true);
    } else if ($(this).val() == 'p') {
        // Enable next 'Deduct from total' select
        next_deduct_from_total_select.prop('disabled', false);
    }
});

// Maximum Deduction
// ------------------------------

// Maximum Deduction: 'Set maximum deduction' checkboxes
var set_maximum_deduction_checkboxes = $("input[name*='-set_maximum_deduction']");

// If 'Set maximum deduction' is not ticked we disable Maximum Deduction: Amount, Amount Type and Deduct from total
set_maximum_deduction_checkboxes.each(function () {
    if (!$(this).is(':checked')) {
        $(this).closest("div.form-group").next("div.form-group").find("input[name*='-maximum_deduction_amount']").prop('disabled', true);
        $(this).closest("div.form-group").next("div.form-group").next("div.form-group").find("select[name*='-maximum_deduction_amount_type']").prop('disabled', true);
        $(this).closest("div.form-group").next("div.form-group").next("div.form-group").next("div.form-group").find("select[name*='-maximum_deduction_from_total']").prop('disabled', true);
    }
});

// If Changed
set_maximum_deduction_checkboxes.change(function () {
    if (this.checked) {
        // Enable next three inputs
        $(this).closest("div.form-group").next("div.form-group").find("input[name*='-maximum_deduction_amount']").prop('disabled', false);
        $(this).closest("div.form-group").next("div.form-group").next("div.form-group").find("select[name*='-maximum_deduction_amount_type']").prop('disabled', false);
        $(this).closest("div.form-group").next("div.form-group").next("div.form-group").next("div.form-group").find("select[name*='-maximum_deduction_from_total']").prop('disabled', false);
    } else {
        // Disable next three inputs
        $(this).closest("div.form-group").next("div.form-group").find("input[name*='-maximum_deduction_amount']").val('').prop('disabled', true);
        $(this).closest("div.form-group").next("div.form-group").next("div.form-group").find("select[name*='-maximum_deduction_amount_type']").val('').prop('disabled', true);
        $(this).closest("div.form-group").next("div.form-group").next("div.form-group").next("div.form-group").find("select[name*='-maximum_deduction_from_total']").val('').prop('disabled', true);
    }
});

// When to apply this rule
// ------------------------------

// 'When to apply' selects
var when_to_apply_this_rule_select = $("select[name*='-when_to_apply']");

// Disable on load
when_to_apply_this_rule_select.each(function () {
    // If 'When to apply' is set to 'Always apply this rule'
    if ($(this).val() == 'a') {
        // Disable next three inputs
        $(this).closest("div.form-group").next("div.form-group").find("select[name*='-when_to_apply_pay_type']").val('').prop('disabled', true);
        $(this).closest("div.form-group").next("div.form-group").next("div.form-group").find("select[name*='-when_to_apply_operator']").val('').prop('disabled', true);
        $(this).closest("div.form-group").next("div.form-group").next("div.form-group").next("div.form-group").find("input[name*='-when_to_apply_amount']").val('').prop('disabled', true);
    }
});

// If Changed
when_to_apply_this_rule_select.change(function () {
    var when_to_apply_pay_type = $(this).closest("div.form-group").next("div.form-group").find("select[name*='-when_to_apply_pay_type']");
    var when_to_apply_operator = $(this).closest("div.form-group").next("div.form-group").next("div.form-group").find("select[name*='-when_to_apply_operator']");
    var when_to_apply_amount = $(this).closest("div.form-group").next("div.form-group").next("div.form-group").next("div.form-group").find("input[name*='-when_to_apply_amount']");

    if ($(this).val() == 'a') {
        // Disable next 'Deduct from total' select & reset it value
        when_to_apply_pay_type.val('').prop('disabled', true);
        when_to_apply_operator.val('').prop('disabled', true);
        when_to_apply_amount.val('').prop('disabled', true);
    } else if ($(this).val() == 'c') {
        // Enable next 'Deduct from total' select
        when_to_apply_pay_type.prop('disabled', false);
        when_to_apply_operator.prop('disabled', false);
        when_to_apply_amount.prop('disabled', false);
    }
});