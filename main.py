import requests
from dotenv import load_dotenv
import os
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import database, models, schemas

app =  FastAPI()

# load env variables
load_dotenv()
api_key = os.getenv("API_KEY")


@app.get("/test")
def testing():
    return {"test": "success"}
# r = requests.get(f'https://api.nasa.gov/neo/rest/v1/feed?start_date=2015-09-07&end_date=2015-09-08&api_key={api_key}')

# print(r.json())

'''
            {
                "links": {
                    "self": "http://api.nasa.gov/neo/rest/v1/neo/3709250?api_key=0mT18MGDzJyEJ8ro9ocAPogkqkCHJvLLDXRc26e3"
                },
                "id": "3709250",
                "neo_reference_id": "3709250",
                "name": "(2015 BY512)",
                "nasa_jpl_url": "https://ssd.jpl.nasa.gov/tools/sbdb_lookup.html#/?sstr=3709250",
                "absolute_magnitude_h": 21.49,
                "estimated_diameter": {
                    "kilometers": {
                        "estimated_diameter_min": 0.1338304618,
                        "estimated_diameter_max": 0.2992540101
                    },
                    "meters": {
                        "estimated_diameter_min": 133.8304618158,
                        "estimated_diameter_max": 299.2540100804
                    },
                    "miles": {
                        "estimated_diameter_min": 0.0831583679,
                        "estimated_diameter_max": 0.1859477635
                    },
                    "feet": {
                        "estimated_diameter_min": 439.0763323438,
                        "estimated_diameter_max": 981.8045264321
                    }
                },
                "is_potentially_hazardous_asteroid": false,
                "close_approach_data": [
                    {
                        "close_approach_date": "2025-03-10",
                        "close_approach_date_full": "2025-Mar-10 12:23",
                        "epoch_date_close_approach": 1741609380000,
                        "relative_velocity": {
                            "kilometers_per_second": "17.3279837746",
                            "kilometers_per_hour": "62380.7415886568",
                            "miles_per_hour": "38760.9669054629"
                        },
                        "miss_distance": {
                            "astronomical": "0.4434335602",
                            "lunar": "172.4956549178",
                            "kilometers": "66336716.092436774",
                            "miles": "41219723.9958405212"
                        },
                        "orbiting_body": "Earth"
                    }
                ],
                "is_sentry_object": false
            }



'''