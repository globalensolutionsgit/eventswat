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
$('.advance_search, #datepicker').hide();
 $('.advance_btn').click(
    function(){
        $('.search_bar').animate(
            {
                'margin-left' : '-=1500px'
            },500);
        $('.advance_search').show();
        $('#datepicker').show();
        });
 
    $('.down_font').click(function(){
        $('#datepicker').hide();
        $('.search_bar').show();
    });

//calendar
	
	$(function() {
	    $( "#datepicker" ).datepicker({
          dateFormat: 'yy-mm-dd',
	      numberOfMonths: 2,
	      showButtonPanel: true,
	       dayNamesMin: ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
	    });
 	 });

	
	

//subcategory hover in listpage
	$(".campus_list ul,.competition_list ul,.exhibition_list ul,.spiritual_list ul,.business_list ul,.sports_list ul,.adventure_list ul").hide();
 	$(".category_img1 ,.category_hovericon").hover(function () {
        $(".entertainment_list ul").show();
        $(".campus_list ul,.competition_list ul,.exhibition_list ul,.spiritual_list ul,.business_list ul,.sports_list ul,.adventure_list ul").hide();
    });
    $(".category_img2 ,.category_hovericon").hover(function () {
        $(".campus_list ul").show();
        $(".entertainment_list ul,.competition_list ul,.exhibition_list ul,.spiritual_list ul,.business_list ul,.sports_list ul,.adventure_list ul").hide();
    });
    $(".category_img3 ,.category_hovericon").hover(function () {
        $(".competition_list ul").show();
        $(".entertainment_list ul,.campus_list ul,.exhibition_list ul,.spiritual_list ul,.business_list ul,.sports_list ul,.adventure_list ul").hide();
    });
     $(".category_img4 ,.category_hovericon").hover(function () {
        $(".exhibition_list ul").show();
        $(".entertainment_list ul,.campus_list ul,.competition_list ul,.spiritual_list ul,.business_list ul,.sports_list ul,.adventure_list ul").hide();
    });
      $(".category_img5 ,.category_hovericon").hover(function () {
        $(".spiritual_list ul").show();
        $(".entertainment_list ul,.campus_list ul,.competition_list ul,.exhibition_list ul,.business_list ul,.sports_list ul,.adventure_list ul").hide();
    });
       $(".category_img6 ,.category_hovericon").hover(function () {
        $(".business_list ul").show();
        $(".entertainment_list ul,.campus_list ul,.competition_list ul,.exhibition_list ul,.spiritual_list ul,.sports_list ul,.adventure_list ul").hide();
    });
        $(".category_img7 ,.category_hovericon").hover(function () {
        $(".sports_list ul").show();
        $(".entertainment_list ul,.campus_list ul,.competition_list ul,.exhibition_list ul,.spiritual_list ul,.business_list ul,.adventure_list ul").hide();
    });
         $(".category_img8 ,.category_hovericon").hover(function () {
        $(".adventure_list ul").show();
        $(".entertainment_list ul,.campus_list ul,.competition_list ul,.exhibition_list ul,.spiritual_list ul,.business_list ul,.sports_list ul").hide();
    });

//Grid and list view in listpage
        $(".listgrid_events").hide();
        $(".grid_view").click(function(){
            $('.listgrid_events').show();
            $('.listview_events').hide();
        });
        
        $(".list_view").click(function(){
            $('.listview_events').show();
            $(".listgrid_events").hide();
        });

 // init Masonry
  var $grid = $('.grid').masonry({
    itemSelector: '.grid-item',
    percentPosition: true,
    columnWidth: '.grid-sizer'
  });
  





});
