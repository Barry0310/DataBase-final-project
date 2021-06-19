from django.shortcuts import render
import json
from django.http import JsonResponse
from django.db import connection

def LoginCheck(request):
    cursor = connection.cursor()
    ID = '\'{ID}\''.format(ID=request['userID'])
    cursor.execute('select password from user where ID={ID}'.format(ID=ID))
    appl = cursor.fetchall()
    useID = request['userID']
    stats = 'SUCCESS'
    if len(appl)==0:
        useID = 'ID_NOT_FOUND'
        stats = 'FAIL'
    elif appl[0][0]!=request['password']:
        useID = 'ERROR_PASSWORD'
        stats = 'FAIL'
    send_json = {
        'userID': useID,
        'stats': stats,
    }
    return send_json

def login(request):
    if request.method == 'POST':
        mes_json = json.loads(request.body.decode('utf-8'))
        if (mes_json['action'] == 'LOGIN'):
            send_js = LoginCheck(mes_json)
            return JsonResponse(send_js)
    return render(request, 'login.html')
# Create your views here.
