from flask import Flask, request, Response
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

# Моковые данные пользователя
users = {
    "admin": "avangard"  # Логин: admin, Пароль: password123
}

# Проверка пользователя и пароля
@auth.verify_password
def verify_password(username, password):
    if username in users and users[username] == password:
        return username
    return None

@app.route('/')
@auth.login_required  # Требуется авторизация
def index():
    return "Добро пожаловать на защищённую страницу!"

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)