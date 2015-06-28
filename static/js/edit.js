
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
            url: "http://176.9.177.17/new/",
            //processData: false,
            success: function(msg) {
                alert(msg)
            }
    });




});

$('#submit').click(function(){

});
