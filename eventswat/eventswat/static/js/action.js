function getevents_by_date(date)
{
  $.ajax({
       type:"GET",
       url:"/postevent/getevents_by_date/",
       data: {
          'date': date,
         },
       success: function(response){
          var x='';
          $.each(eval(response), function(i,val){  
            x += '<li><a href="details/'+ val.id + '">' + val.title + '</a></li>';
          });
          $('.jevent_list_date').html(x);
        }
    });
}

$(document).ready(function(){ 
    getevents_by_date($(this).val());
  	$(document).on("change", "#datepicker", function () {
      getevents_by_date($(this).val());
  	});
});

