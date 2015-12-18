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
    $.get('/admin_subcategory/', { id: id }, function(data) {
        $('#id_event_subcategory').empty();
        $('.field-event_subcategory').show();
        $.each(data, function(key,value) {
            $('#id_event_subcategory').append($('<option>').text(value.name).attr('value', value.id));
        });//end of each loop
    });// end of $.get
});// end of id event category

});//End of Doucment ready
