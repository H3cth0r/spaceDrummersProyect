

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
  if(continue_next == false) return;
  let pass = $('#sign_up_password').val();
  let pass_md5 = $.md5(pass + 'ABCDE');
  // let pass_md5 = 'noeslacontra'
  let user_register_data = {  "user_name"     :   $('#sign_up_name').val(),
                              "user_lastname" :   $('#sign_up_lastname').val(),
                              "user_mail"     :   $('#sign_up_mail').val(),
                              "user_username" :   $("#sign_up_username").val(),
                              "user_password" :   pass_md5.toUpperCase(),
                              "user_birthday" :   $('#sign_up_birthday').val(),
                              "user_country"  :   $('#sign_up_country').val(),
                              "user_gender"   :   $('#sign_up_gender').val()
                            };
  console.log(user_register_data);

  $.ajax({
        type        :"POST",
        url         :"/websiteRegister",
        data        :JSON.stringify(user_register_data),
        contentType :'application/json; charset=utf-8',
        success :function(data){
          var json = JSON.stringify(data);
          var obj  = JSON.parse(json);
          alert(obj.registered);
        }
  })
 
    /*if(continue_next==true)window.location.href = "user_info.html";*/
}

function process_login_data(){
  var continue_next = true;

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
  let pass            = $('#log_in_password').val()
  let pass_md5        = $.md5(pass + 'ABCDE')
  let user_login_data = {'username'   : $("#log_in_username").val(),
                         'password'   : pass_md5.toUpperCase()};
  console.log(user_login_data)

  $.ajax({
    type        : "POST",
    url         : "/loginRegister",
    data        : JSON.stringify(user_login_data),
    contentType : 'application/json; charset=utf-8',
    success     : function(data){
      var json  = JSON.stringify(data);
      var obj   = JSON.parse(json);
    }
  })

  location.replace('/user_info');

  /*if(continue_next==true)window.location.href  = "user_info.html";*/
}