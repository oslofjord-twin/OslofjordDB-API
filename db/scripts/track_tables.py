import requests

url = 'http://host.docker.internal:8080/v1/metadata'
params = {
  "type": "bulk",
  "args": [
    {
       "type": "pg_track_table",
       "args": {
          "source": "default",
          "schema": "public",
          "name": "salinity"
       }
    },
    {
       "type": "pg_track_table",
       "args": {
          "source": "default",
          "schema": "public",
          "name": "turbidity"
       }
    }
  ]
}

headers = {"Content-Type": "application/json", "X-Hasura-Role": "admin", "X-Hasura-Access-Key": "mylongsecretkey"}

response = requests.post(url, json=params, headers=headers)
print(response.content)