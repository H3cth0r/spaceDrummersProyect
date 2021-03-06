from fileinput import filename
import json
import statistics
import string
import base64
from datetime import date, datetime,timedelta

import mimetypes


from unicodedata import name
from unittest import result
from urllib import request, response
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt #para la directiva
import collections
from random import randrange
from json import loads, dumps #para trabajar con json
import sqlite3
#import django.http import hhtp404
from django.contrib.auth.decorators import login_required
from shutil import copyfile


# importing pyjwt lib for generating jwt tokens
import jwt

def index(request):
    return render(request, 'main.html')

"""
Method for checking wether the user has JTW token with the correct data
meaning if the user is logged.
"""
def logged(req):
    if 'login_session' not in req.COOKIES.keys():
        return False
    if req.COOKIES['login_session'] is not None:
        encoded_jwt = req.COOKIES['login_session']
        jwt_key         =   "spaceDrummersIsCool"
        decoded_jwt = jwt.decode(encoded_jwt, jwt_key, algorithms=["HS256"])
        mydb                =   sqlite3.connect("db.sqlite3")
        cur                 =   mydb.cursor()
        stringSQL           =   '''SELECT hashedPwd FROM user WHERE id in (SELECT userId FROM gameprofile WHERE username=?);'''
        row                 =   cur.execute(stringSQL, (decoded_jwt['username'],))
        row                 =   row.fetchone()
        
        if row != None:
            if row[0] == decoded_jwt['password'] and decoded_jwt['logged'] == 'True':
                return True

def decode_jwt(req):
    if 'login_session' not in req.COOKIES.keys():
        return False
    if req.COOKIES['login_session'] is not None:
        encoded_jwt = req.COOKIES['login_session']
        jwt_key         =   "spaceDrummersIsCool"
        decoded_jwt = jwt.decode(encoded_jwt, jwt_key, algorithms=["HS256"])
        return decoded_jwt


@csrf_exempt #directiva
def unityLogin(request):
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = loads(body_unicode)
        username = body['username']
        hashedPwdReq = body['hashedPwd']
        mydb = sqlite3.connect("db.sqlite3")
        cur = mydb.cursor()
        stringSQL = "SELECT id, hashedPwd FROM user WHERE id in (SELECT userId FROM gameprofile WHERE username=?)"
        row = cur.execute(stringSQL, (username,))
        row = row.fetchone()
        
        if row != None:
            userId = row[0]
            hashedPwdDB = row[1]
            accessGranted = 0
            currentLevel=-1
            
            if hashedPwdReq == hashedPwdDB:
                accessGranted = 1
                stringSQL = "SELECT currentLevel FROM gameprofile WHERE username=?"
                row = cur.execute(stringSQL, (username,))
                row = row.fetchone()
                currentLevel = row[0]
            
            d = {
                    "userId":userId,
                    "username":username,
                    "accessGranted":accessGranted,
                    "currentLevel":currentLevel
                    }

        else:
            d = {
                    "userId":None,
                    "username":None,
                    "accessGranted":None,
                    "currentLevel":None
                    }
            return JsonResponse(d, safe=False)

        return JsonResponse(d, safe=False)
    return HttpResponse("Use POST")
  
def main(request):
    return render(request, 'main.html')

@csrf_exempt
def unityLevelstats(request):
    body_unicode = request.body.decode('utf-8')
    body = loads(body_unicode)
    levelId = body['levelId']
    username = body['username']
    score = body['score']
    timeWhenScore = body['timeWhenScore']
    kos = body['kos']
    failedShoots = body['failedShoots']
    mydb = sqlite3.connect("db.sqlite3")
    cur = mydb.cursor()
    stringSQL = '''INSERT INTO "main"."levelstats" ("levelId", "username","score", "timeWhenScore", "kos", "failedShoots") VALUES (?,?,?,?,?,?);'''
    cur.execute(stringSQL, (levelId, username, score, timeWhenScore, kos, failedShoots))
    mydb.commit()

    d = { "informationRecived":1}

    return JsonResponse(d, safe=False)


