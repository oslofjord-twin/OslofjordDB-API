import requests

url = 'http://172.17.0.1:8080/v1/metadata'
params = {
  "type": "pg_track_tables",
  "args": {
    "tables": [
      {
        "source": "default",
        "table": "salinity",
        "configuration": {
          "column_config": {
            "record_time": {
                "comment": "The record time. (timestamptz)"
            },
            "record_number": {  
                "comment": "The record number"
            },
            "sensor_status": {
                "comment": "The status of the sensor"
            },
            "conductivity": {
              "comment": "The conductivity value"
            },
            "temperature": {
                "comment": "The temperature value in degrees Celsius"
            },
            "location": {
                "comment": "The location of the measurement. (PostGIS-location)"
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
          "column_config": {
              "c1_amp": {
                  "comment": "The c1 amp value"
              },
              "c2_amp": {
                  "comment": "The c2 amp value"
              },
              "location": {
                  "comment": "The location of the measurement. (PostGIS-location)"
              },
              "raw_temp": {
                  "comment": "The raw temperature value"
              },
              "record_number": { 
                  "comment": "The record number"
              },
              "record_time": {
                "comment": "The record time. (timestamptz)"
              },
              "sensor_status": {
                  "comment": "The status of the sensor"
              },
              "temperature": {
                  "comment": "The temperature value in degrees Celsius"
              },
              "turbidity": {
                  "comment": "The turbidity value. Turbidity is the measure of relative clarity of a liquid"
              },
              "txc_amp": {
                  "comment": "The txc amp value"
              }
            },
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
            "column_config": {
                "conductivity": {
                    "comment": "The conductivity value"
                },
                "location": {
                    "comment": "The location of the measurement. (PostGIS-location)"
                },
                "record_time": {
                    "comment": "The record time. (timestamptz)"
                },
                "temperature": {
                    "comment": "The temperature value in degrees Celsius"
                },
                "turbidity": {
                    "comment": "The turbidity value. Turbidity is the measure of relative clarity of a liquid"
                }
            },
          "comment": "Simulation values for virtual landers"
        },
        "apollo_federation_config": {
          "enable": "v1"
        }
      },
      {
        "source": "default",
        "table": "grid",
        "configuration": {
          "comment": "Grid for the Oslofjord"
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