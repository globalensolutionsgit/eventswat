$(document).ready(function(){
    $('#id_event_category').change(function(){
        var id= $(this).val();
        $.get('/admin_subcategory/', { id: id }, function(data) {
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
                    $.getJSON("/getcollege?term=" + request.term, function (data) {
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
                    $.getJSON("/getdept?term=" + request.term, function (data) {
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
                        $.getJSON("/getcollege?term=" + request.term, function (data) {
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
                        $.getJSON("/getdept?term=" + request.term, function (data) {
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












    $(function() {
        $("#filterkeywordtxt,#filter_bus,#filter_bus_des" ).autocomplete({

        select : function(event, ui) {
                // $('#filterkeywordtxt').val(ui.item.label);
                $('#filterkeyword').val(ui.item.extra);
        },
        minLength: 2,
        delay: 100
        });
    });
});
