import requests
import json

# URLと送信するデータを定義
url = 'http://127.0.0.1:8888/api'
data = {
    'number': int(input("> "))
}

# JSON形式でデータを送信
response = requests.post(url, json=data)

# レスポンスを表示
print(f"Status code: {response.status_code}")
print(f"Response body: {response.json()}")
