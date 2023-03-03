import requests

url = 'http://0.0.0.0:5005/webhooks/rest/webhook'

res = requests.post(url, json={"message":"Когда перестают выдавать талоны? "})

print(res.text)