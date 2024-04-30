import requests

url = 'http://172.17.0.1:8080/v1/metadata'
params = {
	"type" : "pg_create_event_trigger",
	"args" : {
		"name": "new_request",
		"source": "default",
		"table": {
			"name": "requests",
			"schema": "public"
		},
		"webhook": "https://desired-insect-suitably.ngrok-free.app/new-request",
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

response = requests.post(url, json=params, headers=headers)
print(response.content)
