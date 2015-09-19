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
            'data':text
        },
        url: "http://176.9.177.17/ngo/"+ngo+"/country/",
        //processData: false,
        success: function(msg) {
            alert('اطلاعات به روز شد');
            $('#summernote').destroy();
             $('#submit').css('visibility', 'hidden');
        }
    });
}
function send(ngo,request){
    var text = $('#summernote').code();
    $.ajax({
        type:"POST",
        beforeSend: function (request)
        {
            request.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
        },

        data:{

            'data':text
        },
        url: "http://176.9.177.17/ngo/"+ngo+"/"+request+"/",
        //processData: false,
        success: function(msg) {
            alert('اطلاعات به روز شد');
            $('#summernote').destroy();
             $('#submit').css('visibility', 'hidden');
        }
    });
}
function delete_photo(id){
     $.ajax({
        type:"GET",
        url: "http://176.9.177.17/user/deletephoto/"+id+"/",
        //processData: false,
        success: function(msg) {
            location.reload()
        }
    });

}


