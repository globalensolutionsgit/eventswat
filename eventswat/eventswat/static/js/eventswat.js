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


//subcategory hover in listpage
	$(".campus_list ul,.competition_list ul,.exhibition_list ul,.spiritual_list ul,.business_list ul,.sports_list ul,.adventure_list ul").hide();
 	$(".category_img1").hover(function () {
        $(".entertainment_list ul").toggle();
        $(".campus_list ul,.competition_list ul,.exhibition_list ul,.spiritual_list ul,.business_list ul,.sports_list ul,.adventure_list ul").hide();
    });
    $(".category_img2").hover(function () {
        $(".campus_list ul").toggle();
        $(".entertainment_list ul,.competition_list ul,.exhibition_list ul,.spiritual_list ul,.business_list ul,.sports_list ul,.adventure_list ul").hide();
    });
    $(".category_img3").hover(function () {
        $(".competition_list ul").toggle();
        $(".entertainment_list ul,.exhibition_list ul,.spiritual_list ul,.business_list ul,.sports_list ul,.adventure_list ul").hide();
    });
     $(".category_img4").hover(function () {
        $(".exhibition_list ul").toggle();
        $(".entertainment_list ul,.competition_list ul,.spiritual_list ul,.business_list ul,.sports_list ul,.adventure_list ul").hide();
    });
      $(".category_img5").hover(function () {
        $(".spiritual_list ul").toggle();
        $(".entertainment_list ul,.competition_list ul,.exhibition_list ul,.business_list ul,.sports_list ul,.adventure_list ul").hide();
    });
       $(".category_img6").hover(function () {
        $(".business_list ul").toggle();
        $(".entertainment_list ul,.competition_list ul,.exhibition_list ul,.spiritual_list ul,.sports_list ul,.adventure_list ul").hide();
    });
        $(".category_img7").hover(function () {
        $(".sports_list ul").toggle();
        $(".entertainment_list ul,.competition_list ul,.exhibition_list ul,.spiritual_list ul,.business_list ul,.adventure_list ul").hide();
    });
         $(".category_img8").hover(function () {
        $(".adventure_list ul").toggle();
        $(".entertainment_list ul,.competition_list ul,.exhibition_list ul,.spiritual_list ul,.business_list ul,.sports_list ul").hide();
    });

//Grid and list view in listpage
        
        $(".grid_view").click(function(){
            $('.listgrid_events').show();
            $('.listview_events').hide();
        });
        
        $(".list_view").click(function(){
            $('.listview_events').show();
            $(".listgrid_events").hide();
        });
});
