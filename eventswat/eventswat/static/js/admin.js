$(document).ready(function(){

    //remove text box and add select box in postevent add page for country,state and city
    if(!$('#id_country').val() && !$('#id_state').val() && !$('#id_city').val()){
        $('#id_country,#id_state,#id_city').remove();
        $('<select id="id_country" name="country"><option value="">------------</option></select>').insertAfter('.field-country label');
        $('<select id="id_state" name="state"><option value="">------------</option></select>').insertAfter('.field-state label');
        $('<select id="id_city" name="city"><option value="">------------</option></select>').insertAfter('.field-city label');

        //load country list when add page loading
        $.get('/postevent/load_country/', function(data) {
            $.each(data, function(key,value) {
                $('#id_country').append($('<option>').text(value.value).attr('value', value.label));
            });
        });

        //load list of state user select country
        $('#id_country').change(function(){
            var country= $(this).val();
            $.get('/postevent/load_state/',{ country:country }, function(data) {
                $('#id_state').empty();
                $.each(data, function(key,value) {
                    $('#id_state').append($('<option>').text(value.value).attr('value', value.label));
                });
            });
        });

        //load list of cities user select state
        $('#id_state').change(function(){
            var state= $(this).val();
            $('#id_city').empty();
            $.get('/postevent/load_city/',{ state:state }, function(data) {
                $.each(data, function(key,value) {
                    $('#id_city').append($('<option>').text(value.value).attr('value', value.label));
                });
            });
        });
    }

    //load subcategory base on categories
    $('#id_event_category').change(function(){
        var id= $(this).val();
        $.get('/postevent/admin_subcategory/', { id: id }, function(data) {
            $('#id_event_subcategory').empty();
            $('.field-event_subcategory').show();
            $.each(data, function(key,value) {
            $('#id_event_subcategory').append($('<option>').text(value.name).attr('value', value.id));
            });
        });
    });


    $('#id_subcategoryrelatedfieldvalue_set-0-subcategory_relatedfield').change(function(){
        var id = $(this).val();
        if(id == ''){
            $('#id_subcategoryrelatedfieldvalue_set-0-field_value').attr("disabled","disabled");
        }
        if(id == '1'){
            $('#id_subcategoryrelatedfieldvalue_set-0-field_value').removeAttr('disabled');
            $('#id_subcategoryrelatedfieldvalue_set-0-field_value').autocomplete({
                source: function (request, response) {
                    $.getJSON("/postevent/load_college?term=" + request.term, function (data) {
                        response($.map(data, function (value, key) {
                            return {
                                label: value.label,
                                value: value.value,
                            };
                        }));
                    });
                },
                select : function(event, ui) {
                        $('#id_subcategoryrelatedfieldvalue_set-0-field_value').val(ui.item.value);
                },
            });
        }
        else if(id == '2'){
            $('#id_subcategoryrelatedfieldvalue_set-0-field_value').autocomplete({
                source: function (request, response) {
                    $.getJSON("/postevent/load_dept?term=" + request.term, function (data) {
                        response($.map(data, function (value, key) {
                            return {
                                label: value.label,
                                value: value.value,
                            };
                        }));
                    });
                },
                select : function(event, ui) {
                        $('#id_subcategoryrelatedfieldvalue_set-0-field_value').val(ui.item.value);
                },
            });
        }

    });

    $('#id_subcategoryrelatedfieldvalue_set-1-subcategory_relatedfield').change(function(){
        var test= $('#id_subcategoryrelatedfieldvalue_set-0-subcategory_relatedfield').val();
        var id = $(this).val();
        if(id == ''){
            $('#id_subcategoryrelatedfieldvalue_set-1-field_value').attr("disabled","disabled");
        }
        if (test != id){
            if(id == '1'){
                $('#id_subcategoryrelatedfieldvalue_set-1-field_value').removeAttr('disabled');
                $('#id_subcategoryrelatedfieldvalue_set-1-field_value').autocomplete({
                    source: function (request, response) {
                        $.getJSON("/postevent/load_college?term=" + request.term, function (data) {
                            response($.map(data, function (value, key) {
                                return {
                                    label: value.label,
                                    value: value.value,
                                };
                            }));
                        });
                    },
                    select : function(event, ui) {
                            $('#id_subcategoryrelatedfieldvalue_set-1-field_value').val(ui.item.value);
                    },
                });
            }
            else if(id == '2'){
                $('#id_subcategoryrelatedfieldvalue_set-1-field_value').removeAttr('disabled');
                $('#id_subcategoryrelatedfieldvalue_set-1-field_value').autocomplete({
                    source: function (request, response) {
                        $.getJSON("/postevent/load_dept?term=" + request.term, function (data) {
                            response($.map(data, function (value, key) {
                                return {
                                    label: value.label,
                                    value: value.value,
                                };
                            }));
                        });
                    },
                    select : function(event, ui) {
                            $('#id_subcategoryrelatedfieldvalue_set-1-field_value').val(ui.item.value);
                    },
                });
            }
        }
        else{
            alert('Please select different choice');
            $('#id_subcategoryrelatedfieldvalue_set-1-field_value').attr("disabled","disabled");
        }

    });

    //foreign key plus symbol remove
    $('.field-subcategory_relatedfield .add-another').hide();

});
