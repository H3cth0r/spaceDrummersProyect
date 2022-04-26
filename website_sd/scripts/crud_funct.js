function add_div(){
    var username_list = ["elcarlitos", "elpepino", "elchavo", "elmalo", 
                        "elcalvo", "elcarro", "eldato", "elpelo", "elchato", "elgato"];


    for(let i = 0; i < 10; i++){
            let the = `<div class="single_row_user" id="${username_list[i]}">
                        <div><p id="row_username">${username_list[i]}</p></div>
                        <div><p id="row_mail">elcarlitos@tec.mx</p></div>
                        <div><input type="text" id="row_name"></div>
                        <div><input type="text" id="row_lastname"></div>
                        <div><p id="row_country">Peru</p></div>
                        <div><input type="date" id="row_birth"></div>
                        <div>
                                    <select name="" id="row_gender">
                                        <option value="Female">Female</option>
                                        <option value="Male">Male</option>
                                        <option value="Other">Other</option>
                                    </select>
                        </div>
                        <div>
                                    <select name="" id="row_admin">
                                        <option value="True">Admin</option>
                                        <option value="False">Not Admin</option>
                                    </select>
                        </div>
                        <div><p id="row_date_creation">12/43/2002</p></div>
                        <div><button id="row_save" onclick="save_button('${username_list[i]}');">save</button></div>
                        <div><button id="row_delete" onclick="delete_button('${username_list[i]}');">delete</button></div>
                    </div>`;
        $('.div_list_users').append(the);
        console.log("lol");
    }
}


function new_div(obj){

    for(let i = 0; i < 10; i++){
            let the = `<div class="single_row_user" id="${username_list[i]}">
                        <div><p id="row_username">${username_list[i]}</p></div>
                        <div><p id="row_mail">${obj}</p></div>
                        <div><input type="text" id="row_name" value="${obj}"></div>
                        <div><input type="text" id="row_lastname" value="${obj}"></div>
                        <div><p id="row_country">${obj}</p></div>
                        <div><input type="date" id="row_birth" value="${obj}"></div>
                        <div>
                                    <select name="" id="row_gender">
                                        <option value="${obj}">${obj}</option>
                                        <option value="Female">Female</option>
                                        <option value="Male">Male</option>
                                        <option value="Other">Other</option>
                                    </select>
                        </div>
                        <div>
                                    <select name="" id="row_admin">
                                        <option value="${obj}">${obj}</option>
                                        <option value="True">Admin</option>
                                        <option value="False">Not Admin</option>
                                    </select>
                        </div>
                        <div><p id="row_date_creation">${obj}</p></div>
                        <div><button id="row_save" onclick="save_button('${username_list[i]}');">save</button></div>
                        <div><button id="row_delete" onclick="delete_button('${username_list[i]}');">delete</button></div>
                    </div>`;
        $('.div_list_users').append(the);
        console.log("lol");
    }
}

window.onload = add_div();



function move_rows(id_val){
    $(`#${id_val}`).remove();
}
// div div objs display: none
// animation make smaller row div
// delete the div
function delete_button(id_val){
    anime({
        targets: `#${id_val}`,
        translateX: 1500,
        easing: "easeInOutCubic"
    });
    setTimeout(move_rows, 800, id_val);
}

function save_button(id_val){
    alert("saved " + id_val)
}