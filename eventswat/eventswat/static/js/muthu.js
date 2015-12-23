$(document).ready(function(){

//**************************** start of combobox settings*********************//
    //This is for jquery combobox.User type and select funtion only of textbox
    (function( $ ) {
      $.widget( "custom.combobox", {
        _create: function() {
          this.wrapper = $( "<span>" )
            .addClass( "custom-combobox" )
            .insertAfter( this.element );

          this.element.hide();
          this._createAutocomplete();
          this._createShowAllButton();
        },

        _createAutocomplete: function() {
          var selected = this.element.children( ":selected" ),
            value = selected.val() ? selected.text() : "";

          this.input = $( "<input>" )
            .appendTo( this.wrapper )
            .val( value )
            .attr( "title", "" )
            .addClass( "custom-combobox-input ui-widget ui-widget-content ui-state-default ui-corner-left" )
            .autocomplete({
              delay: 0,
              minLength: 0,
              source: $.proxy( this, "_source" )
            })
            .tooltip({
              tooltipClass: "ui-state-highlight"
            });

          this._on( this.input, {
            autocompleteselect: function( event, ui ) {
              ui.item.option.selected = true;
              this._trigger( "select", event, {
                item: ui.item.option
              });
            },

            autocompletechange: "_removeIfInvalid"
          });
        },

        _createShowAllButton: function() {
          var input = this.input,
            wasOpen = false;

          $( "<a>" )
            .attr( "tabIndex", -1 )
            .attr( "title", "Show All Items" )
            .tooltip()
            .appendTo( this.wrapper )
            .button({
              icons: {
                primary: "ui-icon-triangle-1-s"
              },
              text: false
            })
            .removeClass( "ui-corner-all" )
            .addClass( "custom-combobox-toggle ui-corner-right" )
            .mousedown(function() {
              wasOpen = input.autocomplete( "widget" ).is( ":visible" );
            })
            .click(function() {
              input.focus();

              // Close if already visible
              if ( wasOpen ) {
                return;
              }

              // Pass empty string as value to search for, displaying all results
              input.autocomplete( "search", "" );
            });
        },

        _source: function( request, response ) {
          var matcher = new RegExp( $.ui.autocomplete.escapeRegex(request.term), "i" );
          response( this.element.children( "option" ).map(function() {
            var text = $( this ).text();
            if ( this.value && ( !request.term || matcher.test(text) ) )
              return {
                label: text,
                value: text,
                option: this
              };
          }) );
        },

        _removeIfInvalid: function( event, ui ) {

          // Selected an item, nothing to do
          if ( ui.item ) {
            return;
          }

          // Search for a match (case-insensitive)
          var value = this.input.val(),
            valueLowerCase = value.toLowerCase(),
            valid = false;
          this.element.children( "option" ).each(function() {
            if ( $( this ).text().toLowerCase() === valueLowerCase ) {
              this.selected = valid = true;
              return false;
            }
          });

          // Found a match, nothing to do
          if ( valid ) {
            return;
          }

          // Remove invalid value
          this.input
            .val( "" )
            .attr( "title", value + " didn't match any item" )
            .tooltip( "open" );
          this.element.val( "" );
          this._delay(function() {
            this.input.tooltip( "close" ).attr( "title", "" );
          }, 2500 );
          this.input.autocomplete( "instance" ).term = "";
        },

        _destroy: function() {
          this.wrapper.remove();
          this.element.show();
        }
      });
  })( jQuery );
//********************  End of combobox   ********************************//

//combobox settings select element
$(function() {
  $( "#id_country" ).combobox();
  $( "#id_state" ).combobox();
  $( "#id_city" ).combobox();
});

//Populate state Ajax calling when user select country in postevent page change function
$("#id_country").combobox({
    select: function (event, ui) {
        var country = $(this).val();
        $.get('/postevent/load_state/', { country: country }, function(data) {
            $('#id_state').empty();
            $.each(data, function(key,value) {
                $('#id_state').append($('<option>').text(value.value).attr('value', value.label));
            });//end of each loop
        });// end of $.get
    }//end of select function
});//End of combobox of id country

//Populate cities Ajax calling when user select state in postevent page like change function
$("#id_state").combobox({
    select: function (event, ui) {
        var state = $(this).val();
        $.get('/postevent/load_city/', { state: state }, function(data) {
            $('#id_city').empty();
            $.each(data, function(key,value) {
                $('#id_city').append($('<option>').text(value.value).attr('value', value.label));
            });//end of each loop
        }); // end of $.get
    }//end of select function
});//End of combobox of id state

$('#id_event_category').change(function(){
    var id= $(this).val();
    $.get('/postevent/admin_subcategory/', { id: id }, function(data) {
        $('#id_event_subcategory').empty();
        $('.field-event_subcategory').show();
        $.each(data, function(key,value) {
            $('#id_event_subcategory').append($('<option>').text(value.name).attr('value', value.id));
        });//end of each loop
    });// end of $.get
});// end of id event category

// file uploading in postevent event page
$("#event_poster").filer({
        limit: 4,
        maxSize: 2,
        extensions: ['jpg', 'jpeg', 'png'],
        changeInput: '<div class="jFiler-input-dragDrop"><div class="jFiler-input-inner"><div class="jFiler-input-icon"><i class="icon-jfi-cloud-up-o"></i></div><div class="jFiler-input-text"><h3>Drag&Drop files here</h3> <span style="display:inline-block; margin: 15px 0">or</span></div><a class="jFiler-input-choose-btn blue">Browse Files</a></div></div>',
        showThumbs: true,
        theme: "dragdropbox",
        templates: {
            box: '<ul class="jFiler-items-list jFiler-items-grid"></ul>',
            item: '<li class="jFiler-item">\
                        <div class="jFiler-item-container">\
                            <div class="jFiler-item-inner">\
                                <div class="jFiler-item-thumb">\
                                    <div class="jFiler-item-status"></div>\
                                    <div class="jFiler-item-info">\
                                        <span class="jFiler-item-title"><b title="{{fi-name}}">{{fi-name | limitTo: 25}}</b></span>\
                                        <span class="jFiler-item-others">{{fi-size2}}</span>\
                                    </div>\
                                    {{fi-image}}\
                                </div>\
                                <div class="jFiler-item-assets jFiler-row">\
                                    <ul class="list-inline pull-left">\
                                        <li>{{fi-progressBar}}</li>\
                                    </ul>\
                                    <ul class="list-inline pull-right">\
                                        <li><a class="icon-jfi-trash jFiler-item-trash-action"></a></li>\
                                    </ul>\
                                </div>\
                            </div>\
                        </div>\
                    </li>',
            itemAppend: '<li class="jFiler-item">\
                            <div class="jFiler-item-container">\
                                <div class="jFiler-item-inner">\
                                    <div class="jFiler-item-thumb">\
                                        <div class="jFiler-item-status"></div>\
                                        <div class="jFiler-item-info">\
                                            <span class="jFiler-item-title"><b title="{{fi-name}}">{{fi-name | limitTo: 25}}</b></span>\
                                            <span class="jFiler-item-others">{{fi-size2}}</span>\
                                        </div>\
                                        {{fi-image}}\
                                    </div>\
                                    <div class="jFiler-item-assets jFiler-row">\
                                        <ul class="list-inline pull-left">\
                                            <li><span class="jFiler-item-others">{{fi-icon}}</span></li>\
                                        </ul>\
                                        <ul class="list-inline pull-right">\
                                            <li><a class="icon-jfi-trash jFiler-item-trash-action"></a></li>\
                                        </ul>\
                                    </div>\
                                </div>\
                            </div>\
                        </li>',
            progressBar: '<div class="bar"></div>',
            itemAppendToEnd: false,
            removeConfirmation: true,
            _selectors: {
                list: '.jFiler-items-list',
                item: '.jFiler-item',
                progressBar: '.bar',
                remove: '.jFiler-item-trash-action'
            }
        },
        dragDrop: {
            dragEnter: null,
            dragLeave: null,
            drop: null,
        },
        addMore: true,
        options: null,
        captions: {
            button: "Choose Files",
            feedback: "Choose files To Upload",
            feedback2: "files were chosen",
            drop: "Drop file here to Upload",
            removeConfirmation: "Are you sure you want to remove this file?",
            errors: {
                filesLimit: "Only {{fi-limit}} files are allowed to be uploaded.",
                filesType: "Only Images are allowed to be uploaded.",
                filesSize: "{{fi-name}} is too large! Please upload file up to {{fi-maxSize}} MB.",
                filesSizeAll: "Files you've choosed are too large! Please upload files up to {{fi-maxSize}} MB."
            }
        }
    });//end fo file uploading

    //postevent datetimepicker settings
    $(function(){
        $('#startdate').datetimepicker({
            format:'Y-m-d H:i',
            onShow:function( ct ){
                this.setOptions({
                    maxDate:$('#enddate').val()?$('#enddate').val():false
                })
            },
            timepicker:true,
            validateOnBlur:true,
            minDate:'+1970/01/02',
            onClose:function( ct ){
                $('#datetimepicker1').focus();
            },
        });

        $('#enddate').datetimepicker({
            format:'Y-m-d H:i',
            onShow:function( ct ){
                var start_date = ($('#startdate').val());
                var replace_date = start_date.replace(/-/g,'/');
                var spilit_date = replace_date.split(/ +/);
                this.setOptions({
                    minDate:$('#startdate').val()?spilit_date[0]:false,
                    minTime:$('#startdate').val()?spilit_date[1]:false,
                })
            },
            timepicker:true,
            validateOnBlur:true,
        });
    });// end postevent datetimepicker settings

    //check for valid url
    function isValidUrl(url){
        var re = /^(http|https|ftp):\/\/[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?$/i
        return re.test(url);
    }
    //Email validation
    function validateEmail(email) {
        var re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        return re.test(email);
    }
    //postevent form validation
    $('#postevent_submit').click(function(){

        var event_title = $('#event_title').val();

        if($('#id_event_category').val()==''){
            $('.category_error').show();
            return false;
        }
        else{
            $('.category_error').hide();
        }
        if($('#id_event_subcategory').val()==''){
            $('.subcategory_error').show();
            return false;
        }
        else{
            $('.subcategory_error').hide();
        }
        if(event_title == "" || event_title.length > 25){
            $('.event_title_error').show();
            return false;
        }
        else{
            $('.event_title_error').hide();
        }
        if($('#startdate').val()==""){
            $('.start_date_error').show();
            return false;
        }
        else{
            $('.start_date_error').hide();
        }
        if($('#enddate').val()==""){
            $('.end_date_error').show();
            return false;
        }
        else{
            $('.end_date_error').hide();
        }
        var desc = $('#event_desc').val();
        if($('#event_desc').val()==""|| desc.length > 500){
            $('.event_desc_error').show();
            return false;
        }
        else{
            $('.event_desc_error').hide();
        }
        var cond = $('#term_and_cond').val();
        if($('#terms_and_cond_check').is(':checked')){
            if($('#term_and_cond').val()==""|| cond.length > 500){
                $('.term_and_cond_error').show();
                return false;
            }
            else{
                $('.term_and_cond_error').hide();
            }
        }
        else{
            $('.term_and_cond_error').hide();
        }

        if($('#website').val()){
            if(!isValidUrl($('#website').val())){
                $('.website_error').show();
                return false;
            }
            else{
                $('.website_error').hide();
            }
        }
        if(!$('#is_webniar').is(':checked')){
            if($('#vanue').val()==''){
                $('.vanue_error').show();
                return false;
            }
            else {
                $('.vanue_error').hide();
            }
            if($('#id_country').val()==''){
                $('.country_error').show();
                return false;
            }
            else {
                $('.country_error').hide();
            }
            if($('#id_state').val()==''){
                $('.state_error').show();
                return false;
            }
            else {
                $('.state_error').hide();
            }
            if($('#id_city').val()==''){
                $('.city_error').show();
                return false;
            }
            else {
                $('.city_error').hide();
            }
        }
        if($('#org_name').val()==""){
            $('.org_name_error').show();
            return false;
        }
        else {
            $('.org_name_error').hide();
        }
        if($('#org_email').val()==""){
            $('.org_email_error').show();
            return false;
        }
        else if(!validateEmail($('#org_email').val())){
            $('.org_email_error').show();
            return false;
        }
        else{
            $('.org_email_error').hide();
        }
        var mob = /^[1-9]{1}[0-9]{9}$/;
        if (mob.test($('#org_mobile').val()) == false) {
            $('.org_mobile_error').show();
            return false;
        }
        else{
            $('.org_mobile_error').hide();
            return true;
        }
    });
});//End of Doucment ready
