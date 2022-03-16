// anime({
//     targets: '#to_animate_button_one',
//     translateY: -300,
//     duration:   1000,
//     easing: 'linear',
// });


let sign_up_up = false;
let log_in_up  = false;


function translate_up_or_down(html_object, to_translate, the_duration = 1000, the_easing='linear'){
    anime({targets: html_object, translateY: to_translate, duration: the_duration, easing: the_easing});
}



function on_click_sign_up(){
    // If it is already up exit function
    if(sign_up_up == true) return;
    // if the other login up div, move it down
    if(log_in_up == true){ 
        // 1. display form to none 
        $(".log_in_div_two").css("display", "none");
        $(".button_two").css("display", "none")
        // 2. move "a" fast to -200
        translate_up_or_down('#sign_up_a', -200, 1, 'linear');
        // 3. animate down to 0
        translate_up_or_down('#sign_up_a', 0, 1000, 'linear');
        log_in_up = false;
    }
    // Move up the sign up button
    translate_up_or_down('#sign_up_a', -200, 1000, 'linear');
    setTimeout(() => {
        $(".sign_up_div_two").css("display", "flex");
        $(".button_one").css("display", "block")
        // move sign up a down fast, so it is leveled
        translate_up_or_down('#sign_up_a', 0, 1, 'linear');
        }, 1000);
    sign_up_up = true;
}



function on_click_log_in(){
    // If it is already up exit function
    if(log_in_up == true) return;
    // if the other login up div, move it down
    if(sign_up_up == true){ 
        // 1. display form to none 
        $(".sign_up_div_two").css("display", "none");
        $(".button_one").css("display", "none")
        // 2. move "a" fast to -200
        translate_up_or_down('#login_a', -200, 1, 'linear');
        // 3. animate down to 0
        translate_up_or_down('#login_a', 0, 1000, 'linear');
        sign_up_up = false;
    }
    // Move up the sign up button
    translate_up_or_down('#login_a', -200, 1000, 'linear');
    setTimeout(() => {
        $(".log_in_div_two").css("display", "flex");
        $(".button_two").css("display", "block")
        // move sign up a down fast, so it is leveled
        translate_up_or_down('#login_a', 0, 1, 'linear');
        }, 1000);
    log_in_up = true;
}
