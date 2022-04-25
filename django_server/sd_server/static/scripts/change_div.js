function change_to_account_div(){
    $('#account_button').css('color', '#444444');
    $('#stats_button').css('color', 'white');
    $('.my_stats_div').css('display', 'none');
    $('.account_information_div').css('display', 'block');
    return false;
}


function run_counting_up(){
    
    $('.number_one_s').countTo({from: 0, to: 25});
    $('.number_two_s').countTo({from: 0, to: 3452});
    $('.number_three_s').countTo({from: 0, to: 23});
    $('.number_four_s').countTo({from: 0, to: 728});
    $('.number_five_s').countTo({from: 0, to: 1254});
}


function change_to_stats_div(){
    $('#stats_button').css('color', '#444444');
    $('#account_button').css('color', 'white');
    $('.account_information_div').css('display', 'none');
    $('.my_stats_div').css('display', 'block');
    setTimeout(() => {
        run_counting_up();
        }, 1000);
    return false;
}



