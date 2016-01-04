// this function is used for advance search using ajax
function perform_search(){ 
    var q = $('#form_search_filter').serialize();
    var qfilter = $(".filterdata").find('li.active a').attr('data-value');
        q = q +'&filterdata='+$.trim(qfilter);
        
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
		if ($('#fitlter_title').val())
 			$('[name=q]').val($('#fitlter_title').val());
 		
 		if($('#fitltercity').val())
 		$('[name=city]').val($('#fitltercity').val());	 		
 		if ($("[name='city']").val() == '' )
 			$('[name=city]').attr("disabled",true);
 		validateSearch();
	});


	//sorted_data click function in home page for calendar based events
    $('.filterdata li').click(function () {
      $(this).addClass("active");
      $(this).siblings().removeClass("active");
      perform_search();
    });


	// autocomplete function for city
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
	    // minLength: 2,
	    // delay: 100
	    });
	});
	  
	$("#fitltercitytxt" ).blur(function () {
	   $('#fitltercity').val($("#fitltercitytxt" ).val());
	}); 


	//autocomplete function for Event name
	$(function() { 
	    $("#filter_title_term" ).autocomplete({
	    open: function(){
	        setTimeout(function () {
	            $('.ui-autocomplete').css('z-index', 9999);
	        }, 0);
	    },

	    source: function (request, response) {

	        $.getJSON("/get_event_title?term=" + request.term, function (data) {             
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
	            $('#fitlter_title').val(ui.item.value);                
	    },
	    // minLength: 2,
	    // delay: 100
	    });
	});
	  
	$("#filter_title_term" ).blur(function () {
	   $('#fitlter_title').val($("#filter_title_term" ).val());
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

	//keyword search in listing page
	$('.search_btn_listpage').on('click', function(){
		var words = $('input[name="q"]').val($('#keyword_search').val());
		perform_search();	
	});

});// ends docuement.ready function



