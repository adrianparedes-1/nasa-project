import requests
from dotenv import load_dotenv
import os
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import database, models, schemas
from pydantic_core import from_json

app =  FastAPI()

# load env variables
load_dotenv()
api_key = os.getenv("API_KEY")

@app.get("/test")
def testing():
    # prompt user for date range
    # startDate = input("Enter a start date using this format YYYY-MM-DD: ")
    # endDate = input("Enter an end date using this format YYYY-MM-DD: ")
    
    # r = requests.get(f'https://api.nasa.gov/neo/rest/v1/feed?start_date={startDate}&end_date={endDate}&api_key={api_key}')
    r = requests.get(f'https://api.nasa.gov/neo/rest/v1/feed?start_date=2024-10-11&end_date=2024-10-11&api_key={api_key}')
    print(r.status_code)  # check for any issues
    # validation = from_json(r.json(), allow_partial=True)
    # print(validation)
    # validation = schemas.Neo.model_dump(**r.json(), exclude='links')
    
    print(schemas.NeoMetaData.model_validate_json(r.text))
    return schemas.NeoMetaData.model_validate_json(r.text)

@app.get("/asteroids")
def get_asteroids():
    pass

# current issue ---------------
# Parsing json and only returning the information that matches the pydantic schema
'''
            "links": {
        "next": "http://api.nasa.gov/neo/rest/v1/feed?start_date=2024-10-12&end_date=2024-10-12&detailed=false&api_key=0mT18MGDzJyEJ8ro9ocAPogkqkCHJvLLDXRc26e3",
        "prev": "http://api.nasa.gov/neo/rest/v1/feed?start_date=2024-10-10&end_date=2024-10-10&detailed=false&api_key=0mT18MGDzJyEJ8ro9ocAPogkqkCHJvLLDXRc26e3",
        "self": "http://api.nasa.gov/neo/rest/v1/feed?start_date=2024-10-11&end_date=2024-10-11&detailed=false&api_key=0mT18MGDzJyEJ8ro9ocAPogkqkCHJvLLDXRc26e3"
    },
    "element_count": 18,
    "near_earth_objects": {
        "2024-10-11": [
            {
                "links": {
                    "self": "http://api.nasa.gov/neo/rest/v1/neo/3639439?api_key=0mT18MGDzJyEJ8ro9ocAPogkqkCHJvLLDXRc26e3"
                },
                "id": "3639439",
                "neo_reference_id": "3639439",
                "name": "(2013 LB)",
                "nasa_jpl_url": "https://ssd.jpl.nasa.gov/tools/sbdb_lookup.html#/?sstr=3639439",
                "absolute_magnitude_h": 22.8,
                "estimated_diameter": {
                    "kilometers": {
                        "estimated_diameter_min": 0.0732073989,
                        "estimated_diameter_max": 0.1636967205
                    },
                    "meters": {
                        "estimated_diameter_min": 73.2073989347,
                        "estimated_diameter_max": 163.696720474
                    },
                    "miles": {
                        "estimated_diameter_min": 0.0454889547,
                        "estimated_diameter_max": 0.1017163949
                    },
                    "feet": {
                        "estimated_diameter_min": 240.181762721,
                        "estimated_diameter_max": 537.0627483999
                    }
                },
                "is_potentially_hazardous_asteroid": false,
                "close_approach_data": [
                    {
                        "close_approach_date": "2024-10-11",
                        "close_approach_date_full": "2024-Oct-11 16:40",
                        "epoch_date_close_approach": 1728664800000,
                        "relative_velocity": {
                            "kilometers_per_second": "20.1270694374",
                            "kilometers_per_hour": "72457.4499745792",
                            "miles_per_hour": "45022.2416244823"
                        },
                        "miss_distance": {
                            "astronomical": "0.3425269505",
                            "lunar": "133.2429837445",
                            "kilometers": "51241302.212395435",
                            "miles": "31839868.760449603"
                        },
                        "orbiting_body": "Earth"
                    }
                ],
                "is_sentry_object": false
            },



'''