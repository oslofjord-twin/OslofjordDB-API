import requests
import os

hasura_host = os.getenv("HASURA_HOST", "localhost")
hasura_url = f"http://{hasura_host}:8080/v1/metadata"

monitoring_host = os.getenv("MONITORING_HOST", "localhost")
monitoring_url = f"http://{monitoring_host}:5001/new-request"

params = {
	"type" : "pg_create_event_trigger",
	"args" : {
		"name": "new_request",
		"source": "default",
		"table": {
			"name": "requests",
			"schema": "public"
		},
		"webhook": monitoring_url,
		"insert": {
			"columns": "*"
		},
		"retry_conf": {
			"num_retries": 0,
			"interval_sec": 10,
			"timeout_sec": 60
		},
		"headers": [{
			"name": "secret-authorization-string",
			"value": "super_secret_string_123"
		}],
		"request_transform": {
			"method": "POST"
		}
	}
}

headers = {"Content-Type": "application/json", "X-Hasura-Role": "admin", "x-hasura-admin-secret": "mylongsecretkey"}

response = requests.post(hasura_url, json=params, headers=headers)
print(response.content)
