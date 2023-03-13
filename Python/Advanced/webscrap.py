import requests
import json
url = "https://fakestoreapi.com/products/1"
data = requests.get(url)
print(data)
print(type(data.text))
j=json.loads(data.text)
print(j)
print(type(j))
