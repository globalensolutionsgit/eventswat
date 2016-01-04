$("document").ready(function(){
//function to align popup in center of the page

	jQuery.fn.center = function () {
	    this.css("top", ( jQuery(window).height() - this.height() ) / 2+jQuery(window).scrollTop()+100 + "px");
	    return this;
  	}
  
	$(window).scroll(function (){
	   $(".popup_pos").center();
	       
	});
	var body_win_height = parseInt(document.body.clientHeight) ;
  	var win_height = parseInt(document.documentElement.clientHeight) ;

	if( body_win_height > win_height) {
	      $('.popup_fade').height(body_win_height);
	}
	else {
	      $('.popup_fade').height(win_height);
	}
	  
	$(".popup_pos").center();


	$('.popup_cancel_btn').on('click',function() {
	    $('.pop_up').hide();
	    $('.popup_fade').hide();
	});



	$("a").click(function(e){
		if($(this).attr("href") === '#'){
		  e.preventDefault();
		}
	});

//cancel and close popup
  $('.cancel_btn, .close_btn').on('click', function (){      
      $('.popup_fade,#forgotpassword_popup,#resetpassword_popup, #signin_popup,#signup_popup').hide();      
      $('.search_bar').show();
     
  });

//signup popup
	$('.register, .signup').on('click', function(){
	   $('.popup_fade, #signup_popup').show();       
	   $('.header-search-bar, #signin_popup').hide();       

	});

//forgetpassword popup

  $(".forget_password").on('click', function (){
     $('#signup_popup, #signin_popup').hide();
     $('.popup_fade, #forgotpassword_popup').show();
  });


//signin popup

	$(".login_act, .login_button, .signin").on('click', function (){        
        $('.popup_fade, #signin_popup').show();       
        $('.search_bar,  #signup_popup').hide();       
  });

//postevent act if user is not authenticated

  $('.post_event_btn_act').on('click', function(){  
    $('input[name="next"]').val('/postevent');
  });


//postbanner act if user is not authenticated

  $('.upload_banner_btn_act').click(function(){
    $('input[name="next"]').val('/banner');
  });


//dropdown act for userprofile

  $(".dropdown").click(function(){
        $(".menulist").toggle();
  });


//mobile number validation in signup popup

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
              // alert("id_email"+id_email);
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
       
 });

 //end signup validation//

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

//payu form hide
$('.payment').hide();
$('#paid').click(function(){
  $('.payment').toggle();
});

// function for choosing banner plan 
$("ul li.plan_choose_act").on('click', function(){
  var plan = $(this).val();
  // alert('plan'+plan);  
  var hidden_plan = $(this).siblings('.hidden_plan').val(); 
  $('input[name="hidden_bannerplan"]').val(hidden_plan);
  
  var page = $(this).siblings('.hidden_page').val();
  // alert($(this).siblings('.hidden_page').val()); 
  $('input[name="banner_page"]').val(page);
 
  var position = $(this).siblings('.hidden_position').val();
  // alert($(this).siblings('.hidden_position').val());  
  $('input[name="banner_position"]').val(position);

  var price = $(this).siblings('.hidden_price').val();
  // alert($(this).siblings('.hidden_price').val());  
  $('input[name="banner_price"]').val(price);
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


});