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

    $(".subcategory_list").hide();
    $(".subcategory_list:first").show();

	$( ".category_icon_hover").hover(function () {
        $(this).addClass('active');
        $(this).siblings('li').removeClass('active');
        $(this).find('ul.subcategory_list').show();
        $(this).siblings().find('ul.subcategory_list').hide();
    });
	
//Grid and list view in listpage
        $(".listgrid_events").hide();
        $(".grid_view").click(function(){
            $('#search_result').removeClass('list_active');
            $('#search_result').addClass('grid_active');
            $('.listgrid_events').show();
            $('.listview_events').hide();
        });
        
        $(".list_view").click(function(){
            $('#search_result').removeClass('grid_active');
            $('#search_result').addClass('list_active');
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
