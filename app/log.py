import logging
from flask import Flask, request, jsonify

app = Flask(__name__)

# Настройка логгера, вывод логов в файл
logger = logging.getLogger('user_registration')
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')


info_handler = logging.FileHandler('registration_info.log', mode='a')
info_handler.setLevel(logging.INFO)
info_handler.setFormatter(formatter)

error_handler = logging.FileHandler('registration_error.log', mode='a')
error_handler.setLevel(logging.ERROR)
error_handler.setFormatter(formatter)

logger.addHandler(info_handler)
logger.addHandler(error_handler)


@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    email = data.get('email')
    ip = request.remote_addr

    user_info = f'User: {{"username":"{username}", "email":"{email}"}}'
    endpoint = '/register'

    try:
        # Здесь логика регистрации,
        # например, проверка существует ли email в БД
        if email_exists(email):
            error_msg = 'Email already exists'
            logger.error(f'{endpoint} - IP: {ip} - {user_info} - Error: {error_msg}')
            return jsonify({"error": error_msg}), 400

        # Создание пользователя
        create_user(username, email)

        logger.info(f'{endpoint} - IP: {ip} - {user_info} - Registration successful')
        return jsonify({"message": "User successfully registered"}), 201

    except Exception as e:
        logger.error(f'{endpoint} - IP: {ip} - {user_info} - Exception: {str(e)}')
        return jsonify({"error": "Internal server error"}), 500


def email_exists(email):
    # имитация проверки email в базе
    existing_emails = ['ivan@example.com', 'test@example.com']
    return email in existing_emails

def create_user(username, email):
    # имитация создания пользователя
    pass

if __name__ == 'main':
    app.run(debug=True)
