


function translate_left_or_right(html_object, to_translate, the_duration = 1000, the_easing='linear'){
    anime({targets: html_object, translateX: to_translate, duration: the_duration, easing: the_easing});
}
function nav_bar_slide_left(){
    $('.clicked_sandwich_menu').css({'display': 'flex', 'background-color':'transparent'});
    $('.clicked_sandwich_menu nav ul li a').css({'color':'transparent'});
    translate_left_or_right('.clicked_sandwich_menu', 1230, 500, 'linear');
    
    setTimeout(() => {
        $('.clicked_sandwich_menu').css({'background-color':'#D3450D'});
        $('.clicked_sandwich_menu nav ul li a').css({'color':'white'});
        translate_left_or_right('.clicked_sandwich_menu', 0, 1500, 'linear');
        }, 500);
    
    $('.close_clicked_sandwich_menu').css('display', 'block');
}

function nav_bar_slide_right(){
    translate_left_or_right('.clicked_sandwich_menu', 1230, 1500, 'linear');
    setTimeout(() => {
        $('.clicked_sandwich_menu').css({'display':'none'}); 
        $('.close_clicked_sandwich_menu').css('display', 'none');
        }, 1500);
}