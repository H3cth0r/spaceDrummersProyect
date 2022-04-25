$(function(){
  $('#imgInp').change(function(){
    var input = this;
    var url = $(this).val();
    var ext = url.substring(url.lastIndexOf('.') + 1).toLowerCase();
    if (input.files && input.files[0]&& (ext == "gif" || ext == "png" || ext == "jpeg" || ext == "jpg")) 
     {
        var reader = new FileReader();
        var the_result;

        reader.onload = function (e) {
            $(".left_menu_img").css("background-image", 'url(' + e.target.result + ')');
            the_result = e.target.result;
            console.log(the_result);
            var petition = {"img_base" : String(the_result)};
            $.ajax({
                    type        :"POST",
                    url         :"/takeThisPhoto",
                    data        :JSON.stringify(petition),
                    contentType :'application/json; charset=utf-8',
                    success     :function(data){
                      console.log("changed img == True");
                    }
            });
          }

        reader.readAsDataURL(input.files[0]);
       
    }
    else
    {
    //   $('#img').attr('src', '/assets/no_preview.png');
        console.log("invalid img input")
    }
  });
});