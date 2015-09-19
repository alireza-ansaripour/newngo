/**
 * Created by alireza on 19/09/15.
 */
$(document).ready(function(){
    $('#summernote').summernote();
    $('button').click(function(){
        var text = $('#summernote').code();
        $.ajax({
            type:'UPDATE',
            data:{
                text:text
            },
            beforeSend: function (request)
            {
                request.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
            },
            success:function(data){
                alert(data);
            }
        });
    });
    $('input').click(function(){
        $.ajax({
            type:'DELETE',
            beforeSend: function (request)
            {
                request.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
            },
            success:function(data){
                alert(data);
            }
        });
    });
});