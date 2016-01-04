//Home page nav bar
$(document).ready(function(){


// $(".grid-item").each(function(){
//  var img_height = $(this).children('img').height();
//  var img_width = $(this).children('img').width();
//  $(this).find('img').attr('width', img_width).attr('height', img_height);
//  $(this).css('width', img_width + 'px').attr('height', img_height + 'px');
 
// })

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
$('#datepicker_calender, .calendar, .events_calander').hide();
 $('.advance_btn').click(
    function(){
        $('.search_content').animate(
            {
                'margin-left' : '-=1500px'
            },500);

        $('.advance_search').show();        
        $('.advance_content').animate(
            {
                'margin-right' : '0'
            },510);

        $('#datepicker_calender, .events_calander').show();
        });
 
    $('.down_font').on('click', function(){
        $('.search_content').animate(
            {
                'margin-left' : '100px'
            },500);
        // $('.search_content').show();

        // $('.advance_content').animate(
        //     {
        //     'margin-right' : '+=1500px'
        //     },500);
        $('.advance_search').hide();          
        $('#datepicker_calender, .events_calander').hide();                
    });

//calendar
	
	$(function() {
	    $( "#datepicker_calender" ).datepicker({
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

 // Masonry
  var $grid = $('.grid').masonry({
    columnWidth: 82,
    });
  
//Prioritized banner
   $(function(){
    $(".large_image img:eq(0)").nextAll().hide();
    $(".thumbnails_img img").click(function(e){
        e.preventDefault();
        var index = $(this).index();
        $(".large_image img").eq(index).show().siblings().hide();
    });
});


});
