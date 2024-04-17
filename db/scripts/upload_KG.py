import requests

# First delete if fuseki already contains our ontology.
url = 'http://172.17.0.1:3030/ds/update'
headers = {'Content-Type': 'application/sparql-update'}
response = requests.post(url, data="DROP default", headers=headers)
print(response.content)

# Then upload the new ontology
url = 'http://172.17.0.1:3030/ds/data'
data = open('ontology.ttl').read()
headers = {'Content-Type': 'text/turtle;charset=utf-8'}
response = requests.post(url, data=data, headers=headers)
print(response.content)