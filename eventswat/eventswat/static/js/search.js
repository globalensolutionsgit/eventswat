$(document).ready(function(){
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
	 		$('[name=q]').val($('#event_title').val());
	 		$('[name=city]').val($('#city').val());	 		
	 		if ($("[name='city']").val() == '' )
	 			$('[name=city]').attr("disabled",true);
			validateSearch();
	 });
});