import requests
import os

hasura_host = os.getenv("HASURA_HOST", "localhost")
hasura_url = f"http://{hasura_host}:8080/v1/metadata"

grasp_host = os.getenv("GRASP_HOST", "localhost")
grasp_url = f"http://{grasp_host}:4000"

params = {
  "type": "add_remote_schema",
    "args": {
        "name": "Grasp",
        "definition": {
            "url": grasp_url,
            "headers": [{"name": "Content-Type", "value": "application/json"}],
            "forward_client_headers": False,
            "timeout_seconds": 60
        },
        "comment": "A server providing a bridge between GraphQL and SparQL (Ontology).",
    }
}

headers = {"Content-Type": "application/json", "X-Hasura-Role": "admin", "x-hasura-admin-secret": "mylongsecretkey"}

response = requests.post(hasura_url, json=params, headers=headers)
print(response.content)