function new_div(obj){
            let the = `<div class="single_row_user" id="${obj.username}">
                        <div><a href="#" style="text-decoration-color: black;" onclick="add_gaming_info('${obj.username}')"><p id="row_username">${obj.username}</p></a></div>
                        <div><p id="row_mail">${obj.email}</p></div>
                        <div><input type="text" id="row_name" value="${obj.name}"></div>
                        <div><input type="text" id="row_lastname" value="${obj.lastname}"></div>
                        <div><p id="row_country">${obj.country}</p></div>
                        <div><input type="date" id="row_birth" value="${obj.birth}"></div>
                        <div>
                                    <select name="" id="row_gender">
                                        <option value="${obj.gender}">${obj.gender}</option>
                                        <option value="Female">Female</option>
                                        <option value="Male">Male</option>
                                        <option value="Other">Other</option>
                                    </select>
                        </div>
                        <div>
                                    <select name="" id="row_admin">
                                        <option value="${obj.admin}">${obj.admin}</option>
                                        <option value="True">True</option>
                                        <option value="False">False</option>
                                    </select>
                        </div>
                        <div><p id="row_date_creation">${obj.creation}</p></div>
                        <div><button id="row_save" onclick="save_button('${obj.username}');">save</button></div>
                        <div><button id="row_delete" onclick="delete_button('${obj.username}');">delete</button></div>
                    </div>`;
        $('.div_list_users').append(the);
        console.log("lol");
}
function add_div(){
    var users_data_request  =   {"giveme" : "please"}

    $.ajax({
        type            :   "POST",
        url             :   "/users_data",
        data            :   JSON.stringify(users_data_request),
        contentType     :   "application/json; charset=utf-8",
        success         :   function(data){
            var jso = JSON.stringify(data);
            var obj = JSON.parse(jso)
            console.log(obj);
            // number of elements
            no_objects = Object.keys(obj).length;
            console.log(no_objects);
            for(var i = 0; i < no_objects; i++){
                new_div(obj[`user_${i}`]);
            }
        }
    });
}




window.onload = add_div();



function move_rows(id_val){
    $(`#${id_val}`).remove();
}

function delete_button(id_val){
    anime({
        targets: `#${id_val}`,
        translateX: 1500,
        easing: "easeInOutCubic"
    });
    setTimeout(move_rows, 800, id_val);

    var username        = $(`#${id_val} #row_mail`).text();
    var request_data    = {"username" : username}
    $.ajax({
        type            : "POST",
        url             : "/delete_user",
        data            : JSON.stringify(request_data),
        contentType     : 'application/json; charset=utf-8',
        success         : function(data){
            var jso     = JSON.stringify(data);
            var obj     = JSON.parse(jso);
            console.log(obj);
        }
    });
}





function save_button(id_val){

    var username    = $(`#${id_val} #row_username`).text();
    var name        = $(`#${id_val} #row_name`).val();
    var lastname    = $(`#${id_val} #row_lastname`).val();
    var birth       = $(`#${id_val} #row_birth`).val();
    var gender      = $(`#${id_val} #row_gender`).val();
    var admin       = $(`#${id_val} #row_admin`).val();

    var request_data={"username": username,
                      "name"    : name,
                      "lastname": lastname,
                      "birth"   : birth,
                      "gender"  : gender,
                      "admin"   : admin
    }
    console.log(request_data);

    $.ajax({
        type            : "POST",
        url             : "/safe_admin_changes",
        data            : JSON.stringify(request_data),
        contentType     : 'application/json; chaset=utf-8',
        success         : function(data){
            var jso     = JSON.stringify(data);
            var obj     = JSON.parse(jso);
            alert("saved_data")
        }
    });
}


function add_rows_gaming(obj){
    var level           = obj["level"];
    var score           = obj["score"];
    var time            = obj["timeWhenScore"];
    var kos             = obj["kos"];
    var failedShoots    = obj["failedShoots"];

    var data_div = `<div class="user_game_info_row" id="user_game_info_id">
                        <div><p id="game_row_levelId">${level}</p></div>
                        <div><p id="game_row_score">${score}</p></div>
                        <div><p id="game_row_timeWhenScore">${time}</p></div>
                        <div><p id="game_row_kos">${kos}</p></div>
                        <div><p id="game_row_failedShoots">${failedShoots}</p></div>
                    </div>`;
    $('.user_game_info_square').append(data_div);
}

function appear_gaming_info_div(){
    $(".user_game_info_div").css("display", "flex");
}

function add_gaming_info(username){
    appear_gaming_info_div();

    var request = {"username" : username};
    $.ajax({
        type        : "POST",
        url         : "/get_gaming_info",
        data        : JSON.stringify(request),
        contentType : 'application/json; charset=utf-8',
        success     : function(data){
            var count = Object.keys(data).length;
            for(var i = 0; i < count; i++){
                add_rows_gaming(data[`val_${i}`]);
            }
        }
    });
}


function close_gaming_info(){
    // must delete the current divs
    $(".user_game_info_div").css("display", "none");
    $(".user_game_info_row").remove();
}


// window.onload = add_gaming_info();