def login(request):
    is_logged = logged(request)
    if is_logged == True:
        response = redirect('/user_info')
        return response
    return render(request, 'registration/login.html')


@csrf_exempt
def loginRegister(request):
    if request.method == "POST":
        body_unicode        =   request.body.decode('utf-8')
        body                =   loads(body_unicode)
        username            =   body['username']
        password            =   body['password']

        # QUERY
        mydb                =   sqlite3.connect("db.sqlite3")
        cur                 =   mydb.cursor()
        stringSQL           =   '''SELECT hashedPwd FROM user WHERE id in (SELECT userId FROM gameprofile WHERE username=?);'''
        row                 =   cur.execute(stringSQL, (username,))
        row                 =   row.fetchone()

        # if found password, return cookie
        if row != None:
            if row[0]   ==  password:
                confirmation    =   {"correct_credentials" : "Correct credentials"}
                response        =   JsonResponse(confirmation)
                login_session   =   {"username" : username, "password":password, "logged":"True"}
                jwt_key         =   "spaceDrummersIsCool"
                encoded_jwt     =   jwt.encode(login_session, jwt_key, algorithm="HS256")
                response.set_cookie("login_session", encoded_jwt)
            else:
                confirmation    =   {"correct_credentials" : "Incorrect credentials"}
                response        =   JsonResponse(confirmation)
            return response

        # else return incorrect credentials response
        else:
            confirmation    =   {"correct_credentials" : "Incorrect credentials"}
            return JsonResponse(confirmation)

@csrf_exempt
def websiteRegister(request):
    if request.method == "POST":
        body_unicode        =   request.body.decode('utf-8')
        body                =   loads(body_unicode)
        name                =   body['user_name']
        lastname            =   body['user_lastname'] 
        mail                =   body['user_mail']
        username            =   body['user_username']
        password            =   body['user_password']
        birthday            =   body['user_birthday']
        country             =   body['user_country']
        gender              =   body['user_gender']
        mydb                =   sqlite3.connect("db.sqlite3")
        cur                 =   mydb.cursor()
        stringSQL           =   '''SELECT id, email FROM user WHERE id in (SELECT userId FROM gameprofile WHERE username=?);'''
        row                 =   cur.execute(stringSQL, (username,))
        row                 =   row.fetchone()


        # if username does not exist, register on db
        # create registration confirmation obj
        if row == None:
            # First insert user into user table
            stringSQL       =   '''INSERT INTO "main"."user" ("name", "lastName", "age", "email", "hashedPwd", "country", "gender", "admin", "accountCreation") VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);'''
            cur2 =  mydb.cursor()
            today = date.today()
            accountCreation = today.strftime("%Y-%m-%d")
            cur2.execute(stringSQL, (name, lastname, birthday, mail, password, country, gender, "False", accountCreation,))

            # Second insert username into gameprofile
            stringSQL       =   '''INSERT INTO "main"."gameprofile" ("username", "userId", "currentLevel") VALUES (?, last_insert_rowid(), ?);'''
            cur3 = mydb.cursor()
            cur3.execute(stringSQL, (username, 0,))

            mydb.commit()

            # set image
            src = "static/profile_photos/the_data/default.png" 
            dts = "static/profile_photos/" + username + ".png"
            copyfile(src, dts)

            # Create confirmation object
            confirmation = {"registered" : "Registered"}
            return JsonResponse(confirmation, safe = False)
    
            # if user does exist,create invalid registration object
        confirmation    =   {"registered" : "Found already registered username"}
        return JsonResponse(confirmation, safe=False)


