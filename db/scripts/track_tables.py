import requests

url = 'http://host.docker.internal:8080/v1/metadata'
params = {
  "type": "pg_track_tables",
  "args": {
    "tables": [
      {
        "source": "default",
        "table": "salinity",
        "configuration": {
          "column_config": {
            "conductivity": {
              "comment": "The conductivity value"
            }
          },
          "comment": "Salinity in the Oslofjord"
        },
        "apollo_federation_config": {
          "enable": "v1"
        }
      },
      {
        "source": "default",
        "table": "turbidity",
        "configuration": {
            "comment": "Turbidity in the Oslofjord"
        },
        "apollo_federation_config": {
          "enable": "v1"
        }
      },
      {
        "source": "default",
        "table": "simulations",
        "configuration": {
          "comment": "Simulation values for virtual landers"
        },
        "apollo_federation_config": {
          "enable": "v1"
        }
      }
    ]
  }
}

headers = {"Content-Type": "application/json", "X-Hasura-Role": "admin", "x-hasura-admin-secret": "mylongsecretkey"}

response = requests.post(url, json=params, headers=headers)
print(response.content)