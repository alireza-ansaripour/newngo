
$(document).ready(function() {
    $('#summernote').summernote();
    $('.note-editable').attr('dir','rtl')



});
$("#click").click(function(){
    var st = $('#summernote').code();
    alert("sending")


    $.ajax({
            type:"POST",
            beforeSend: function (request)
            {
                request.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
            },
            data:{
                'ali':'reza'
            },
            url: "http://127.0.0.1:8000/new/",
            //processData: false,
            success: function(msg) {
                alert(msg)
            }
    });




});

$('#submit').click(function(){

});
