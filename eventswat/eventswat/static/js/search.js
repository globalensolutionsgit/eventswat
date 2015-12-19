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
	    	// var q = $('#f_search').serialize();
	    	// alert(q);
	    	$("#f_search").submit();
	   }	   			 
	}
	 
	 $('.advsearch-btn').on('click', function() {
	 		$('[name=city]').val($('#city').val());
			validateSearch();
	 });
});