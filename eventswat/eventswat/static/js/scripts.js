(function($) {
  "use strict";
  $.cookie.raw = true;
  var $body = $('body');
  // var $head = $('head');
  // var $mainWrapper = $('#main-wrapper');

  // Mediaqueries
  // ---------------------------------------------------------
  // var XS = window.matchMedia('(max-width:767px)');
  // var SM = window.matchMedia('(min-width:768px) and (max-width:991px)');
  // var MD = window.matchMedia('(min-width:992px) and (max-width:1199px)');
  // var LG = window.matchMedia('(min-width:1200px)');
  // var XXS = window.matchMedia('(max-width:480px)');
  // var SM_XS = window.matchMedia('(max-width:991px)');
  // var LG_MD = window.matchMedia('(min-width:992px)');


  // jquery ui call functionfor calendar
  //------------------------------------------------
  $(function () {
    $(  "#dpd1" ).datepicker({ format: 'dd-mm-yyyy', minDate: 0});
    $( "#dpd2" ).datepicker({ format: 'dd-mm-yyyy', minDate: 0});
    // $( "#address" ).datepicker({ format: 'dd-mm-yyyy', minDate: 0});
});

  // for date picker

  var nowTemp = new Date();
  var now = new Date(nowTemp.getFullYear(), nowTemp.getMonth(), nowTemp.getDate(), 0, 0, 0, 0);

  var checkin = $('#dpd1').datepicker({
        format: 'dd-mm-yyyy',
        onRender: function(date) {
            return date.valueOf() < now.valueOf() ? 'disabled' : '';
        }
  }).on('changeDate', function(ev) {
  if (ev.date.valueOf() > checkout.date.valueOf()) {
    var newDate = new Date(ev.date)
    newDate.setDate(newDate.getDate());
    checkout.setValue(newDate);
  }
  checkin.hide();
  $('#dpd2')[0].focus();
  }).data('datepicker');
var checkout = $('#dpd2').datepicker({
  format: 'dd-mm-yyyy',
  onRender: function(date) {
    return date.valueOf() <= checkin.date.valueOf() ? 'disabled' : '';
  }
}).on('changeDate', function(ev) {
  checkout.hide();
}).data('datepicker');
  // Touch
  // ---------------------------------------------------------
  var dragging = false;

  $body.on('touchmove', function() {
    dragging = true;
  });

  $body.on('touchstart', function() {
    dragging = false;
  });


  // Advanced search toggle
  var $SearchToggle = $('.header-search-bar .search-toggle');
  $SearchToggle.hide();

  $('.header-search-bar .toggle-btn').on('click', function(e){
    e.preventDefault();
    $SearchToggle.slideToggle(300);
  });


  // navbar toggle
  //------------------------------------------------
  $('.header-nav-bar button').on('click',function(){
    $('.header-nav-bar').toggleClass('active');
  });

  var $headerNavBar = $('#header .header-nav-bar, .header-nav-bar button');

  $headerNavBar.each(function () {
    var $this = $(this);

    $this.on('clickoutside touchendoutside', function () {
      if ($this.hasClass('active')) { $this.removeClass('active'); }
    });
  });

  $('input[type=file]').simpleFilePreview();

  // Category toggle
  //-------------------------------------------------

  $('.category-toggle button').on('click',function(){
    $('.category-toggle').toggleClass('active');
  });

  var $CategoryTtoggle = $('.category-toggle');

  $CategoryTtoggle.each(function () {
    var $this = $(this);

    $this.on('clickoutside touchendoutside', function () {
      if ($this.hasClass('active')) { $this.removeClass('active'); }
    });
  });





  //home slide tab-content hide
  //---------------------------------------
  $('.home-tab li > a').on('click', function(){

    $CategoryTtoggle.removeClass('active');
  });

  // home map tab-content hide
  //---------------------------------------------
  $('.accordion-tab li > div a').on('click', function(){

    $CategoryTtoggle.removeClass('active');
  });


  // our-partners slider customize
  //-----------------------------------------
  $("#partners-slider").owlCarousel({
    autoPlay: 3000,
    items : 3,
    itemsDesktop : [1199,4],
    itemsDesktopSmall : [979,3],
    itemsTablet: [600,2]
  });



    

    function find_city(state){
      $.get('/find_city/', { state: state }, function(data) {
      $('.select_city').html($('<option>').text("Select City"));
      $(".select_city").siblings('.select-clone').html($('<li>').text("Select City").attr('data-value', "select_city"));
      $.each(data, function(key,value) {
        $('.select_city').append($('<option>').text(value.name).attr('value', value.id));
        $(".select_city").siblings('.select-clone').append($('<li>').text(value.name).attr('data-value', value.id));
      });
      });
    }


   function find_colleges(city_id){
      $.get('/find_colleges/', { city_id: city_id }, function(data) {
      $('.select_college').html($('<option>').text("Select College"));
      $(".select_college").siblings('.select-clone').html($('<li>').text("Select College").attr('data-value', "select_college"));
      $.each(data, function(key,value) {
        $('.select_college').append($('<option>').text(value.name).attr('value', value.id));
        $(".select_college").siblings('.select-clone').append($('<li>').text(value.name).attr('data-value', value.id));
      });
      });
    }


   function find_department(college_id){
      $.get('/find_department/', { college_id: college_id }, function(data) {
      $('.select_dept').html($('<option>').text("Select Department"));
      $(".select_dept").siblings('.select-clone').html($('<li>').text("Select Department").attr('data-value', "select_department"));
      $.each(data, function(key,value) {
        $('.select_dept').append($('<option>').text(value.name).attr('value', value.name));
        $(".select_dept").siblings('.select-clone').append($('<li>').text(value.name).attr('data-value', value.name));
      });
      });
    }

    function find_subcategory(category_id){
      $.get('/find_subcategory/', { category_id: category_id }, function(data) {
         $('.select_subcategory').empty();
      $.each(data, function(key,value) {
        $('.select_subcategory').append($('<option>').text(value.name).attr('value', value.id));
      });
      });
    }

  

  $( "#slider-range-min" ).slider({
    range: "min",
    value: 42,
    min: 1,
    max: 100,
    slide: function( event, ui ) {
      $( "#amount" ).val( ui.value +   "km" );
    }
  });
  $( "#amount" ).val( $( "#slider-range-min" ).slider( "value" ) +   "km");


  $( "#slider-range-search" ).slider({
    range: "min",
    value: 42,
    min: 1,
    max: 100,
    slide: function( event, ui ) {
      $( "#amount-search" ).val( ui.value +   "km" );
    }
  });
  $( "#amount-search" ).val( $( "#slider-range-search" ).slider( "value" ) +   "km");


  $('.select_category').on('change' ,function(){
    var id = $('.select_category').val();
    find_subcategory(id);
  });

  $( "#slider-range-search-day" ).slider({
    range: "min",
    value: 20,
    min: 1,
    max: 300,
    slide: function( event, ui ) {
      $( "#amount-search-day" ).val(  "<"  + ui.value );
    }
  });
  $( "#amount-search-day" ).val( "<" +  $( "#slider-range-search-day" ).slider( "value" ) );





  // Accordion
  // ---------------------------------------------------------
  $('.accordion').each(function () {

    $(this).find('ul > li > a').on('click', function (event) {
      event.preventDefault();

      var $this = $(this),
        $li = $this.parent('li'),
        $div = $this.siblings('div'),
        $siblings = $li.siblings('li').children('div');

      if (!$li.hasClass('active')) {
        $siblings.slideUp(250, function () {
          $(this).parent('li').removeClass('active');
        });

        $div.slideDown(250, function () {
          $li.addClass('active');
        });
      } else {
        $div.slideUp(250, function () {
          $li.removeClass('active');
        });
      }
    });

  });



  // header login register scripts
  //-------------------------------------------

  var $headerLoginRegister = $('#header .header-login, #header .header-register');

  $headerLoginRegister.each(function () {
    var $this = $(this);

    $this.children('a').on('click', function (event) {
      event.preventDefault();
      $this.toggleClass('active');
      setTimeout (function(){
        $this.find('form input[type="text"]:first').focus();
      }, 1000);
      $this.siblings().removeClass('active');
      $('#header .header-language').removeClass('active');
      $('#header .header-social').removeClass('active');
    });

    $this.on('clickoutside touchendoutside', function () {
      if ($this.hasClass('active')) { 
        $this.removeClass('active'); 
      }
    });
  });

  var $headerNavbar = $('#header .header-nav-bar .primary-nav > li');

  $headerNavbar.each(function () {
    var $this = $(this);

    $this.children('a').on('click', function (event) {
      $this.toggleClass('active');
    });

    $this.on('clickoutside touchendoutside', function () {
      if ($this.hasClass('active')) { $this.removeClass('active'); }
    });
  });




  // Header Language Toggle
  var $headerLanguageToggle = $('#header .header-language');

  $headerLanguageToggle.children('a').on('click', function (event) {
    event.preventDefault();
    $(this).parent('.header-language').toggleClass('active');
    $('#header .header-login').removeClass('active');
    $('#header .header-register').removeClass('active');
    $('#header .header-social').removeClass('active');

  });

  $headerLanguageToggle.on('clickoutside touchendoutside', function () {
    if ($headerLanguageToggle.hasClass('active')) { $headerLanguageToggle.removeClass('active'); }
  });

  // Header Social Toggle
  
  var $headerSocialToggle = $('#header .header-social');
 
  $headerSocialToggle.children('a').on('click', function (event) {
    event.preventDefault();
    $(this).parent('.header-social').toggleClass('active');
    $('#header .header-login').removeClass('active');
    $('#header .header-register').removeClass('active');
    $('#header .header-language').removeClass('active');
  });

  $headerSocialToggle.on('clickoutside touchendoutside', function () {
    if ($headerSocialToggle.hasClass('active')) { $headerSocialToggle.removeClass('active'); }
  });



  // sub-categories remove and active class
  //-----------------------------------------------------
  var $CategoryLink = $('#categories .accordion ul li div a');

  $CategoryLink.on('click', function(){
    $(this)
      .addClass('active')
      .siblings().removeClass('active')
      .parent().parent().siblings('li').children('div a').click(function(){
        $CategoryLink.removeClass('active');
      });
  });



  // style switcr for list-grid view
  //--------------------------------------------------
  $('.change-view button').on('click',function(e) {

    if ($(this).hasClass('grid-view')) {
      $(this).addClass('active');
      $('.list-view').removeClass('active');
      $('.page-content .view-switch').removeClass('product-details-list').addClass('product-details');

    } else if($(this).hasClass('list-view')) {
      $(this).addClass('active');
      $('.grid-view').removeClass('active');
      $('.page-content .view-switch').removeClass('product-details').addClass('product-details-list');
      }
  });




  // company-heading slider content
  //--------------------------------------------------------
  $('.button-content button').on('click',function(e) {
    console.log('clickes');

    if ($(this).hasClass('general-view-btn')) {
      $(this).addClass('active')
      .siblings().removeClass('active')
      .parent().parent().next().css("left","0%");


    } else if($(this).hasClass('map-view-btn')) {
      $(this).addClass('active')
      .siblings().removeClass('active')
      .parent().parent().next().css("left","-100%");

    } else if($(this).hasClass('male-view-btn')) {
      $(this).addClass('active')
     .siblings().removeClass('active')
     .parent().parent().next().css("left","-200%");
    }

  });


  $("a").click(function(e){
    if($(this).attr("href") === '#'){
      e.preventDefault();
    }
  });



  $('input, textarea').placeholder();


}(jQuery));


