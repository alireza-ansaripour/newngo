$('.note-editable').attr('dir','rtl');
function summernote(){
        $('#summernote').summernote();
        $('#submit').css('visibility', 'visible');
        $('.note-editable').attr('dir','rtl');

    }
    function send(ngo){
        var text = $('#summernote').code();
        $.ajax({
            type:"POST",
            beforeSend: function (request)
            {
                request.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
            },
            data:{
                'about':text
            },
            url: "http://127.0.0.1:8000/ngo/"+ngo+"/country/",
            //processData: false,
            success: function(msg) {
                alert('اطلاعات به روز شد');
                $('#summernote').destroy();
                 $('#submit').css('visibility', 'hidden');
            }
        });
    }

$('#submit').click(function(){

});
