import requests
import json


# 200 - Success
# 300 - redirect
# 400 - error/not available

data = {'jokes':[]}
for i in range(10):
    response = requests.get("https://api.chucknorris.io/jokes/random")
    data['jokes'].append(response.json()['value'])

with open('./chucks_jokes.json', mode='a') as file:
    json.dump(data, file)

json_file = 'chucks_jokes.json'
with open(json_file, 'r') as file_obj:
    jokes = json.load(file_obj)

print(jokes)

