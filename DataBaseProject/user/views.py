from django.shortcuts import render
import json
from django.http import JsonResponse
from django.db import connection

def UserData(request):
    cursor = connection.cursor()
    ID = '\'{ID}\''.format(ID=request['userID'])
    cursor.execute('select * from user where ID={ID}'.format(ID=ID))
    appl = cursor.fetchall()
    send_json = {
        'userID': appl[0][0],
        'name': appl[0][2],
        'gender': appl[0][3],
        'education': appl[0][4],
        'create_time': appl[0][5],
        'num_post': appl[0][6],
    }
    return send_json

def user(request):
    if request.method == 'POST':
        mes_json = json.loads(request.body.decode('utf-8'))
        if (mes_json['action'] == 'GET_USER_DATA'):
            send_js = UserData(mes_json)
            return JsonResponse(send_js)
    return render(request, 'personal.html')
# Create your views here.
