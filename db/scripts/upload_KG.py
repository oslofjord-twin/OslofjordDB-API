import requests

url = 'http://172.17.0.1:3030/ds/data'
data = open('ontology.ttl').read()
headers = {'Content-Type': 'text/turtle;charset=utf-8'}
response = requests.post(url, data=data, headers=headers)
print(response.content)