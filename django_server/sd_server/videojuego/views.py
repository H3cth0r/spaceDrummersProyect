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
def levelstats(request):
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
    name_var = 'username'
    point_var = 'Points'
    role = {"role": 'style'}

    data = [[name_var,point_var, role]]


    data.append(['Pepo117/Italy', randrange(100000), '#274A9F'])
    data.append(['Alpha/Mexico', randrange(100000), '#1A7A3C'])
    data.append(['ToxicV69/Japan', randrange(100000), '#D3450D'])

    name_var_json = dumps(name_var)
    point_var_json = dumps(point_var)
    modified_data = dumps(data)

    return render  (request,'grafica.html',{'values':modified_data,'username': name_var_json,'points':point_var_json, 'Rols': role})

