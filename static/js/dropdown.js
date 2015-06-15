    $(function(){
    $(".dropdown").hover(
            function() {
                $('.dropdown-menu', this).fadeIn("fast");
                $('b', this).toggleClass("caret caret-up");
            },
            function() {
                $('.dropdown-menu', this).fadeOut("fast");
                $('b', this).toggleClass("caret caret-up");
            });
    });