def image_to_base64(t_username):
    img_path = "static/profile_photos/"
    the_file = img_path + t_username + ".png"
    with open(the_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
    return encoded_string

@csrf_exempt
def giveMeUserData(request):
    if request.method == "POST":
        body_unicode        =   request.body.decode('utf-8')
        body                =   loads(body_unicode)
        client_response     =   body['give']
        jwt_token           =   decode_jwt(request)
        # QUERY
        mydb                =   sqlite3.connect("db.sqlite3")
        cur                 =   mydb.cursor()
        stringSQL           =   '''SELECT name, lastName, age, email, country, gender, age, accountCreation, admin FROM user WHERE id in (SELECT userId FROM gameprofile WHERE username=?);'''
        row                 =   cur.execute(stringSQL, (jwt_token['username'],))
        row                 =   row.fetchone()
        result              =   {"name"     : row[0],
                                 "lastname" : row[1],
                                 "username" : jwt_token['username'],
                                 "age"      : row[2],
                                 "mail"     : row[3],
                                 "country"  : row[4],
                                 "gender"   : row[5],
                                 "birthday" : row[6],
                                 "creation" : row[7],
                                 "bs4_img"  : image_to_base64(jwt_token['username']),
                                 "admin"    : row[8]
                                }
        return  JsonResponse(result, safe=False)
    
    result              =   {"name"     : "none",
                             "lastName" : "none",
                             "age"      : "0",
                             "mail"     : "none",
                             "country"  : "none",
                             "gender"   : "none",
                             "birthday" : "none",
                             "creation" : "none",
                             "bs4_img"  : "none",
                             "admin"    : "none"
                            }
    return JsonResponse(result, safe=False)



@csrf_exempt
def user_info(request):
    """
    Checking if is user is logged
    """
    is_logged = logged(request)
    if is_logged == False:
        response = redirect('/login')
        return response
    jwt_token           =   decode_jwt(request)
    jueg = jwt_token['username']

    mydb = sqlite3.connect("db.sqlite3")
    cur = mydb.cursor()

    #Scores per game
    stringSQL = 'SELECT currentLevel FROM Gameprofile WHERE username = ?'
    table = cur.execute(stringSQL, (jueg,))
    table = table.fetchall()
    data = []
    i = 0

    while i <= table[0][0]:
        r = str(i)
        stringSQL = 'SELECT Levelstats.timeWhenScore, Levelstats.score  FROM Levelstats WHERE username = ? AND levelId = ? ORDER by score DESC'
        table1 = cur.execute(stringSQL, (jueg, i,))
        table1 = table1.fetchall()
        i = i+1

        if table1 == []:
            pass
        else:
            data.append([('Level '+ r), table1[0][0], table1[0][1]])
    data_Json = dumps(data)

    #Score acumulado 
    stringSQL = 'SELECT count(score) FROM Levelstats WHERE username = ? '
    table = cur.execute(stringSQL, (jueg,))
    table = table.fetchall()
    i = 0
    t=0

    while i < int(table[0][0]):
        stringSQL = 'SELECT score FROM Levelstats WHERE username = ? '
        table1 = cur.execute(stringSQL, (jueg,))
        table1 = table1.fetchall()
        t += int(table1[i][0])
        i += 1

    t_data = dumps(t)
    
    #Minutos jugados
    stringSQL = 'SELECT Levelstats.timeWhenScore FROM  Levelstats WHERE username=? '
    tableMJ = cur.execute(stringSQL, (jueg,))
    tableMJ = tableMJ.fetchall()
    stringSQL = 'SELECT count(Levelstats.timeWhenScore) FROM  Levelstats WHERE username=? '
    tableMJ1 = cur.execute(stringSQL, (jueg,))
    tableMJ1 = tableMJ1.fetchone()
    par = tableMJ1[0]
    tim = 0

    for i in range(par):
        tim += float(tableMJ[i][0])

    #Tiempo promedio por sesion

    stringSQL = 'SELECT Gameprofile.userId FROM  Gameprofile WHERE username=? '
    tableTP = cur.execute(stringSQL, (jueg,))
    tableTP = tableTP.fetchone()
    idUsr = tableTP[0]
    stringSQL = 'SELECT count(Gamesesion.startTime) FROM  Gamesesion WHERE userId=? '
    tableTP = cur.execute(stringSQL, (idUsr,))
    tableTP = tableTP.fetchone()
    canFech= tableTP[0]
    stringSQL = 'SELECT Gamesesion.startTime, Gamesesion.endTime FROM  Gamesesion WHERE userId=? '
    tableTP = cur.execute(stringSQL, (idUsr,))
    tableTP = tableTP.fetchall()
    per= []
    perMin=[]
    for i in range(canFech):
        time_01 = datetime.strptime(tableTP[i][0][11:19],"%H:%M:%S")
        time_02 = datetime.strptime(tableTP[i][1][11:19],"%H:%M:%S")
        time_interval = time_02 - time_01
        per.append(str(time_interval))
    
    for i in range(canFech):
        m=int(per[i][0])*60 + int(per[i][2:4])
        perMin.append(m)

    tiemAcum=0
    for i in range(canFech):
        tiemAcum+=perMin[i]
    

    if canFech != 0:
        promT=tiemAcum/canFech
    else:
        promT=0

    

    return render(request, 'user_info.html', {'values':t_data,'valT':tim,'valP':promT, 'valueSc':data_Json})

@csrf_exempt
def updateUserDataNow(request):
    if request.method == "POST":
        body_unicode        =   request.body.decode('utf-8')
        body                =   loads(body_unicode)
        name                =   body['user_name']
        lastname            =   body['user_lastname'] 
        if 'password' in body:
            password        =   body['user_password']
        else:
            password        =   False
        birthday            =   body['user_birthday']
        country             =   body['user_country']
        gender              =   body['user_gender']
        mydb                =   sqlite3.connect("db.sqlite3")
        tkn                 =   decode_jwt(request)

        cur2 =  mydb.cursor()
        # First insert user into user table
        if password != False:
            stringSQL       =   '''UPDATE user 
                                   SET name = ?, lastName = ?, age = ?, hashedPwd = ?, country = ?, gender = ? 
                                   FROM gameprofile WHERE gameprofile.userId == user.id 
                                   AND gameprofile.username == ?;'''
            cur2.execute(stringSQL, (name, lastname, birthday, password, country, gender, tkn['username'],))
        else:
            stringSQL       =   '''UPDATE user 
                                   SET name = ?, lastName = ?, age = ?, country = ?, gender = ?
                                   FROM gameprofile WHERE gameprofile.userId == user.id
                                   AND gameprofile.username == ?;'''
            cur2.execute(stringSQL, (name, lastname, birthday, country, gender, tkn['username'],))


        mydb.commit()

        # Create confirmation object
        confirmation = {"registered" : "Registered"}
        return JsonResponse(confirmation, safe = False)
    
@csrf_exempt
def takeThisPhoto(request):
    if request.method == 'POST':
        body_unicode        =   request.body.decode('utf-8')
        body                =   loads(body_unicode)
        #   get username from cookie
        jwt_tkn             =   decode_jwt(request)
        username            =   jwt_tkn['username']
        #   get base64 img
        img_base64          =   body['img_base']
        img_data            =   img_base64.split(',')
        img_data            =   img_data[1]
        #   decode img_data
        img_64_decode       =   base64.b64decode(img_data)
        username_file_name  =   username + '.png'
        img_path            =   "static/profile_photos/"
        img_result          =   open(img_path + username_file_name, 'wb')
        img_result.write(img_64_decode)
        #   img changed confirmation
        confirmation        =   {"image_change":"True"}
        return  JsonResponse(confirmation, safe=False)

def is_admin(req):
    d_jwt = decode_jwt(req)
    username                =  d_jwt['username']

    stringSQL               =   '''SELECT admin FROM user WHERE id in (SELECT userId FROM gameprofile WHERE username=?);'''
    mydb                    =   sqlite3.connect("db.sqlite3")
    cur                     =   mydb.cursor()
    table                   =   cur.execute(stringSQL, (username,),).fetchone()
    return  table[0]
    
  

def admin_panel(request):
    # add is logged
    is_logged = logged(request)
    if is_logged == False:
        response = redirect('/login')
        return response
    
    is_adm = is_admin(request)
    if is_adm == 'False':
        response = redirect('/user_info')
        return response

    return render(request, "crud.html")

@csrf_exempt
def to_admin_panel(request):
    if request.method == 'POST':
       return redirect('/admin_panel')

@csrf_exempt
def users_data(request):
    # add is logged

    if request.method == 'POST':
        body_unicode        =   request.body.decode('utf-8')
        body                =   loads(body_unicode)

        # Get data
        mydb                =   sqlite3.connect("db.sqlite3")
        cur                 =   mydb.cursor()
        stringSQL           =   '''SELECT * FROM Gameprofile INNER JOIN user ON user.id=Gameprofile.userId'''
        table               =   cur.execute(stringSQL,)
        table               =   table.fetchall()
        
        confirmation        =   {"done" : "yes"}

        the_users           =   {}
        counter             =   0
        for i in table:
            the_users[f"user_{counter}"]   =   {"username" :   i[0],
                                             "id"       :   i[1],
                                             "name"     :   i[4],
                                             "lastname" :   i[5],
                                             "birth"    :   i[6],
                                             "email"    :   i[7],
                                             "country"  :   i[9],
                                             "gender"   :   i[10],
                                             "admin"    :   i[11],
                                             "creation" :   i[12]

            }
            counter += 1
        return JsonResponse(the_users, safe=False)


@csrf_exempt
def save_admin_changes(request):
    if request.method == 'POST':
        body_unicode        =   request.body.decode('utf-8')
        body                =   loads(body_unicode)

        mydb                =   sqlite3.connect("db.sqlite3")
        stringSQL           =   '''UPDATE user 
                                SET name = ?, lastName = ?, age = ?, gender = ?, admin = ?
                                FROM gameprofile WHERE gameprofile.userId == user.id
                                AND gameprofile.username == ?;'''
        cur                 =   mydb.cursor()

        cur.execute(stringSQL, (body['name'], body['lastname'], body['birth'], body['gender'], body['admin'],body['username'],))

        mydb.commit()
        confirmation        =   {"confirmation" : "True"}
        return JsonResponse(confirmation, safe=False)

        
@csrf_exempt
def delete_user(request):
    if request.method == 'POST':
        body_unicode        =   request.body.decode('utf-8')
        body                =   loads(body_unicode)
        
        mydb                =   sqlite3.connect("db.sqlite3")
        stringSQL           =   '''DELETE FROM user WHERE email = ?'''
        cur                 =   mydb.cursor()

        cur.execute(stringSQL, (body['username'],),)

        mydb.commit()

        confirmation        =   {"confirmation" : "True"}
        return  JsonResponse(confirmation, safe=False)


@csrf_exempt
def get_gaming_info(request):
    if request.method == 'POST':
        body_unicode        =   request.body.decode('utf-8')
        body                =   loads(body_unicode)
        username            =   body['username']

        mydb                =   sqlite3.connect("db.sqlite3")
        stringSQL           =   '''SELECT levelId, username,score, timeWhenScore, kos, failedShoots FROM Levelstats WHERE username = ?;'''
        cur                 =   mydb.cursor()
        table               =   cur.execute(stringSQL, (username,),).fetchall()
        mydb.commit()
        user_info = {}
        counter = 0
        for i in table:
            user_info[f"val_{counter}"] = {"level"          : i[0],
                                           "username"       : i[1],
                                           "score"          : i[2],
                                           "timeWhenScore"  : i[3],
                                           "kos"            : i[4],
                                           "failedShoots"   : i[5]
            }
            counter += 1
        return JsonResponse(user_info, safe=False)


def download_game(request):
    filename        =   'unityBuild.zip'
    filepath        =   'static/videogame_file/'+filename
    path            =   open(filepath, 'rb')
    mime_type, _    =   mimetypes.guess_type(filepath)
    response = HttpResponse(path, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response


    
@csrf_exempt
def unityGamesession(request):
    body_unicode = request.body.decode('utf-8')
    body = loads(body_unicode)
    startTime = body['startTime']
    endTime = body['endTime']
    userId = body['userId']
    mydb = sqlite3.connect("db.sqlite3")
    cur = mydb.cursor()
    stringSQL = '''INSERT INTO "main"."gamesesion" ( "startTime", "endTime","userId") VALUES (?,?,?);'''
    cur.execute(stringSQL, (startTime,endTime,userId,))
    mydb.commit()

    d = {"informationRecived":1}

    return JsonResponse(d, safe=False)
    
@csrf_exempt
def unityCurrentlevel(request):
    body_unicode = request.body.decode('utf-8')
    body = loads(body_unicode)
    currentLevel = body['currentLevel']
    username = body['username']
    mydb = sqlite3.connect('db.sqlite3')
    cur = mydb.cursor()
    stringSQL = "UPDATE Gameprofile SET currentLevel = ? WHERE username = ?"
    cur.execute(stringSQL, (currentLevel, username))
    mydb.commit()

    d = { "informationRecived":1 }

    return JsonResponse(d, safe=False)    

def stats(request):
    mydb = sqlite3.connect("db.sqlite3")
    cur = mydb.cursor()


    stringSQL = '''SELECT Gameprofile.username, User.country, Levelstats.score FROM (User JOIN Gameprofile ON User.id = Gameprofile.userId) JOIN Levelstats ON Gameprofile.username = Levelstats.username ORDER by score DESC LIMIT 3'''
    table = cur.execute(stringSQL)
    table = table.fetchall()
    
    name_var = 'username'
    point_var = 'Points'
    role = {"role": 'style'}
    data = [[name_var,point_var, role]]


    country_var = 'Country'
    people_var = 'People'
    dataC = [[country_var, people_var]]


    level_var = 'LEVEL'
    username_var = 'USERNAME'
    score_var = 'SCORE'


    data.append([table[1][0]+" / "+table[1][1], table[1][2], '#1A7A3C'])
    data.append([table[0][0]+" / "+table[0][1], table[0][2], '#274A9F'])
    data.append([table[2][0]+" / "+table[2][1], table[2][2], '#D3450D'])

    name_var_json = dumps(name_var)
    point_var_json = dumps(point_var)
    modified_data = dumps(data)

    paises = [['Afganistan'],['Albania'],['Algeria'],['American Samoa'],['Andorra'],['Angola'],['Anguilla'],['Antigua & Barbuda'],['Argentina'],['Armenia'],['Aruba'],['Australia'],['Austria'],['Azerbaijan'],['Bahamas'],['Bahrain'],['Bangladesh'],['Barbados'],['Belarus'],['Belgium'],
          ['Belize'],['Benin'],['Bermuda'],['Bhutan'],['Bolivia'],['Bonaire'],['Bosnia & Herzegovina'],['Botswana'],['Brazil'],['British Indian Ocean Ter'],['Brunei'],['Bulgaria'],['Burkina Faso'],['Burundi'],['Cambodia'],['Cameroon'],['Canada'],['Canary Islands'],['Cape Verde'],['Cayman Islands'],
          ['Central African Republic'],['Chad'],['Channel Islands'],['Chile'],['China'],['Christmas Island'],['Cocos Island'],['Colombia'],['Comoros'],['Congo'],['Cook Islands'],['Costa Rica'],['Cote DIvoire'],['Croatia'],['Cuba'],['Curaco'],['Cyprus'],['Czech Republic'],['Denmark'],['Djibouti'],
          ['Dominica'],['Dominican Republic'],['East Timor'],['Ecuador'],['Egypt'],['El Salvador'],['Equatorial Guinea'],['Eritrea'],['Estonia'],['Ethiopia'],['Falkland Islands'],['Faroe Islands'],['Fiji'],['Finland'],['France'],['French Guiana'],['French Polynesia'],['French Southern Ter'],['Gabon'],['Gambia'],
          ['Georgia'],['Germany'],['Ghana'],['Gibraltar'],['Great Britain'],['Greece'],['Greenland'],['Grenada'],['Guadeloupe'],['Guam'],['Guatemala'],['Guinea'],['Guyana'],['Haiti'],['Hawaii'],['Honduras'],['Hong Kong'],['Hungary'],['Iceland'],['Indonesia'],
          ['India'],['Iran'],['Iraq'],['Ireland'],['Isle of Man'],['Israel'],['Italy'],['Jamaica'],['Japan'],['Jordan'],['Kazakhstan'],['Kenya'],['Kiribati'],['North Korea'],['South Korea'],['Kuwait'],['Kyrgyzstan'],['Laos'],['Latvia'],['Lebanon'],
          ['Lesotho'],['Liberia'],['Libya'],['Liechtenstein'],['Lithuania'],['Luxembourg'],['Macau'],['Macedonia'],['Madagascar'],['Malaysia'],['Malawi'],['Maldives'],['Mali'],['Malta'],['Marshall Islands'],['Martinique'],['Mauritania'],['Mauritius'],['Mayotte'],['Mexico'],
          ['Midway Islands'],['Moldova'],['Monaco'],['Mongolia'],['Montserrat'],['Morocco'],['Mozambique'],['Myanmar'],['Nambia'],['Nauru'],['Nepal'],['Netherland Antilles'],['Netherlands'],['Nevis'],['New Caledonia'],['New Zealand'],['Nicaragua'],['Niger'],['Nigeria'],['Niue'],
          ['Norfolk Island'],['Norway'],['Oman'],['Pakistan'],['Palau Island'],['Palestine'],['Panama'],['Papua New Guinea'],['Paraguay'],['Peru'],['Phillipines'],['Pitcairn Island'],['Poland'],['Portugal'],['Puerto Rico'],['Qatar'],['Republic of Montenegro'],['Republic of Serbia'],['Reunion'],['Romania'],
          ['Russia'],['Rwanda'],['St Barthelemy'],['St Eustatius'],['St Helena'],['St Kitts-Nevis'],['St Lucia'],['St Maarten'],['St Pierre & Miquelon'],['St Vincent & Grenadines'],['Saipan'],['Samoa'],['Samoa American'],['San Marino'],['Sao Tome & Principe'],['Saudi Arabia'],['Senegal'],['Seychelles'],['Sierra Leone'],['Singapore'],
          ['Slovakia'],['Slovenia'],['Solomon Islands'],['Somalia'],['South Africa'],['Spain'],['Sri Lanka'],['Sudan'],['Suriname'],['Swaziland'],['Sweden'],['Switzerland'],['Syria'],['Tahiti'],['Taiwan'],['Tajikistan'],['Tanzania'],['Thailand'],['Togo'],['Tokelau'],
          ['Tonga'],['Trinidad & Tobago'],['Tunisia'],['Turkey'],['Turkmenistan'],['Turks & Caicos Is'],['Tuvalu'],['Uganda'],['United Kingdom'],['Ukraine'],['United Arab Erimates'],['United States of America'],['Uraguay'],['Uzbekistan'],['Vanuatu'],['Vatican City State'],['Venezuela'],['Vietnam'],['Virgin Islands (Brit)'],['Virgin Islands (USA)'],
          ['Wake Island'],['Wallis & Futana Is'],['Yemen'],['Zaire'],['Zambia'],['Zimbabwe']]

    for i in paises:
        stringSQL = 'SELECT count(name) from User WHERE country = "'+i[0]+'";'
        table = cur.execute(stringSQL)
        table = table.fetchall()
        if (table[0][0] != 0):
            dataC.append([i[0], table[0][0]])
        else:
            continue

    country_var_json = dumps(country_var)
    people_var_json = dumps(people_var)
    modified_dataC = dumps(dataC)

    i = 0

    dataB = []

    while (i <= 8):
        
        r = str(i)
        stringSQL = 'SELECT Levelstats.levelId, Levelstats.username, Levelstats.score  FROM Levelstats WHERE levelId = '+r+' ORDER by score DESC LIMIT 1'
        table = cur.execute(stringSQL)
        table = table.fetchall()
        dataB.append([('Level '+ str(i+1)), table[0][1], table[0][2]])

        i = i + 1

    modified_dataB = dumps(dataB)


    level_var_json = dumps(level_var)
    username_var_json = dumps(level_var)
    score_var_json = dumps(score_var)
    
     # Histograma de las edades de los jugadores
    stringSQL = 'SELECT count(age) FROM User'
    tablaEda = cur.execute(stringSQL)
    tablaEda = tablaEda.fetchone()
    numEda = tablaEda[0]
    stringSQL = 'SELECT age FROM User'
    tablaEda = cur.execute(stringSQL)
    tablaEda = tablaEda.fetchall()
    cantNum = []

    """
    Date right now  
    """
    now =  datetime.now()
    for i in range(numEda):
        birth = datetime.strptime(tablaEda[i][0], '%Y-%m-%d')
        # birth = tablaEda[i][0]
        cantNum.append(int((now - birth).days / 365.25))
    # cantNum = list(set(cantNum))
    no_repited_values_list = list(set(cantNum))
    dataUni = [['Edad', 'Cantidad']]
    for i in no_repited_values_list:
        dataUni.append([i, cantNum.count(i)])
    
    modificada = dumps(dataUni)
    
    edadM = max(no_repited_values_list)


    return render  (request,'stats.html',{'values':modified_data,'username': name_var_json,'points':point_var_json, 'Rols': role, 'valuesC':modified_dataC,'Country':country_var_json,'People':people_var_json,'Edad':modificada, 'MaxEd':edadM, 'valuesB':modified_dataB,'level':level_var_json,'username':username_var_json,'score':score_var_json})
    #,{'valuesC':modified_dataC,'Country':country_var_json,'People':people_var_json}

   

@csrf_exempt
def topScore(request):
    body_unicode = request.body.decode('utf-8')
    body = loads(body_unicode)
    username = body['username']
    mydb = sqlite3.connect("db.sqlite3")
    cur = mydb.cursor()
    stringSQL = '''SELECT score , timeWhenScore FROM Levelstats WHERE username = ?'''
    row = cur.execute(stringSQL, (username,))
    row = row.fetchone()
    stringSQL2 = '''SELECT username, score , timeWhenScore FROM Levelstats ORDER by score DESC LIMIT 3'''
    row2 = cur.execute(stringSQL2)
    row2 = row2.fetchall()
    d={ "userTopScore":{
            "score":row[0],
            "timeWhenScore":row[1]
        },
        "topTree":{
            "t1":{
            "username":row2[0][0] ,
            "score":row2[0][1],
            "timeWhenScore": row2[0][2]
            },
            "t2":{
            "username":row2[1][0] ,
            "score":row2[1][1],
            "timeWhenScore": row2[1][2]
            },
            "t3":{
            "username":row2[2][0] ,
            "score":row2[2][1],
            "timeWhenScore": row2[2][2]
            }

        }

    }

    return JsonResponse(d, safe=False)


@login_required   
def priv(request):
    usuario = request.user

    return HttpResponse('Hola')

