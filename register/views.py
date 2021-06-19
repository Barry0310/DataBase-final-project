from django.shortcuts import render
import json
from django.http import JsonResponse
from django.db import connection
def UserRegister(request):
    cursor = connection.cursor()
    ID = '\'{ID}\''.format(ID=request['userID'])
    cursor.execute('select password from user where ID={ID}'.format(ID=ID))
    appl = cursor.fetchall()
    stats = 'SUCCESS'
    if(len(appl)!=0):
        stats = 'FAIL'
    else:
        password = '\'{password}\''.format(password=request['password'])
        name = '\'{name}\''.format(name=request['name'])
        gender = '\'{gender}\''.format(gender=request['gender'])
        education = '\'{education}\''.format(education=request['education'])
        cursor.execute(
            'insert into user values({ID}, {password}, {name}, {gender}, {education}, {create_time}, 0)'.format(
                ID=ID,
                password=password,
                name=name,
                gender=gender,
                education=education,
                create_time='now()',
            ))
    send_json = {
        'stats' : stats,
    }
    return send_json


def register(request):
    if request.method == 'POST':
        mes_json = json.loads(request.body.decode('utf-8'))
        if (mes_json['action'] == 'REGISTER'):
            send_js=UserRegister(mes_json)
        return JsonResponse(send_js)
    return render(request, 'register.html')
# Create your views here.