$( ".keywords input, .select-location input " ).focus(function() {
  $('html, body').animate({ scrollTop: $(".header-search-bar").offset().top }, 500);
});

  jQuery.fn.center = function () {
    this.css("top", ( jQuery(window).height() - this.height() ) / 2+jQuery(window).scrollTop()+100 + "px");
    return this;
  }
  
  $(window).scroll(function (){
    $(".popup_pos").center();
        
  });



$("document").ready(function($){

// $("#review_from").submit(function(event) {
//        $.ajax({ 
//                 data: $(this).serialize(), 
//                 type: $(this).attr('method'), 
//                 url: $(this).attr('action'),
//                 success: function(response) {
//                 $('#mgs').show();
//             }
//         })
//         event.preventDefault();
//     });
$('.error').hide();
 $("#review_btn").click(function(event){
         $('.error').hide();
          var name = $('input[name="name"]').val();
          if (name == "") {
            $("label#name_error").show();
            $("input#name").focus();
            return false;
          }
          var email = $('input[name="email"]').val();
          if (email == "") {
            $("label#email_error").show();
            $("input#email").focus();
            return false;
          }
          var rating = $('input[name="rating"]').val();
          if (rating == "") {
            $("label#rating_error").show();
            $("input#rating").focus();
            return false;
          }
          var content = $('input[name="content"]').val();
          if (content == "") {
            $("label#content_error").show();
            $("input#content").focus();
            return false;
          }

          $.ajax({
               type:"POST",
               url:"/review/",
               data: {
                      'name': $('#name').val(),
                      'email': $('#email').val(),
                      'rating': $('input[name="rating"]').val(),
                      'content': $('#content').val(),
                      'postevent': $('#postevent').val(),
                      },
               success: function(){
                   $('#mgs').show();
                   setTimeout(function() { $("#mgs").hide(); }, 5000);
                  }
          });
          $('#name').val('');
          $('#email').val('');
          $('#rating').val('');
          $('#content').val('');
          return false;
        
       });


/******************feedback form ************************/
$('.error').hide();
 $("#feed_btn").click(function(event){
         $('.error').hide();
          var name = $('input[name="name"]').val();
          if (name == "") {
            $("label#name_error").show();
            $("input#name").focus();
            return false;
          }
          var email = $('input[name="email"]').val();
          if (email == "") {
            $("label#email_error").show();
            $("input#email").focus();
            return false;
          }
          var rating = $('input[name="rating"]').val();
          if (rating == "") {
            $("label#rating_error").show();
            $("input#rating").focus();
            return false;
          }
          var comments = $('input[name="comments"]').val();
          if (comments == "") {
            $("label#comments_error").show();
            $("input#comments").focus();
            return false;
          }

          $.ajax({
               type:"POST",
               url:"/feed/",
               data: {
                      'name': $('#name').val(),
                      'email': $('#email').val(),
                      'rating': $('input[name="rating"]').val(),
                      'comments': $('#comments').val(),
                      
                      },
               success: function(){
                   $('#mgs').show();
                   setTimeout(function() { $("#mgs").hide(); }, 5000);
                  }
          });
          $('#name').val('');
          $('#email').val('');
          $('#rating').val('');
          $('#comments').val('');
          return false;
        
       });
/**************end******************/

// var limit = 3;
// var count = 1;
// var add_number = $('.number');
// $('.add_number_act').click(function(){
// if(count < limit){
//   count++;   
//   $(add_number).append("<input type='text' placeholder='Organizer mobile' name='organizer_mobile_"+ count +"' id='organizer_mobile_"+count +"' class='organizer_mobile margintop_2rem' value='' data-number='true' data-required='true'>");
// }
// });


$(".feedback_popup").hide();
$('.feedback1').click(function(){
 $(".feedback_popup").show();
  $('.feedback1').hide();
});


//add aditional mobile  number for organizer in postevent
var limit = 3;
var count = 1;
var add_number = $('.number');
$('.add_number_act').click(function(){
if(count < limit){
  count++;   
  $(add_number).append("<input type='text' placeholder='Organizer mobile' name='organizer_mobile_"+ count +"' id='organizer_mobile_"+count +"' class='organizer_mobile margintop_2rem' value='' data-number='true' data-required='true'>");
}
});


$('.close').click(function(){
  $(".feedback_popup").hide();
  $('.feedback1').show();
});

  $(".stepsForm").stepsForm({
      width     :'100%',
      active      :0,
      errormsg    :'Please fill the all fields.',
      sendbtntext   :'submit',
      posturl     :'/submit_event_v2',
      theme     :'green',
    }); 
    
    $(".container .themes>span").click(function(e) {
        $(".container .themes>span").removeClass("selectedx");
        $(this).addClass("selectedx");
        $(".stepsForm").removeClass().addClass("stepsForm");
        $(".stepsForm").addClass("sf-theme-"+$(this).attr("data-value"));
    });

  var nav = $('.header-search-bar');
    $(window).scroll(function () {
      if ($(this).scrollTop() > 430) {
        nav.addClass("sticky");
      } else {
        nav.removeClass("sticky");
        $( ".keywords input, .select-location input " ).blur();
      }
  });

  $('.north').tipsy({gravity: 'n'});
  $('.west').tipsy({gravity: 'w'});
  $('.east').tipsy({gravity: 'e'});
  $('.south').tipsy({gravity: 's'});
  $('.northwest').tipsy({gravity: 'nw'});
  $('.southwest').tipsy({gravity: 'sw'});
  $('.northeast').tipsy({gravity: 'ne'});
  $('.southeast').tipsy({gravity: 'se'});

  // $('.header-search-bar').show();

  
  // $('.slider-content #home-slider .item > img').css('height',$(window).height()-75);
  // $('.slider-content').css('height',$(window).height()-75);
  if ($.cookie('eventdescription')){
      $('.eventdescription').val($.cookie('eventdescription'));
  }

  var body_win_height = parseInt(document.body.clientHeight) ;
  var win_height = parseInt(document.documentElement.clientHeight) ;
  
  if( body_win_height > win_height) {
      $('.popup_fade').height(body_win_height);
  } else {
      $('.popup_fade').height(win_height);
  }
  
  $(".popup_pos").center();

  $('.popup_cancel_btn').on('click',function() {
    $('.pop_up').hide();
    $('.popup_fade').hide();
  });

  $('.cancel_btn, .close_btn').on('click', function (){
    $.removeCookie('plan',{ path: '/' });
    $('.deposit_popup, .popup_fade,#forgotpassword_popup,#resetpassword_popup,.terms_services_popup, #signin_popup,#signup_popup, #joinus_popup_content, #signin_popup1, #email_activate, #login_window, #login_window1, .lead_details_popup, #directbuy_signin_popup, #auction_popup, #ask_question_popup, #thank_you_popup').hide();
    $('#plan_change').show();
    $('.header-search-bar').show();
    $('input[name="plan"]').val() == '';
  });

  $(".login_act, .login_button, .signin").on('click', function (){
        $('.popup_fade').show();
        $('#signin_popup').show();
        $('.header-search-bar').hide();       
  });

  $(".register_btn, .signup").on('click', function (){
    $('.popup_fade, #signup_popup').show();
    $('.header-search-bar').hide();     
  });


  // $('#forgotpassword_popup').hide();
  $(".forget_password").on('click', function (){
    alert("enter");

     $('#signup_popup, #signin_popup').hide();
     $('.popup_fade, #forgotpassword_popup').show();
  });

  $(".reset_btn").on('click', function (){
     $('#signup_popup').hide();
     $('.popup_fade, #resetpassword_popup').show();
  });

// $('.forgot_act').click(function(){
//   alert("enter");
//       forgot_center_align();
//       $('.popup_fade').show();
//       $('.popup_fade, #forgotpassword_popup').show();
//       $('.forgot_div, .close_btn').show();       
//       document.body.style.overflow = 'hidden';
//       });

  $('.post_event_btn_act').click(function(){
    $('input[name="next"]').val('/post_event');
  });
    $('.upload_banner_btn_act').click(function(){
    $('input[name="next"]').val('/upload_banner');
  });
  // home slider section
  //-------------------------------------------
  var homeSlide = $("#home-slider");

  homeSlide.owlCarousel({
    
    items : 1,
    loop:true,
    autoPlay: true,
    navigation : false, // Show next and prev buttons
    slideSpeed : 600,
    paginationSpeed : 600,
    singleItem:true,
    


  });


  // Custom Navigation Events
    $(".next").click(function(){
      homeSlide.trigger('owl.next');
    });
    $(".prev").click(function(){
      homeSlide.trigger('owl.prev');
    });



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

  $(function() {    
    $("#state" ).autocomplete({
    open: function(){
        setTimeout(function () {
            $('.ui-autocomplete').css('z-index', 9999);
        }, 0);
    },

    source: function (request, response) {
        $.getJSON("/getstate?term=" + request.term, function (data) {             
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
            $('#statetxt').val(ui.item.value);                
    },
    minLength: 2,
    delay: 100
    });
  });
  $("#state" ).blur(function () {
    $('#statetxt').val($("#state" ).val());
  });
  $(function() {    
    $("#city" ).autocomplete({
    open: function(){
        setTimeout(function () {
            $('.ui-autocomplete').css('z-index', 9999);
        }, 0);
    },

    source: function (request, response) {
         var state=$('#statetxt').val();
        $.getJSON("/getcity?term=" + request.term+"&state="+state, function (data) {             
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
            $('#citytxt').val(ui.item.value);
            $('#cityid').val(ui.item.extra);                
    },
    minLength: 2,
    delay: 100
    });
  });
  $("#city" ).blur(function () {
    $('#citytxt').val($("#city" ).val());
  });
  $(function() {    
    $("#college" ).autocomplete({
    open: function(){
        setTimeout(function () {
            $('.ui-autocomplete').css('z-index', 9999);
        }, 0);
    },

    source: function (request, response) {
        var city=$('#cityid').val();
        $.getJSON("/getcollege?term=" + request.term+"&city="+city, function (data) {             
            response($.map(data, function (value, key) {                            
                return {
                    label: value.label,
                    value: value.value,
                    extra: value.collegeid
                };
            }));
        });
    },
    select : function(event, ui) {
            $('#collegetxt').val(ui.item.value); 
            $('#collegeid').val(ui.item.extra);               
    },
    minLength: 2,
    delay: 100
    });
  });
$("#college" ).blur(function () {
    $('#collegetxt').val($("#college" ).val());
  });
  $(function() {    
    $("#dept" ).autocomplete({
    open: function(){
        setTimeout(function () {
            $('.ui-autocomplete').css('z-index', 9999);
        }, 0);
    },

    source: function (request, response) {
        var college=$('#collegeid').val();
        $.getJSON("/getdept?term=" + request.term+"&college="+college, function (data) {             
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
            $('#depttxt').val(ui.item.value);                
    },
    minLength: 2,
    delay: 100
    });
  });
  $("#dept" ).blur(function () {
    $('#depttxt').val($("#dept" ).val());
  });

  $('.select-location,.category-search').click(function(){
    //$('.base_search').focus();
  });


  $("a.bookmark").click(function(e){

     // this will prevent the anchor tag from going the user off to the link
    var bookmarkUrl = this.href;
    var bookmarkTitle = this.title;
    if (window.sidebar) { // For Mozilla Firefox Bookmark
      e.preventDefault();
      window.sidebar.addPanel(bookmarkTitle, bookmarkUrl,"");
    } else if( window.external || document.all) { // For IE Favorite
        e.preventDefault();
        window.external.AddFavorite( bookmarkUrl, bookmarkTitle);
    } else if(window.opera) { // For Opera Browsers
        e.preventDefault();
        $("a.bookmark").attr("href",bookmarkUrl);
        $("a.bookmark").attr("title",bookmarkTitle);
        $("a.bookmark").attr("rel","sidebar");
    } else { // for other browsers which does not support
        alert('Your browser does not support this bookmark action');
      return false;
  }
  });

$('.eventdetail_fields').hide();
$('.user_fields').hide();

$('.events').click(function(){
  $('.events_fields').toggle();
});

  $('.bxslider').bxSlider({
  auto: true,
  autoControls: true
});          

// // validation by kalai//
// //login form validation on button click
//   var sign_in_required =["emailid_signin", "password_signin"];
//   jQuery('#signin').click(function(){ 
//     email_val = $('#emailid_signin').val();    
//       for (i=0;i<sign_in_required.length;i++) {
//       var input = jQuery('#'+sign_in_required[i]);
//       if (input.val() == "")  {   
//         input.addClass("error_input_field");
//         input.next().next('.error_message').hide();         
//         input.next('.error_message').show();         
//       } else {    
//         input.removeClass("error_input_field");
//         input.next().next('.error_message').hide(); 
//         input.next('.error_message').hide();        
//       }
//     }
    
//     //Validate the e-mail.
   
//     if (!/^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/.test(email_val)) {
//       $("#emailid_signin").addClass("error_input_field");
//       $("#emailid_signin").next('.error_message').hide();
//       $("#emailid_signin").next().next('.error_message').show();
//     }
//     else
//     {
//       $("#emailid_signin").removeClass("error_input_field");
//       $("#emailid_signin").next().next('.error_message').hide();
//     }
  

//     if ($("#login_val :input").hasClass("error_input_field")){
//     return false;
//     }
//     else{
//       $('form[name="sign_in"]').submit();      
//       return true;
//     }
//   });

//Registration form validation on button click
//    jQuery('#create_user').click(function(){  
//     var sign_up_required =["emailid_signup", "username_signup", "mobile_signup", "password_signup", "confirm_password_signup" ];  
//     for (i=0;i<sign_up_required.length;i++) {
//       var input = jQuery('#'+sign_up_required[i]);
//       if (input.val() == "")  {   
//         input.addClass("error_input_field");
//         input.next().next('.error_message').hide();
//         input.next('.error_message').show();         
//       } else {    
//         input.removeClass("error_input_field");

//         input.next('.error_message').hide();        
//       }
//     }
//     //password
//     if($('#password_signup').val() == ''){   
//         $('#password_signup').addClass("error_input_field");
//         $('#password_signup').next('.error_message').show();         
//       } else {    
//         $('#password_signup').removeClass("error_input_field");
//         $('#password_signup').next('.error_message').hide();       
//       }
//     // confirm password
//     if($('#confirm_password_signup').val() == ''){   
//         $('#confirm_password_signup').addClass("error_input_field");
//         $('#confirm_password_signup').next().next('.error_message').hide(); 
//         $('#confirm_password_signup').next('.error_message').show();             
//       } 
//       else if ($('#confirm_password_signup').val() != $('#password_signup').val()){
//         $('#confirm_password_signup').addClass("error_input_field");
//         $('#confirm_password_signup').next('.error_message').hide();  
//         $('#confirm_password_signup').next().next('.error_message').show(); 
//       }
//       else {    
//         $('#confirm_password_signup').removeClass("error_input_field");
//         $('#confirm_password_signup').next('.error_message').hide();    
//         $('#confirm_password_signup').next().next('.error_message').hide();    
//       }
//     //Validate the e-mail
//     if($('#emailid_signup').val() != ''){
//     if (!/^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/.test($('#emailid_signup').val())) {
//       $('#emailid_signup').addClass("error_input_field");
//       $('#emailid_signup').next('.error_message').hide();
//       $('#emailid_signup').next().next('.error_message').show();
//     }
//     else
//     {
//       $('#emailid_signup').removeClass("error_input_field");
//       $('#emailid_signup').next().next('.error_message').hide();
//     }
//     }
//     //Validate the mobile
//     if($('#mobile_signup').val() != ''){
//       mobile_validation('#mobile_signup');
//     }

//      if ($("#user_form :input").hasClass("error_input_field")){
//     return false;
//     }
//     else{
//       $('form[name="sign_in"]').submit();      
//       return true;
//     }
// });

// // validation on blur
// $('.header-call-to-action input').blur(function(){
//         if ($(this).val() == "")  {   
//           $(this).addClass("error_input_field");
//           $(this).next().next('.error_message').hide();
//           $(this).next('.error_message').show();         
//         } else {    
//           $(this).removeClass("error_input_field");
//           $(this).next().next('.error_message').hide();
//           $(this).next('.error_message').hide();        
//         }

//         id = "#" + $(this).attr('id');
//         if ((id=="#emailid_signup" && $(id).val() != '') || (id=="#emailid_signin")){
//            if (!/^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/.test($(id).val())) {
//               $(id).addClass("error_input_field");
//               $(id).next('.error_message').hide();
//               $(id).next().next('.error_message').show();
//             }
//             else
//             {
//               $(id).removeClass("error_input_field");
//               $(id).next('.error_message').hide();
//               $(id).next().next('.error_message').hide();
//             } 
//         }

//         if(id=="#mobile_signup")
//           mobile_validation(id);


//         if ((id=="#confirm_password_signup") && ($(id).val()!='')){
//           if($(id).val()!=$('#password_signup').val()){
//             $(id).addClass("error_input_field");
//             $(id).next('.error_message').hide();  
//             $(id).next().next('.error_message').show(); 
//           }
//           else {    
//           $(id).removeClass("error_input_field");
//           $(id).next('.error_message').hide();    
//           $(id).next().next('.error_message').hide();    
//           }
//         }    
//  });
// //end validation//

  // New Registration form validation code for popup design
  jQuery('#create_user').click(function(){  
    // alert("create_user");
    var sign_up_required =["id_username", "id_email", "id_mobile", "id_password", "id_confirm_password"];  
    for (i=0;i<sign_up_required.length;i++) {
      var input = jQuery('#'+sign_up_required[i]);
      if (input.val() == "") {   
        input.addClass("error_input_field");
        input.next().next('.error').hide();
        input.next('.error').show();
      } else {    
        input.removeClass("error_input_field");

        input.next('.error').hide();        
      }
    }
    //password
    if($('#id_password').val() == ''){   
        $('#id_password').addClass("error_input_field");
        $('#id_password').next('.error').show();         
      } else {    
        $('#id_password').removeClass("error_input_field");
        $('#id_password').next('.error').hide();       
      }
    // confirm password
    if($('#id_confirm_password').val() == ''){   
        $('#id_confirm_password').addClass("error_input_field");
        $('#id_confirm_password').next().next('.error').hide(); 
        $('#id_confirm_password').next('.error').show();             
      } 
      else if ($('#id_confirm_password').val() != $('#id_password').val()){
        $('#id_confirm_password').addClass("error_input_field");
        $('#id_confirm_password').next('.error').hide();  
        $('#id_confirm_password').next().next('.error').show(); 
      }
      else {    
        $('#id_confirm_password').removeClass("error_input_field");
        $('#id_confirm_password').next('.error').hide();    
        $('#id_confirm_password').next().next('.error').hide();    
      }
    //Validate the e-mail
    if($('#id_email').val() != ''){
    if (!/^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/.test($('#id_email').val())) {
      $('#id_email').addClass("error_input_field");
      $('#id_email').next('.error').hide();
      $('#id_email').next().next('.error').show();
    }
    else
    {
      $('#id_email').removeClass("error_input_field");
      $('#id_email').next().next('.error').hide();
    }
    }
    //Validate the mobile
    if($('#id_mobile').val() != ''){
      mobile_validation('#id_mobile');
    }

     if ($("#user_form :input").hasClass("error_input_field")){
    return false;
    }
    else{
      $('form[name="sign_up"]').submit();      
      return true;
    }
});

    // validation on blur
    $('#user_form input').bind('blur keyup', function(){
        if ($(this).val() == "")  {   
          $(this).addClass("error_input_field");
          $(this).siblings('.email_exists_error').hide();
          $(this).next().next('.error').hide();
          $(this).next('.error').show();         
        } else {    
          $(this).removeClass("error_input_field");
          $(this).next().next('.error').hide();
          $(this).next('.error').hide();        
        }

        id = "#" + $(this).attr('id');
        if ((id=="#id_email" && $(id).val() != '') || (id=="#id_login_email")){
           if (!/^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/.test($(id).val())) {
              $(id).addClass("error_input_field");
              $(id).siblings('.email_exists_error').hide();
              $(id).next('.error').hide();
              $(id).next().next('.error').show();
            }
            else
            {
              $(id).removeClass("error_input_field");
              $(id).next('.error').hide();
              $(id).next().next('.error').hide();
            } 
        }

        if(id=="#id_mobile")
          mobile_validation(id);


        if ((id=="#id_confirm_password") && ($(id).val()!='')){
          if($(id).val()!=$('#id_password').val()){
            $(id).addClass("error_input_field");
            $(id).next('.error').hide();  
            $(id).next().next('.error').show(); 
          }
          else {    
          $(id).removeClass("error_input_field");
          $(id).next('.error').hide();    
          $(id).next().next('.error').hide();    
          }
        }    
         // if(($('#emailid_signup').val() != '') && (/^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/.test($('#emailid_signup').val()))){
         //  $.post("/register/", $('#user_form').serialize(),
         //      function (data) {
         //          if (data.email_exists){
         //            $('#emailid_signup').siblings('.error').hide();
         //            $('#emailid_signup').siblings('.email_exists_error').show();
         //          }
         //          if (!data.email_exists && isHTML(data))
         //            $('#emailid_signup').siblings('.email_exists_error').hide();

         //          // if (isHTML(data))
         //          //   top.location.href= $('input[name="next"]').val();             
         //          })
         //          .fail(function (err) {
         //          // alert(err);
         //    });
         // }
 });
//end validation//

  // New login form validation code for popup design
  function isHTML(str) {
    var a = document.createElement('div');
    a.innerHTML = str;
    for (var c = a.childNodes, i = c.length; i--; ) {
        if (c[i].nodeType == 1) return true; 
    }
    return false;
  }
  // sign in form validation
  var sign_in_required =["id_login_email", "id_login_password"];
  jQuery('#sign_in').click(function(){ 
      // email = $('#emailid_signin').val();    
      for (i=0;i<sign_in_required.length;i++) {
      var input = jQuery('#'+sign_in_required[i]);
      if (input.val() == "")  {
        input.addClass("error_input_field"); 
        input.next().next('.error').hide();
        input.next('.error').show();         
      } else {    
        input.removeClass("error_input_field");
        input.next('.error').hide();        
      }
    }

    if(($('#id_login_email').val() != '') && (!/^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/.test($('#id_login_email').val()))){
      $('#id_login_email').addClass("error_input_field");
      $('#id_login_email').next().next('.error').show();
    }
    else
    {
      $('#id_login_email').removeClass("error_input_field");
      $('#id_login_email').next().next('.error').hide();
    }

    if((($('#id_login_email').val() != '') && (/^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/.test($('#id_login_email').val()))) && ($('#id_login_password').val() != '')){
        $.post("/login/", $('#login_val').serialize(),
          function (data) {
          if (data.email_exists)
            $('#id_login_email').siblings('.email_exists_error').show();
          else
            $('#id_login_email').siblings('.email_exists_error').hide();

          if(data.password)
            $('#id_login_password').siblings('.error_pwd').show();
          else
            $('#id_login_password').siblings('.error_pwd').hide();

          if (isHTML(data))
            top.location.href= $('input[name="next"]').val();             
          })
          .fail(function (err) {
          // alert(err);
         });
    }
  });
  
  $('#login_val input').keyup(function(){
      if ($(this).val() == "")  {
        $(this).addClass("error_input_field"); 
        $(this).siblings('.email_exists_error').hide();
        $(this).siblings('.error_pwd').hide();
        $(this).siblings('.error').hide();
        $(this).next('.error').show();         
      } else {    
        $(this).removeClass("error_input_field");
        $(this).next('.error').hide();        
      }
      if(($('#id_login_email').val() != '') && (!/^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/.test($('#id_login_email').val()))){
        $('#id_login_email').addClass("error_input_field");
        $(this).siblings('.email_exists_error').hide();
        $(this).siblings('.error').hide();
        $('#id_login_email').next().next('.error').show();
      }
      else
      {
        $('#id_login_email').removeClass("error_input_field");
        $('#id_login_email').next().next('.error').hide();
      }
      if((($('#id_login_email').val() != '') && (/^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/.test($('#id_login_email').val()))) || ($('#password_signin').val() != '')){
        $.post("/login/", $('#login_val').serialize(),
          function (data) {
          if (data.email_exists){
            $('#id_login_email').siblings('.error').hide();
            $('#id_login_email').siblings('.email_exists_error').show();
          }
          else
            $('#id_login_email').siblings('.email_exists_error').hide();

          if(data.password){
            $('#id_login_password').siblings('.error').hide();
            $('#id_login_password').siblings('.error_pwd').show();
          }
          else
            $('#id_login_password').siblings('.error_pwd').hide();

          // if (isHTML(data))
          //   top.location.href= $('input[name="next"]').val();             
          })
          .fail(function (err) {
          // alert(err);
         });
      
      }
  });

  //for events_calendar newly updated by kalai
  $(document).on("mouseenter", ".days", function() {
    $(this).find('.list_events').show();
    $(this).siblings().find('.list_events').hide();
  });

  //postevent form validation
  //events
    // var events_required =["festname_required", "festcaption_val"];
  $('.free').click(function(){
    $('input[name="plan"]').val($('input[name="free"]').val());
    $('.plan_table_act').hide();
    $('.eventdetail_fields').show();
    
  });
  $('.paid').click(function(){
    $('input[name="plan"]').val($('input[name="paid"]').val());
    $('.plan_table_act').hide();
    $('.eventdetail_fields').show();
  });
  $('.login_act').click(function(){
    $('input[name="plan"]').val($('input[name="paid"]').val());
  });
  if($.cookie('plan')){
    $('.plan_table_act').hide();
  }
  else{
   $('.plan_table_act').show(); 
  }
  $('.plan_change').click(function(){
    $('.plan_table_act').show();
  });



  jQuery('.free,.events_details,.paid').click(function(){     
    if($('.eventtitle').val() == ''){
      $('.eventtitle_error').show();
      return false;
    }
    else{
      $('.eventtitle_error').hide();
    }

    if($('.startdate').val() == ''){
      $('.date1_error').show();
      return false;
    }
    else{
      $('.date1_error').hide();
    }  

    if($('.enddate').val() == ''){
      $('.date2_error').show();
      return false;
    }
    else{
      $('.date2_error').hide();
    }

    if($('.category').val() == ''){
      $('.category_error').show();
      return false;
    }
    else{
      $('.category_error').hide();
    }
    if($('.eventtype').val() == 'select_subcategory'){
      $('.subcategory_error').show();
      return false;
    }
    else{
      $('.subcategory_error').hide();
    }
    if($('.eventdescription').val() == ''){
      $('.eventdescription_error').show();
      return false;
    }
    else{
      $('.eventdescription_error').hide();
      var date = new Date();
      date.setTime(date.getTime() + (120 * 1000));
      $.cookie('eventtitle',$('.eventtitle').val(),{path: '/',raw: true, expires: date});
      $.cookie('startdate',$('.startdate').val(),{path: '/',raw: true,expires: date });
      $.cookie('enddate',$('.enddate').val(),{path: '/',raw: true,expires: date});
      if ($.cookie('category')){
        $.cookie('category',$('.category_id').val(),{path: '/',raw: true,expires: date});
        $.cookie('category_name',$('.category_name').val(),{path: '/',raw: true,expires: date});
        
      }
      else{
        $.cookie('category',$('.category option:selected').val(),{path: '/',raw: true,expires: date});
        $.cookie('category_name',$('.category option:selected').text(),{path: '/',raw: true,expires: date});
        
      }
      if ($.cookie('eventtype')){
        $.cookie('eventtype',$('.eventtype_id').val(),{path: '/',raw: true,expires: date});
        $.cookie('eventtype_name',$('.eventtype_name').val(),{path: '/',raw: true,expires: date});
      }
      else{
        $.cookie('eventtype',$('.eventtype option:selected').val(),{path: '/',raw: true,expires: date});
        $.cookie('eventtype_name',$('.eventtype option:selected').text(),{path: '/',raw: true,expires: date});
      }
      $.cookie('eventdescription',$('.eventdescription').val(),{path: '/',raw: true,expires: date});
      $.cookie('plan',$('input[name="plan"]').val(),{path: '/',raw: true,expires: date});

    }
    if($('input[name="plan"]').val() == ''){
      $('.plan_error').show();
      return false;
    }
    else{
      $('.plan_error').hide();
      $('.eventdetail_fields').show();
    }

  });

  //Event details

jQuery('.user_details').click(function(){     
    var mobile =$('.organize_moobile').val(); 
    var pattern = /^\d{10}$/;
    function isValidEmailAddress(emailAddress) {
        var pattern = new RegExp(/^[+a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/i);
        return pattern.test(emailAddress);
    };

    if($('.address').val() == ''){
      $('.address_error').show();
      return false;
    }
    else{
      $('.address_error').hide();
    }

    if($('.organize_name').val() == ''){
      $('.organizer_error').show();
      return false;
    }
    else{
      $('.organizer_error').hide();
    }  

    if($('.organize_email').val() == ''){
      $('.organizer_email_error').show();
      return false;
    }
    else if(!isValidEmailAddress( $('.email').val() )){
      $('.organizer_email_error').show().text('Enter Valid emailAddress');
      return false;
    }
    else{
      $('.organizer_email_error').hide();
    }  
    if($('.organize_moobile').val() == ''){
      $('.organizer_mobile_error').show();
      return false;
    }
     else if(!pattern.test(mobile)){
      $('.organizer_mobile_error').show().text("It is not valid mobile number.input 10 digits number!");
      return false;
    }
    else{
      $('.organizer_mobile_error').hide();
    } 
    if($('.state').val() == ''){
      $('.state_error').show();
      return false;
    }
    else{
      $('.state_error').hide();
    }

    if($('.select_city').val() == ''){
      $('.city_error').show();
      return false;
    }
    else{
      $('.city_error').hide();
    }
    if($('.college').val() == ''){
      $('.college_error').show();
      return false;
    }
    else{
      $('.college_error').hide();
    }
    if($('.dept').val() == ''){
      $('.dept_error').show();
      return false;
    }
    else{
      $('.dept_error').hide();
      $('.user_fields').show();
    }


  });
// Image upload in post event
    $(document).on('change','.poster',function(){
      files = this.files;
      size = files[0].size;
      var oFReader = new FileReader();
      oFReader.readAsDataURL(this.files[0]);
      oFReader.onload = function (oFREvent) {
        var image = new Image();
        image.src = oFREvent.target.result;
        $('#uploaded_img').remove();
        image.onload = function () {

          // if (this.width > 1200 ) {
          //   alert("Exceeded Image width (1200 pixels).Please upload below 1200px width");
          //   return false;
          // }
          if (this.width < 500 ) {
            alert("Image width should be above 500 px");
            return false;
          }
          // else if (this.height > 700 ) {
          //   alert("Exceeded height (700 pixels).Please upload below 700px height");
          //   return false;
          // }
          else if (this.height < 500 ) {
            alert("Image height should above be 500 px");
            return false;
          }
          else if (this.size >1024*1000 ) {
            // alert("Image height is (700 pixels).Please upload above 650px height");
            alert("please upload less than 1MB");
            return false;
          }
          else{
            return true;
          }
         // access image size here & do further implementation
        };
      };
      //max size 50kb => 50*1000
      // if( size > 1024*2000){
      //  alert('Please upload less than 2mb file');
      //  return false;
      // }
      // else{
      //   $('.user_fields').show();
      //   return true;
      // }
      
    });

//banner image upload validation
$(document).on('change','.banner',function(){
    files = this.files;
    size = files[0].size;
    if( size > 1024*2000){
      alert('Please upload less than 2mb file');
        $('.simpleFilePreview_filename').remove();
      // // show styled input "button"
        $('.simpleFilePreview_remove').hide().end().find('.simpleFilePreview_preview ').remove();
      // $('.simpleFilePreview_preview ').remove();
       $('.banner').removeClass('simpleFilePreview_formInput');
       $('.simpleFilePreview_input').show();
       $('.banner').addClass('simpleFilePreview_formInput');
       return false;
    }
    else{
       $('.banner').addClass('simpleFilePreview_formInput');
       
    }
});


  // user validation
// $('#postevent').click(function(){
//     var mobile =$('.mobile').val(); 
//     var pattern = /^\d{10}$/;

//   if($('.name').val() == ''){
//       $(this).addClass("sf-error")
//       return false;
//     }
//     else{
//       $("#sf-msg").text("");
//     }
//     if($('.email').val() == ''){
//       $('.email').addClass("sf-error");
//       $("#sf-msg").text("Please enter email address");
//       return false;
//     }
//     // else if( !isValidEmailAddress( $('.email').val() )){
//     //   $('.email_error').show().text('Enter Valid emailAddress');
//     //   return false;
//     // }
//     else{
//       $("#sf-msg").text("");
//       $('.email').removeClass("sf-error");
//     }
//     if($('.mobile').val() == '' ){
//       $('.mobile').addClass("sf-error");
//       $("#sf-msg").text("Please enter mobile number");
//       return false;
//     }
//     else if(!pattern.test(mobile)){
//       $("#sf-msg").text("It is not valid mobile number.input 10 digits number!");
//       return false;
//     }
//     else{
//      $("#sf-msg").text("");
//       $('.mobile').removeClass("sf-error");
//       return true;
//     }
//   $.cookie('name',$('.name').val(),{path: '/',raw: true});
//   $.cookie('email',$('.email').val(),{path: '/',raw: true});
//   $.cookie('mobile',$('.mobile').val(),{path: '/',raw: true});
// });


  //upload banner validation

  jQuery('#banner_upload').click(function(){
    if(!$('.banner').val()){
            $(this).addClass("error_input_field");
            $('.imageError').show();
            return false;
        }
        else{
          $(this).removeClass("error_input_field");
          $('.imageError').hide(); 
        }
    if($('.pageurl_required').val() == 'Select Page URL'){
            $(this).addClass("error_input_field");
            $('.pageurl_labelError').show();
            return false;
        }
        else{
          $(this).removeClass("error_input_field");
          $('.pageurl_labelError').hide(); 
        }
    if($('.position_required').val() == 'position_required'){
            $(this).addClass("error_input_field");
            $('.position_labelError').show();
            return false;
        }
        else{
          $(this).removeClass("error_input_field");
          $('.position_labelError').hide(); 
        }
    if($('.price_required').val() == 'Select Price'){
            $(this).addClass("error_input_field");
            $('.price_labelError').show();
            return false;
        }
        else{
          $(this).removeClass("error_input_field");
          $('.price_labelError').hide(); 
          $('form[name="upload_banner"]').submit();
          $('.banner_price').text($('#price_required').val());     
          return true;
        }

});

  // $('#mobile_signup').keyup(function(){
  //   mobile_validation($(this));
  // });

  $('#id_password').keyup(function(){
     strength_status = checkStrength($('#id_password').val());
     // alert(strength_status);
     $('#id_password').addClass("error_input_field"); 
     error = $(this).next().next('.error').text(strength_status);
     if (error.html() == "Too short" || error.html() == "Weak")
      $(this).next().next('.error').css({"color":"#900"});
     else if (error.html() == "Fair")
      $(this).next().next('.error').css({"color":"#e4b200"});
     else if (error.html() == "Good")
      $(this).next().next('.error').css({"color":"#3b5998"});
     else if (error.html() == "Strong" )
      $(this).next().next('.error').css({"color":"#2ab558"});
    $(this).next('.error').hide(); 
    error.show();
  });

});

      function mobile_validation(id){
        var mob = /^[1-9]{1}[0-9]{9}$/;
        var txtMobile =$(id).val();
        // alert(txtMobile.length);
        if (txtMobile == ""){
          $(id).addClass("error_input_field"); 
          $(id).next().next('.error').hide();
          $(id).next('.error').show();
        }
        else if (mob.test(txtMobile) == false) {
        $(id).addClass("error_input_field"); 
        $(id).next('.error').hide();
        $(id).next().next('.error').show();
        // txtMobile.focus();
        } 
        else{
        $(id).removeClass("error_input_field"); 
        $(id).next('.error').hide();   
        $(id).next().next('.error').hide();
        }
      }

    function checkStrength(password){
      //initial strength
      var strength = 0
   
      //if the password length is less than 6, return message.
      if (password.length < 6) 
          return 'Too short'
   
      //length is ok, lets continue.
   
      //if length is 8 characters or more, increase strength value
      if (password.length > 7) strength += 1
   
      //if password contains both lower and uppercase characters, increase strength value
      if (password.match(/([a-z].*[A-Z])|([A-Z].*[a-z])/))  strength += 1
   
      //if it has numbers and characters, increase strength value
      if (password.match(/([a-zA-Z])/) && password.match(/([0-9])/))  strength += 1 
   
      //if it has one special character, increase strength value
      if (password.match(/([!,%,&,@,#,$,^,*,?,_,~])/))  strength += 1
   
      //if it has two special characters, increase strength value
      if (password.match(/(.*[!,%,&,@,#,$,^,*,?,_,~].*[!,",%,&,@,#,$,^,*,?,_,~])/)) strength += 1
   
      //now we have calculated strength value, we can return messages
   
      //if value is less than 2
      if (strength < 2 ) 
          return 'Weak'
      else if (strength == 2 )
          return 'Fair'
      else if (strength == 3 ) 
          return 'Good'
      else 
          return 'Strong'

}  
$('.payment').hide();
$('#paid').click(function(){
  $('.payment').toggle();
});

var thewidth=$('.advertisement img').width();
var theheight=$('.advertisement img').height();
//$('.advertisement img').css({'margin-left':-thewidth/2+'px','margin-top':-theheight/2+'px'});


$('.addnum').hide();
    $(".plus").click(function(){
        $(".addnum").toggle();
    });

$('.addnum').hide();
    $(".edit").click(function(){
        $(".addnum").toggle();
    });
    

$(".confirm").click(function(){
        $(".addnum").hide();
    });

 // Organizer mobile number add with popup done by Ramya

    var max_fields      = 2; //maximum input boxes allowed
    var wrapper         = $(".addnum"); //Fields wrapper
    var add_button      = $(".btn_plus1"); //Add button ID
   
    var x = 1; //initlal text box count
    $(add_button).click(function(e){ //on add input button click
        e.preventDefault();
        if(x < max_fields){ //max input box allowed
            x++; //text box increment
            $(wrapper).append("<div class='block'><input type='text' placeholder='Organizer mobile' name='organizer_mobile[]' id='organizer_mobile_"+ x + "' class='organizermobile' value='' data-number='true'><img src='media/static/img/close.png' alt='close' class='btn_close1' '33px' width='20px'></div>"); //add input box
        }
    });
   
    $(wrapper).on("click",".btn_close1", function(e){ //user click on remove text
        e.preventDefault(); $(this).parent('div').remove(); x--;
    });

    var mobile_number = '';
    var number = '';
    $(document).on('click','#number_add_act', function(){
      length = $('.organizermobile').length;
      mobile_number = $('.organizer_mobile').val().split(',')[0];
      $('.organizermobile').each(function(index){
         if(index == length - 1)
          number = number + $(this).val()
         else
          number = number + $(this).val() + ',';
      });
      // alert(number);
      if($('.organizer_mobile, .organizermobile').val() == '')
        $('.organizer_mobile').val(number);  
      else
        $('.organizer_mobile').val(mobile_number + ',' + number);
      number= '';
    });
  
// $(".signup").click(function(){
//     $(".email").show();
// }); 

// $(".signin").click(function(){
//     $(".email").hide();
// });

// $(".upload_image").find('.simpleFilePreview_inputButtonText').text("UPLOAD A IMAGE");

$('.privacy_content').hide();
$(".privacy").click(function(){
    $('.privacy_content').show();
    $(".profile ,.myevents_content").hide();
});

$(".info").click(function(){
    $('.profile').show();
    $(".privacy_content ,.myevents_content").hide();
});
$('.myevents_content').hide();
$(".myevents").click(function(){
    $('.myevents_content').show();
    $(".profile,.privacy_content").hide();
});

$(".dropdown").click(function(){
        $(".menulist").toggle();
});

$("#page-content").on('click', function (){
   $('.select-clone').hide();     
  });

// $('.save_personal').click(function(){
//   alert('profile'+$('input[type="file"]#profile_poster').val());
//   $.post("/user_profile/", $('#userprofile').serialize(),
//       function (data) {
//         alert("success");
//   });
//   return false;
// });

$('.save_privacy').click(function(){
  
 $.ajax({

               type:"POST",
               url:"/privacy/",
               data: {
                      'newpassword': $('#newpassword').val(),
                      'confirmpassword': $('#confirmpassword').val(),
                    },
               success: function(){
                  alert('password changed successfully');
                  }
          });
       $('#newpassword').val('');
       $('#confirmpassword').val('');
       return false;
});
