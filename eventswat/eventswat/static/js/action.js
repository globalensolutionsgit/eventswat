$(document).ready(function(){

	$(document).on("change", "#datepicker", function () {
	   $.ajax({
           type:"GET",
           url:"/postevent/getevents_by_date/",
           data: {
              'date': $(this).val(),
             },
           success: function(data){
           	  x = '<ul>';
           	  $.each(data, function(i,val){  
              	x += '<li><a href="details/'+val.id + '">' + val.eventtitle + '</a></li>';
              });
              x += '</ul>';
              alert(x);
              $('.event_name').html(x);
            }
	   });
	});
});