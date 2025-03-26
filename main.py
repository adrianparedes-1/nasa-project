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
    
    #test request
    r = requests.get(f'https://api.nasa.gov/neo/rest/v1/feed?start_date=2024-10-11&end_date=2024-10-11&api_key={api_key}')
    
    
    print(r.status_code)  # check for any issues
    
    # print(schemas.NeoMetaData.model_validate(r.json()))
    
    return schemas.NeoMetaData.model_validate(r.json())

@app.get("/asteroids")
def get_asteroids():
    pass
