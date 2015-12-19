//Home page nav bar
$(document).ready(function(){

// hide .navbar first
	$(".navbar").hide();
	
	// fade in .navbar
	$(function () {
		$(window).scroll(function () {
            // set distance user needs to scroll before we fadeIn navbar
			if ($(this).scrollTop() > 100) {
				$('.navbar').fadeIn();
			} else {
				$('.navbar').fadeOut();
			}
			if ($(this).scrollTop() > 654) {
				$('.navbar').addClass('navbar_active');
				$('.navbar-header a').addClass('white_logo');
				$('.navbar-nav a').addClass('active_color');
			} 
		});
	});

//on clicking the down-arrow the slider-content slidesup	
	$('.down-arrow').click(function(){
  	$('html, body').animate({ scrollTop: $(".slider_content").offset().top }, 'slow');
  });

//advance button slide left
$('.advance_search').hide();
 $('.advance_btn').click(
    function(){
        $('.search_bar').animate(
            {
                'margin-left' : '-=1500px'
            },500);
        $('.advance_search').show();
        });
 

//calendar
	$('#datepicker ,.events_calander').hide();
	$(function() {
	    $( "#datepicker" ).datepicker({
	      numberOfMonths: 2,
	      showButtonPanel: true,
	       dayNamesMin: ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
	    });
 	 });

	$('.down_font').click(
    function(){
       $('.calander').addClass('calander_active');
    });

	$(".down_font").click(function(){
		$('#datepicker, .events_calander').toggle();

	});



});