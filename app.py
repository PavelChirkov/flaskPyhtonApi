from flask import Flask, request, jsonify
from dotenv.main import load_dotenv
import os


load_dotenv()
API_PASSWORD = os.environ['API_PASSWORD']

app = Flask(__name__)

'''
Заглавная страница api
'''
@app.route('/')
def index():
    if(ispassword(request.args.get("api_password"))):
        return jsonify("Открытая страница")
    else:
        return jsonify("Доступ закрыт")

'''
Страница получения записи из группы
'''
@app.route('/get/note', methods=['GET'])
def note():
    return "Last Note"


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