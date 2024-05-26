import requests

url = 'http://127.0.0.1:8888/api'
data = {
    'number': int(input("> "))
}

response = requests.post(url, json=data)

# レスポンスを表示
print(f"Status code: {response.status_code}")
print(f"Response body: {response.json()}")
