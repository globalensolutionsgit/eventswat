// this function is used for advance search using ajax
function perform_search(){ 
    var q = $('#form_search_filter').serialize();
    $.get('/search/?'+ q, function(data){       
      $('#search_result').html(data);
      // Below condition is used for setting grid and view after ajax load
      if ($('#search_result').hasClass("grid_active")){
      	$('.listview_events').hide();
      }     	
      if ($('#search_result').hasClass("list_active")){
      	$('.listgrid_events').hide();
      }      	
      attach_pagination_events();       
    });
}

function attach_pagination_events(){
    $('[data-ajaxlink=true]').click(function(ele){
    $("html, body").animate({ scrollTop: 1100 }, "slow");
    $('#page').val($(ele.currentTarget).attr('data-ajaxpage'));             
    perform_search();
    return false;
    });      
}

$(document).ready(function(){
	attach_pagination_events();
	function validateSearch() {
	   var is_search_page = window.location.href.indexOf('/search')
	   if(is_search_page > 1)
	   {
	   		$('[name=q]').val($('#q').val());
			perform_search();
	   }
	   else
	   {
	       	if($('#q').val() == ''){
		         $('#q').val('');
	    	}	
	    	$("#f_search").submit();
	   }	   			 
	}
	$('.search-btn, .advsearch-btn').on('click', function() {
		if ($('#event_title').val())
 			$('[name=q]').val($('#event_title').val());
 		$('[name=city]').val($('#city').val());	 		
 		if ($("[name='city']").val() == '' )
 			$('[name=city]').attr("disabled",true);
		validateSearch();
	});
	
	// City based search when change dropdown in listing page
	$(document).on("change", '.city_selectbox', function () {       
		var selected_option = $( ".city_selectbox option:selected" ).val();  
		$('[name=city]').val(selected_option);	
		perform_search();		      
	});

	// Event type search either free or paid when choose radio button in listing page
	$(document).on("change", 'input[name="radio"]', function () {       
		var selected_option = $( 'input[name="radio"]:checked' ).val();  
		$('[name=eventtype]').val(selected_option);
		perform_search();		      
	});

	// Load city via ajax before typed fully
	$(function() {    
	    $("#fitltercitytxt" ).autocomplete({
	    open: function(){
	        setTimeout(function () {
	            $('.ui-autocomplete').css('z-index', 9999);
	        }, 0);
	    },

	    source: function (request, response) {

	        $.getJSON("/getcity_base?term=" + request.term, function (data) {             
	            response($.map(data, function (value, key) {                            
	                return {
	                    label: value.label,
	                    value: value.value,
	                    extra: value.cityid
	                };
	            }));
	        });
	    },
	    select : function(event, ui) {
	            $('#fitltercity').val(ui.item.value);                
	    },
	    minLength: 2,
	    delay: 100
	    });
  });
  
  $("#fitltercitytxt" ).blur(function () {
    	$('#fitltercity').val($("#fitltercitytxt" ).val());
  });


});
