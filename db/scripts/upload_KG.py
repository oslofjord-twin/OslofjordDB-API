import requests
import os

fuskei_host = os.getenv("FUSEKI_HOST", "localhost")
fuskei_url = f"http://{fuskei_host}:3030/ds"

# First delete if fuseki already contains our ontology.
url = f'{fuskei_url}/update'
headers = {'Content-Type': 'application/sparql-update'}
response = requests.post(url, data="DROP default", headers=headers)
print(response.content)

# Then upload the new ontology
url = f'{fuskei_url}/data'
data = open('ontology.ttl').read()
headers = {'Content-Type': 'text/turtle;charset=utf-8'}
response = requests.post(url, data=data, headers=headers)
print(response.content)