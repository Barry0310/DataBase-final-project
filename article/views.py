from django.shortcuts import render
import json
from django.http import JsonResponse
from django.db import connection

def ArticleData(request, num):
    cursor = connection.cursor()
    cursor.execute(
        'select * from article where serial_num={serial_num}'.format(serial_num=num))
    appl = cursor.fetchall()
    send_json = {
        'serial_num': appl[0][0],
        'class_name': appl[0][2],
        'userID': appl[0][1],
        'title': appl[0][3],
        'content': appl[0][4],
        'post_time': appl[0][5],
        'comment': [
        ],
    }
    cursor.execute('select * from comment where article_num={serial_num}'.format(serial_num=num))
    appl = cursor.fetchall()
    for i in appl:
        send_json['comment'].append({'userID': i[1], 'comment_time': i[4], 'content': i[5]})
    return send_json

def AddComment(request, num):
    with open('comment_serial.txt', 'r') as f:
        serial_num = int(f.read())
    stats = 'SUCCESS'
    cursor = connection.cursor()
    userID = '\'{userID}\''.format(userID=request['userID'])
    content = '\'{content}\''.format(content=request['content'])
    cursor.execute(
        'insert into article values({serial_num}, {userID}, {article_num}, {post_time}, {content})'.format(
            serial_num=serial_num,
            userID=userID,
            article_num=num,
            post_time='now()',
            content=content,
        ))
    with open('comment_serial.txt', 'w') as f:
        f.write(str(serial_num + 1))
    send_json = {
        'serial_num': serial_num,
        'stats': 'SUCCESS',
    }
    return send_json




def PostArticle(request):
    if request.method == 'POST':
        request = json.loads(request.body.decode('utf-8'))
        if(request['action']=='ADD_ARTICLE'):
            with open('article_serial.txt', 'r') as f:
                serial_num = int(f.read())
            stats = 'SUCCESS'
            cursor = connection.cursor()
            name = '\'{name}\''.format(name=request['class_name'])
            cursor.execute('select * from classification where name={name}'.format(name=name))
            appl = cursor.fetchall()
            if len(appl)==0:
                serial_num=-1
                stats = 'FAIL'
            else:
                author = '\'{author}\''.format(author=request['userID'])
                title = '\'{title}\''.format(title=request['title'])
                content = '\'{content}\''.format(content=request['content'])
                cursor.execute(
                    'insert into article values({serial_num}, {author}, {class_name}, {title}, {content}, {post_time})'.format(
                        serial_num=serial_num,
                        author=author,
                        class_name=name,
                        title=title,
                        content=content,
                        post_time='now()',
                    ))
                with open('article_serial.txt', 'w') as f:
                    f.write(str(serial_num + 1))
            send_json = {
                'serial_num': serial_num,
                'stats': stats,
            }
        elif(request['action']=='GET_CLASS_LIST'):
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
    return render(request, 'add.html')

def article(request, num):
    if request.method == 'POST':
        mes_json = json.loads(request.body.decode('utf-8'))
        if (mes_json['action'] == 'GET_ARTICLE_DATA'):
            send_js=ArticleData(mes_json, num)
        elif (mes_json['action'] == 'ADD_COMMENT'):
            send_js = AddComment(mes_json, num)
        return JsonResponse(send_js)
    return render(request, 'article.html')

# Create your views here.
