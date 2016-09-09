$(function () {
    // City
    var response_cache = {};

    $('#id_country').change(function() {
        var country_id = $('#id_country').val();

        if (response_cache[country_id]) {
            $("#id_city").html(response_cache[country_id]);
        } else {
            $.getJSON("/accounts/cities-of-country", {country_id: country_id},
                function(ret, textStatus) {
                    if (country_id == 1)
                        var options = '';
                    else
                        var options = '<option value="1" selected="selected">Not Selected</option>';

                    for (var i in ret) {
                        options += '<option value="' + ret[i].id + '">'
                            + ret[i].name + '</option>';
                    }
                    response_cache[country_id] = options;
                    $("#id_city").html(options);
                });
        }
    });

    // Security Question
    if ($('#id_security_question').val() == 1)
        $("#id_security_answer").prop('disabled', true);

    $('#id_security_question').change(function() {
        $("#id_security_answer").val("");

        if ($('#id_security_question').val() == 1)
            $("#id_security_answer").prop('disabled', true);
        else
            $("#id_security_answer").prop('disabled', false);
    });

     /*
    // Username
    $("#username_availability").click(function (event) {
        event.preventDefault();
        $("#checking").show();
        var username = $('#id_username').val().trim();

        if(!username.length) {
            $("#checking").hide();
            $('#username_info').html(username + 'You did not enter a username to check');
        } else {
            $.post("/accounts/check-availability", { username:username },
                function (result) {
                    $("#checking").hide();

                    if (result == "INVALID") {
                        $('#username_info').removeClass('info').addClass('error');
                        $('#username_info').html("Username format is incorrect.");
                    }
                    else if (result == 1) {
                        $('#username_info').removeClass('info').addClass('error');
                        $('#username_info').html(username + ' is unavailable');
                    } else {
                        $('#username_info').removeClass('error').addClass('info');
                        $('#username_info').html(username + ' is available');
                    }
                });
        }

    });
    */
});
