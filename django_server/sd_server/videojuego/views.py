from urllib import response
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt #para la directiva
import collections
from random import randrange
from json import loads, dumps #para trabajar con json
import sqlite3
#import django.http import hhtp404
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'main.html')


@csrf_exempt #directiva
def unityLogin(request):
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = loads(body_unicode)
        print(body_unicode)
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
            raise Http404("username does not exist")

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
    return render(request, 'registration/login.html')

@login_required
def user_info(request):
    return render(request, 'user_info.html')

# def loginA(request):

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

    d = {"Perfecto":"Datos subidos"}

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
    country_var = 'Country'
    people_var = 'People'
    level_var = 'LEVEL'
    username_var = 'USERNAME'
    score_var = 'SCORE'

    data = [[name_var,point_var, role]]
    dataC = [[country_var, people_var]]
    dataB = []

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

    while (i <= 8):
        i = i + 1
        r = str(i)
        stringSQL = 'SELECT Levelstats.levelId, Levelstats.username, Levelstats.score  FROM Levelstats WHERE levelId = '+r+' ORDER by score DESC LIMIT 1'
        table = cur.execute(stringSQL)
        table = table.fetchall()
        dataB.append([('Level '+ r), table[0][1], table[0][2]])

    level_var_json = dumps(level_var)
    username_var_json = dumps(level_var)
    score_var_json = dumps(score_var)
    modified_dataB = dumps(dataB)

     # Histograma de las edades de los jugadores
    stringSQL = 'SELECT count(age) FROM User'
    tablaEda = cur.execute(stringSQL)
    tablaEda = tablaEda.fetchone()
    numEda = tablaEda[0]
    stringSQL = 'SELECT age FROM User'
    tablaEda = cur.execute(stringSQL)
    tablaEda = tablaEda.fetchall()
    stringSQL = 'SELECT max(age) FROM User'
    unDig = cur.execute(stringSQL)
    unDig = unDig.fetchone()
    edadM = unDig[0]
    cantNum = []
    numRep = []
    for i in range(numEda):
        cantNum.append(tablaEda[i][0])
    cantNum = list(set(cantNum))

    for i in range(len(cantNum)):
        num=0
        for j in range(numEda):
            if cantNum[i]==tablaEda[j][0]:
                num+=1
        numRep.append(num)
    dataUni=[['Edad','Cantidad']]
    for i in range(len(cantNum)):
        dataUni.append([cantNum[i] ,numRep[i]])
    
    modificada = dumps(dataUni)

    print(edadM)

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
    print(usuario)

    return HttpResponse('Hola')

    '''
    mydb = sqlite3.connect('db.sqlite3')
    cur = mydb.cursor()
    stringSQL = 'SELECT username, userId, currentLevel FROM Gameprofile WHERE django_user=?'
    rows = cur.execute(stringSQL,(str(usuario),))
    rr = rows.fetchone()
    rows = cur.execute(stringSQL,(str(usuario),))
    if rr == None:
        raise Http404('user_id does not exist')
    else:
        lista_salida = []
        for r in rows:
            print(r)
            d = {}
            d['id'] = r[0]
            d['username'] = r[1]
            d["score"] = r[3]
            lista_salida.append(d)
        j = dumps(lista_salida)
    return HttpResponse(j, content_type="text/json-comment-filtered")'''