// UOU Selects
// ---------------------------------------------------------
$.fn.uouCustomSelect = function () {
    var $select = $(this);
    $select.wrap('<div class="uou-custom-select"></div>');
    var $container = $select.parent('.uou-custom-select');
    $container.append('<ul class="select-clone"></ul>');
    var $list = $container.children('.select-clone'),
    placeholder = $select.data('placeholder') ? $select.data('placeholder') : $select.find('option:eq(0)').text();
    $('<input class="value-holder" type="hidden" disabled="disabled" placeholder="' + placeholder + '"><span class="placeholder">' + placeholder + '</span><i class="fa fa-chevron-down"></i>').insertBefore($list);
    var $valueHolder = $container.children('.value-holder');
    var $valuePlaceholder = $container.children('.placeholder');
    $select.find('option').each(function () {
        var $this = $(this);
        $list.append('<li data-value="' + $this.val() + '">' + $this.text() + '</li>');
    });
    // Toggle list
    $container.on('click', function () {
      // console.log('click ' + $container);
      $container.toggleClass('active');
      $list.slideToggle(250);
    });
    // Option Select
   $list.delegate('li','click', function () {
        var $this = $(this);
        var id_value = $this.attr('data-value');     
        $valueHolder.val(id_value);
        $valuePlaceholder.html($this.text());
        // $(input.valueHolder).parent().next('input[type="hidden"]#subcategoryid').val(id_value);
        $select.find('option[value="' + $this.data('value') + '"]').prop('selected', true);
        // if ($this.parent('select-clone').siblings('select').hasClass('select_city'))
        if ($this.parents().children().hasClass('select_city'))
        { 
        
            if ($this.parent().siblings('.placeholder').text() != "Select City")
            find_colleges($this.data('value'));
        }
        if ($this.parents().children().hasClass('select_college')){
            if ($this.parent().siblings('.placeholder').text() != "Select College")
            find_department($this.data('value'));
        }
        if ($this.parents().children().hasClass('select_category'))
        {
            if ($this.parent().siblings('.placeholder').text() != "Event Category")
            find_subcategory($this.data('value'));
        }
        if ($this.parents().children().hasClass('select_state'))
        {
            if ($this.parent().siblings('.placeholder').text() != "State")
            find_city($this.data('value'));
        }
        if ($this.parents().children().hasClass('pageurl_required'))
        {
            if ($this.parent().siblings('.placeholder').text() != "Select Page URL")
            if ($this.data('value')=='/')
            {
                find_position('home');
            }
            else if($this.data('value')=='event/')
            {
                find_position('list');
            }
            else
            {
                find_position('details');
            }
        } 
        if ($this.parents().children().hasClass('position_required'))
        {
            if ($this.parent().siblings('.placeholder').text() != "Select Position")
            var page=$('#pageurl_required').val();
            if (page=='/')
            {
                var path='home';
            }
            else if(page=='event/')
            {
                var path='list';
            }
            else
            {
                var path='details';
            }
            find_price($this.data('value'),path);
        }  
        if ($this.parents().children().hasClass('festtype'))
            $select.find('option[value="' + $this.data('value') + '"]').attr('selected', true);  

    });
    // Hide
    $container.on('clickoutside touchendoutside mouseoveroutside', function () {
        if (!dragging) {
            $container.removeClass('active');
            $list.slideUp(250);
        }
    });
    // Links
    if ($select.hasClass('links')) {
        $select.on('change', function () {
            window.location.href = select.val();
        });
    }

    $select.on('change', function () {
        console.log(changed);
        console.log($(this).val());
    });
};
    $('select').each(function () {
        $(this).uouCustomSelect();
    });
    function find_position(path){
        $.get('/find_position/', { path: path }, function(data) {
            $('.position_required').empty();
            $(".position_required").siblings('.select-clone').empty();
            $('.position_required').html($('<option>').text("Select Position").attr('value', "position_required"));
            $(".position_required").siblings('.select-clone').html($('<li>').text("Select Position").attr('data-value', "position_required"));
      
            $.each(data, function(key,value) {
                $('.position_required').append($('<option>').text(value.name).attr('value', value.name));
                $(".position_required").siblings('.select-clone').append($('<li>').text(value.name).attr('data-value', value.name));
            });
        });
    }

    function find_price(position,path){
        $.get('/find_price/', { position: position,path: path }, function(data) {
            $.each(data, function(key,value) {
                $(".price_required").val(value.name);
                $('.banner_price_act').text('Amount: '+value.name)
            });
        });
    }
    
