import requests

url = 'http://172.17.0.1:8080/v1/metadata'
params = {
  "type": "add_remote_schema",
    "args": {
        "name": "Grasp",
        "definition": {
            "url": "http://172.17.0.1:4000",
            "headers": [{"name": "Content-Type", "value": "application/json"}],
            "forward_client_headers": False,
            "timeout_seconds": 60
        },
        "comment": "A server providing a bridge between GraphQL and SparQL (Ontology).",
    }
}

headers = {"Content-Type": "application/json", "X-Hasura-Role": "admin", "x-hasura-admin-secret": "mylongsecretkey"}

response = requests.post(url, json=params, headers=headers)
print(response.content)