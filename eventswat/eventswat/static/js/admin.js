$(document).ready(function(){
    $('.field-event_subcategory').hide();
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
});
