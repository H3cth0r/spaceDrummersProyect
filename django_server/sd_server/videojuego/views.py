from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt #para la directiva
import collections
from random import randrange
from json import loads, dumps #para trabajar con json
import sqlite3

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

    d = {"Perfecto":"Datos subidos"}

    return JsonResponse(d, safe=False)


def log_reg(request):
    return render(request, 'log_reg.html')

def user_info(request):
    return render(request, 'user_info.html')


    

def stats(request):
    mydb = sqlite3.connect("db.sqlite3")
    cur = mydb.cursor()
    stringSQL = '''SELECT Gameprofile.username, User.country, Levelstats.score FROM (User JOIN Gameprofile ON User.id = Gameprofile.userId) JOIN Levelstats ON Gameprofile.username = Levelstats.username WHERE levelId = 1 ORDER by score DESC LIMIT 3'''
    table = cur.execute(stringSQL)
    table = table.fetchall()
    
    name_var = 'username'
    point_var = 'Points'
    role = {"role": 'style'}
    country_var = 'Country'
    people_var = 'People'

    data = [[name_var,point_var, role]]
    dataC = [[country_var, people_var]]

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

    for i in paises-1:
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

    return render  (request,'stats.html',{'values':modified_data,'username': name_var_json,'points':point_var_json, 'Rols': role, 'valuesC':modified_dataC,'Country':country_var_json,'People':people_var_json})
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
    
