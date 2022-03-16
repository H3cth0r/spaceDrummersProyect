// anime({
//     targets: '#to_animate_button_one',
//     translateY: -300,
//     duration:   1000,
//     easing: 'linear',
// });


let sign_up_up = false;
let log_in_up  = false;



function on_click_sign_up(){
    if(log_in_up == true) log_in_down();
    anime({
        targets: '#sign_up_a',
        translateY: -200,
        duration: 1000,
        easing: 'linear'
    });
    setTimeout(() => {
        $(".sign_up_div_two").css("display", "flex");
        $(".button_one").css("display", "block")
        sign_up_down(1);
        }, 1000);
    
    sign_up_up = true;
}
function sign_up_down(the_delay=1000){
    anime({
        targets: '#sign_up_a',
        translateY: 0,
        duration: the_delay,
        easing: 'linear'
    });   
}




function on_click_log_in(){
    if(sign_up_up==true) sign_up_down();
    anime({
        targets: '#login_a',
        translateY: -200,
        duration: 1000,
        easing: 'linear'
    });
    log_in_up = true;
}

function log_in_down(){
    anime({
        targets: '#login_a',
        translateY: 0,
        duration: 1000,
        easing: 'linear'
    });
}