$(function(){
  $('#imgInp').change(function(){
    var input = this;
    var url = $(this).val();
    var ext = url.substring(url.lastIndexOf('.') + 1).toLowerCase();
    if (input.files && input.files[0]&& (ext == "gif" || ext == "png" || ext == "jpeg" || ext == "jpg")) 
     {
        var reader = new FileReader();

        reader.onload = function (e) {
        //    $('#img').attr('src', e.target.result);
            $(".left_menu_img").css("background-image", 'url(' + e.target.result + ')');
            console.log("changed img" + e.target.result);
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