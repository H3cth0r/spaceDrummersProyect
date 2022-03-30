from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from json import loads, dumps #para trabajar con json
from django.views.decorators.csrf import csrf_exempt #para la directiva
import sqlite3

# Create your views here.

def index(request):
    return HttpResponse('<h1> Hola desde Django</h1>')

@csrf_exempt #directiva
def unityLogin(request):
    body_unicode = request.body.decode('utf-8')
    body = loads(body_unicode)
    username = body['username']
    hashedPwdReq = body['hashedPwd']
    mydb = sqlite3.connect("db.sqlite3")
    cur = mydb.cursor()
    stringSQL = '''SELECT id, hashedPwd FROM user WHERE id in (SELECT userId FROM gameprofile WHERE username=?)'''
    row = cur.execute(stringSQL, (username,))
    row = row.fetchone()
    
    if row != None:
        userId = row[0]
        hashedPwdDB = row[1]
        accessGranted = 0
        currentLevel=-1
        
        if hashedPwdReq == hashedPwdDB:
            accessGranted = 1
            stringSQL = '''SELECT currentLevel FROM gameprofile WHERE username=?'''
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