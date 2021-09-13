from django.shortcuts import render
import json
from django.http import JsonResponse
from django.db import connection

def ClassData(request, name):
    cursor = connection.cursor()
    class_name = '\'{name}\''.format(name=name)
    cursor.execute('select * from classification where name={name}'.format(name=class_name))
    appl = cursor.fetchall()
    send_json = {
        'name': name,
        'disscusion': appl[0][1],
        'num_comment': appl[0][2],
        'last_article_time': appl[0][3],
        'article': [
        ],
    }
    cursor.execute('select * from article where class={name}'.format(name=class_name))
    appl = cursor.fetchall()
    for i in appl:
        send_json['article'].append({'serial_num' : i[0], 'title' : i[3]})
    return send_json


def classification(request, name):
    if request.method == 'POST':
        mes_json = json.loads(request.body.decode('utf-8'))
        if (mes_json['action'] == 'GET_CLASS_DATA'):
            send_js=ClassData(mes_json, name)
        return JsonResponse(send_js)
    return render(request, 'article_list.html')


def ClassList(request):
    if request.method == 'POST':
        mes_json = json.loads(request.body.decode('utf-8'))
        if (mes_json['action'] == 'GET_CLASS_LIST'):
            cursor = connection.cursor()
            send_json = {
                 'name': [
                 ]
            }
            cursor.execute('select name from classification')
            appl = cursor.fetchall()
            for i in appl:
                send_json['name'].append(i[0])
            return JsonResponse(send_json)
    return render(request, 'class_list.html')
# Create your views here.
