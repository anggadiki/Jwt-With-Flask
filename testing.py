import requests

# Endpoint API yang ingin diuji
login_url = 'http://localhost:5000/login'
protected_url = 'http://localhost:5000/protected'

# Permintaan login dengan username dan password
login_data = {'username': 'yuha', 'password': 'password2'}
response = requests.post(login_url, json=login_data)
access_token = response.json()['access_token']

# Mengirim permintaan GET ke endpoint yang dilindungi dengan token JWT
headers = {'Authorization': f'Bearer {access_token}'}
response = requests.get(protected_url, headers=headers)

# Menampilkan respons dari API
print(response.json())
