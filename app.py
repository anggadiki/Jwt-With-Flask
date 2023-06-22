from flask import Flask, request, jsonify, make_response
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)

# Konfigurasi jwt
app.config['JWT_SECRET_KEY'] = 'fasghjdewqgyqewr1234567890askd'  # bisa diubah
jwt = JWTManager(app)

# Data pengguna untuk autentikasi
users = {
    'angga': 'password1',
    'yuha': 'password2'
}

# Membuat endpoint untuk autentifikasi dan menghasilkan token jwt
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    if username in users and users[username] == password:
        access_token = create_access_token(identity=username)
        return make_response(jsonify(access_token=access_token), 200)
    else:
        return make_response(jsonify({'error': 'Invalid username or password'}), 401)

# Endpoint yang membutuhkan autentikasi menggunakan token JWT
@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return make_response(jsonify({'message': f'Hello, {current_user}! This is a protected route.'}), 200)

if __name__ == '__main__':
    app.run(debug=True)
