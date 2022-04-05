from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from json import loads, dumps
import collections
import sqlite3 
from django.http import Http404
from random import randrange
# Create your views here.

def index(request):
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

def grafica(request):
    mydb = sqlite3.connect("db.sqlite3")
    cur = mydb.cursor()
    stringSQL = '''SELECT Gameprofile.username, User.country, Levelstats.score FROM (User JOIN Gameprofile ON User.id = Gameprofile.userId) JOIN Levelstats ON Gameprofile.username = Levelstats.username ORDER by score DESC'''
    table = cur.execute(stringSQL)
    table = table.fetchall()
    
    name_var = 'username'
    point_var = 'Points'
    role = {"role": 'style'}

    data = [[name_var,point_var, role]]


    
    data.append([table[1][0]+" / "+table[1][1], table[1][2], '#1A7A3C'])
    data.append([table[0][0]+" / "+table[0][1], table[0][2], '#274A9F'])
    data.append([table[2][0]+" / "+table[2][1], table[2][2], '#D3450D'])

    name_var_json = dumps(name_var)
    point_var_json = dumps(point_var)
    modified_data = dumps(data)

    return render  (request,'grafica.html',{'values':modified_data,'username': name_var_json,'points':point_var_json, 'Rols': role})

