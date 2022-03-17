

function process_register_data(){
    let user_register_data = {'user_name':      $('#sign_up_name').val(),
                              'user_lastname':  $('#sign_up_lastname').val(),
                              'user_mail':      $('#sign_up_mail').val(),
                              'user_password':  $('#sign_up_password').val(),
                              'user_birthday':  $('#sign_up_birthday').val(),
                              'user_country':   $('#sign_up_country').val(),
                              'user_gender':    $('#sign_up_gender').val()
                            };
    console.log(user_register_data);
    window.location.href = "user_info.html";
}

// function process_login_data(){

// }