from flask import Flask, request, jsonify
from dotenv.main import load_dotenv
import os
import psycopg2
from psycopg2 import Error
from datetime import datetime
import time  

load_dotenv()
API_PASSWORD = os.environ['API_PASSWORD']
DB_NAME = os.environ['DB_NAME']
DB_USER = os.environ['DB_USER']
DB_PASSWORD = os.environ['DB_PASSWORD']
DB_HOST = os.environ['DB_HOST']
conn = psycopg2.connect(dbname = DB_NAME, user = DB_USER, 
                        password = DB_PASSWORD, host = DB_HOST)
cursor = conn.cursor()
app = Flask(__name__)
'''
Заглавная страница api
'''
@app.route('/')
def index():
    if(ispassword(request.args.get("api_password"))):
        return jsonify("Доступ открыт")
    else:
        return jsonify("Доступ закрыт")
'''
Страница пользователя отображение
'''
@app.route('/user/view', methods=['GET'])
def userView():
    if(ispassword(request.args.get("api_password"))):
        id = request.args.get("id")
        cursor.execute("SELECT * FROM public.users where id=%s",(id))
        records = cursor.fetchall()
        return jsonify(records)
    else:
        return jsonify("Доступ закрыт")
'''
Страница пользователя добавление
'''
@app.route('/user/add', methods=['GET'])
def userAdd():
    if(ispassword(request.args.get("api_password"))):
        idUser = request.args.get("id_user")
        userName = request.args.get("username")
        timeStamp = datetime.fromtimestamp (time.time())
        cursor.execute("INSERT INTO public.users (id_user, username,created_on) VALUES (%s, %s, %s)",(idUser,userName,timeStamp))
        conn.commit()
        return jsonify("Данные пользователя добавлены")
    else:
        return jsonify("Доступ закрыт")
'''
Страница получения данных группы
'''
@app.route('/group/view', methods=['GET'])
def groupView():
    if(ispassword(request.args.get("api_password"))):
        id = request.args.get("id")
        cursor.execute("SELECT * FROM public.groups where id=%s",(id))
        records = cursor.fetchall()
        return jsonify(records)
    else:
        return jsonify("Доступ закрыт")
'''
Страница добавление группы
'''
@app.route('/group/save', methods=['GET'])
def groupSave():
    if(ispassword(request.args.get("api_password"))):
        idUser = request.args.get("id_user")
        userName = request.args.get("username")
        timeStamp = datetime.fromtimestamp (time.time())
        cursor.execute("INSERT INTO public.groups (id_user, id_group, created_on, value, title) VALUES (%s, %s, %s)",(idUser,userName,timeStamp))
        conn.commit()
        return jsonify("Данные пользователя добавлены")
    else:
        return jsonify("Доступ закрыт")
'''
Страница получения сообщений группы
'''
@app.route('/message/view', methods=['GET'])
def groupMessage():
    if(ispassword(request.args.get("api_password"))):
        id = request.args.get("id")
        cursor.execute("SELECT * FROM public.groups where id=%s",(id))
        records = cursor.fetchall()
        return jsonify(records)
    else:
        return jsonify("Доступ закрыт")
'''
Страница добавление сообщений группы
'''
@app.route('/message/save', methods=['GET'])
def groupSave():
    if(ispassword(request.args.get("api_password"))):
        idUser = request.args.get("id_user")
        idGroup = request.args.get("id_group")
        value = request.args.get("value")
        title = request.args.get("title")
        timeStamp = datetime.fromtimestamp (time.time())
        cursor.execute("INSERT INTO public.groups (id_user, id_group, created_on, value, title) VALUES (%s, %s, %s, %s, %s)",(idUser, idGroup, timeStamp, value, title))
        conn.commit()
        return jsonify("Данные пользователя добавлены")
    else:
        return jsonify("Доступ закрыт")
'''
Функция проверки доступа
'''
def ispassword(password):
    if password == API_PASSWORD: 
        return True
    else:
        return False
    
if __name__ == '__main__':
    app.run(debug=True)
    cursor.close()
    conn.close()