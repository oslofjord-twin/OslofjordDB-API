import requests
import os

hasura_host = os.getenv("HASURA_HOST", "localhost")
hasura_url = f"http://{hasura_host}:8080/v1/metadata"

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
                "object_relationships": [
                    {
                        "name": "grid",
                        "using": {
                            "foreign_key_constraint_on": "grid_id"
                        }
                    }
                ],
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
                "object_relationships": [
                    {
                        "name": "grid",
                        "using": {
                            "foreign_key_constraint_on": "grid_id"
                        }
                    }
                ],
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
                        },
                        "id_sim": {
                            "comment": "The id of the simulation"
                        },
                        "grid_id": {
                            "comment": "The id of the grid"
                        }
                    },
                    "comment": "Simulation values for virtual landers"
                },
                "object_relationships": [
                    {
                        "name": "grid",
                        "using": {
                            "foreign_key_constraint_on": "grid_id"
                        }
                    }
                ],
                "apollo_federation_config": {
                    "enable": "v1"
                }
            },
            {
                "source": "default",
                "table": "grid",
                "configuration": {
                    "column_config": {
                        "geom": {
                          "comment": "The geometry of the grid"
                        },
                        "i": {
                            "comment": "The i value of the grid"
                        },
                        "j": {
                            "comment": "The j value of the grid"
                        },
                        "id": {
                            "comment": "The id for the grid"
                        }
                    },
                    "comment": "Grid for the Oslofjord"
                },
                "apollo_federation_config": {
                    "enable": "v1"
                }
            },
            {
                "source": "default",
                "table": "requests",
                "configuration": {
                    "column_config": {
                        "request_id": {
                          "comment": "The id for the request"
                        },
                        "grid_id": {
                            "comment": "The id for the grid"
                        },
                        "species_name": {
                            "comment": "The name of the species"
                        },
                        "done": {
                            "comment": "Boolean value signifying if the request is completed"
                        }
                    },
                    "comment": "Requests made by the front end to the monitoring component"
                },
                "object_relationships": [
                    {
                        "name": "grid",
                        "using": {
                            "foreign_key_constraint_on": "grid_id"
                        }
                    }
                ],
                "apollo_federation_config": {
                    "enable": "v1"
                }
            },
            {
                "source": "default",
                "table": "runtime_monitoring",
                "configuration": {
                    "column_config": {
                        "id": {
                          "comment": "The id for the row"
                        },
                        "request_id": {
                            "comment": "The id for the request"
                        },
                        "id_sim": {
                            "comment": "The id of the simulation"
                        },
                        "suitable_temperature": {
                            "comment": "The suitable temperature for the species"
                        },
                        "suitable_spawning_temperature": {
                            "comment": "The suitable spawning temperature for the species"
                        },
                        "preferred_spawning_temperature": {
                            "comment": "The preferred spawning temperature for the species"
                        }
                    },
                    "comment": "Runtime monitoring of the Oslofjord"
                },
                "apollo_federation_config": {
                    "enable": "v1"
                }
            }
        ]
    }
}

headers = {"Content-Type": "application/json",
           "X-Hasura-Role": "admin", "x-hasura-admin-secret": "mylongsecretkey"}

response = requests.post(hasura_url, json=params, headers=headers)
print(response.content)


def create_params(table_name: str, foreign_key: str) -> object:
    return {
        "type": "pg_create_object_relationship",
        "args": {
            "table": f"{table_name}",
            "name": "grid",
            "source": "default",
            "using": {
                "foreign_key_constraint_on": [f"{foreign_key}"]
            }
        }
    }


grid_id_tables = ["requests", "salinity", "simulations", "turbidity"]


for table in grid_id_tables:
    response = requests.post(hasura_url, json=create_params(table, "grid_id"), headers=headers)
    print(response.content)
