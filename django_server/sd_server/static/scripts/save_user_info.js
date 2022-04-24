function save_user_info(){
  var continue_next = true;
  switch(true){
    case (!$("#sign_up_name").val()):
      alert("Input Your Name");
      continue_next = false;
    break;

    case (!$("#sign_up_lastname").val()):
      alert("Input Your Lastname");
      continue_next = false;
    break;
    case (!$("#sign_up_username").val()):
      alert("Input a username")
      continue_next = false; 
      break;
    case (!$("#sign_up_birthday").val()):
      alert("Input Your Birthday");
      continue_next = false;
    break;

    case (!$("#sign_up_country").val()):
      alert("Input Your Country");
      continue_next = false;
    break;

    case (!$("#sign_up_gender").val()):
      alert("Input Your Gender");
      continue_next = false;
    break;
  }
  if($("#sign_up_mail").val() != $("#sign_up_password").val()){
    alert("password not the same");
    return;
  }

  if(continue_next == false) return;

  let user_register_data;

  if($("#sign_up_password").val() && ($("#sign_up_password").val().length > 0)){
    let pass = $("#sign_up_password").val();
    let pass_md5 = $.md5(pass + 'ABCDE');
    user_register_data = {"user_name"     :   $('#sign_up_name').val(),
                              "user_lastname" :   $('#sign_up_lastname').val(),
                              "user_password" :   pass_md5.toUpperCase(),
                              "user_birthday" :   $('#sign_up_birthday').val(),
                              "user_country"  :   $('#sign_up_country').val(),
                              "user_gender"   :   $('#sign_up_gender').val()
                            };
  } else{
    user_register_data = {"user_name"     :   $('#sign_up_name').val(),
                              "user_lastname" :   $('#sign_up_lastname').val(),
                              "user_birthday" :   $('#sign_up_birthday').val(),
                              "user_country"  :   $('#sign_up_country').val(),
                              "user_gender"   :   $('#sign_up_gender').val()
                            };

  }

  $.ajax({
    type            : "POST",
    url             : "/updateUserDataNow",
    data            : JSON.stringify(user_register_data),
    contentType     : "application/json; charset=utf-8",
    success         : function(data){
      alert("Data Updated");
    }
  })
}





async function change_vals(ob){
  var now = new Date();

  var day = ("0" + now.getDate()).slice(-2);
  var month = ("0" + (now.getMonth() + 1)).slice(-2);

  var today = now.getFullYear()+"-"+(month)+"-"+(day) ;

          $("#sign_up_name").val(ob.name);
          $('#sign_up_lastname').val(ob.lastname);
          $("#sign_up_country").val(ob.country);
          $("#sign_up_username").val(ob.username);
          $("#sign_up_birthday").val(today);
          $("#sign_up_gender").val(ob.gender);

}

window.onload =function initial_values_user_info(){
  // request data via post
  let petition ={ "give" : "True" }
  $.ajax({
        type          :"POST",
        url           :"/giveMeUserData",
        data          :JSON.stringify(petition),
        contentType   :'application/json; charset=utf-8',
        success       :function(data){
          var jso = JSON.stringify(data);
          var obj  = JSON.parse(jso);
          change_vals(obj);
        }
  });
  // $.ajax({
  //   ""
  // })

}



function log_me_out(){
  document.cookie = 'login_session' +'=; Path=/; Expires=Thu, 01 Jan 1970 00:00:01 GMT;';
  window.location.href = "/login";
}