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
	$('.city_selectbox').on("change", function () {       
		var selected_option = $(".city_selectbox option:selected").val();  
		$('[name=city]').val(selected_option);	
		perform_search();		      
	});

	// Event type search either free or paid when choose radio button in listing page
	$('input[name="radio"]').on("change", function () {       
		var selected_option = $( 'input[name="radio"]:checked' ).val();  
		$('[name=eventtype]').val(selected_option);
		perform_search();		      
	});

	// Category based search in listing page
	$('.subcategory_list li').on("click", function () {       
		var selected_option = $(this).attr('data-subcategory');
		$('[name=eventtype]').val('');  
		$('[name=eventsubcategory]').val(selected_option);
		perform_search();		      
	});

});
