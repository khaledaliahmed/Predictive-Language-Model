## this is client page to path the data and get result from the API at the vscode window


import json 
import requests

data = {"How are you?"}

url = 'http://127.0.0.1:8000/predict/'


data = json.dumps(data)
response = requests.post(url, data)
print (response)