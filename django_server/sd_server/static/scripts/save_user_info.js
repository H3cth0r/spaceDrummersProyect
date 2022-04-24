function save_user_info(){
    alert("User data saved");
}


function log_me_out(){
  document.cookie = 'login_session' +'=; Path=/; Expires=Thu, 01 Jan 1970 00:00:01 GMT;';
  window.location.href = "/login";
}