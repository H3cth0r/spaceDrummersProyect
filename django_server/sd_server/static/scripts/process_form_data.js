

function process_register_data(){

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

    case (!$("#sign_up_mail").val()):
      alert("Input Your Mail");
      continue_next = false;
    break;

    case (!$("#sign_up_password").val()):
      alert("Input Your Password");
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

    let user_register_data = {'user_name':      $('#sign_up_name').val(),
                              'user_lastname':  $('#sign_up_lastname').val(),
                              'user_mail':      $('#sign_up_mail').val(),
                              'user_password':  $('#sign_up_password').val(),
                              'user_birthday':  $('#sign_up_birthday').val(),
                              'user_country':   $('#sign_up_country').val(),
                              'user_gender':    $('#sign_up_gender').val()
                            };
    console.log(user_register_data);
    /*if(continue_next==true)window.location.href = "user_info.html";*/
}

function process_login_data(){
  var continue_next = true;
  let user_login_data = {'usernameORpassword': $("#log_in_username").val(),
                         'password':           $("#log_in_password").val()};
  console.log(user_login_data);
  switch(true){
    case (!$("#log_in_username").val()):
      alert("Input your username");
      continue_next = false;
    break;

    case (!$("#log_in_password").val()):
      alert("Input Your Password");
      continue_next = false;
    break;
  }

  /*if(continue_next==true)window.location.href  = "user_info.html";*/
}