from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import sqlite3
from json import dumps, loads
import collections
# Create your views here.

def index(request):
    return HttpResponse('<h1> Hola desde Django</h1>')

@csrf_exempt
def gamesesion(request):
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
