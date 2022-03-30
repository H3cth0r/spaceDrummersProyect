from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from json import loads, dumps
import collections
import sqlite3 
from django.http import Http404
# Create your views here.

def index(request):
    return HttpResponse('<h1> Hola desde Django</h1>')

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