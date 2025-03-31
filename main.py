from pydantic import PositiveInt
import requests as rq
from dotenv import load_dotenv
import os
from fastapi import FastAPI, Depends, status, HTTPException
from sqlalchemy.orm import Session
from schemas import NeoMetaData, BrowseNeos, Neo
from models import SaveSearch
from database import get_db as sess
from save_search import save as s

app =  FastAPI()

# load env variables
load_dotenv()
api_key = os.getenv("API_KEY")


def result_validation(result):
    if not result:
        raise ValueError
    else:
        return result
    
@app.get("/test")
def testing(db: Session =  Depends(sess)):
    
    # single asteroid
    # return Neo.model_validate(r.json())
    
    #all asteroids
    result = NeoMetaData.model_validate(s(f'https://api.nasa.gov/neo/rest/v1/feed?detailed=false&api_key={api_key}', db).json())
    return result

# Get all NEOs

@app.get("/asteroids")
def get_asteroids(db: Session = Depends(sess)):
    try: 
        page = PositiveInt(input("Enter a page number (default: 0): "))
    except ValueError: # validating input error
        print("Invalid page number. Page value will default to 0.")
        page = 0
        
    try:
        page_size = PositiveInt(input("Enter a page size from 1 - 20 (default: 20): "))
    except ValueError: # validating input error
        page_size = 20
        print("Invalid page size. Page size value will default to 20.")
    
    endpoint = f'https://api.nasa.gov/neo/rest/v1/neo/browse?&page={page}&size={page_size}&api_key={api_key}'
    try:
        r = rq.get(endpoint)
        r.raise_for_status()
    except rq.exceptions.HTTPError: # catching 400
        if r.status_code == 400:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    
    result = BrowseNeos.model_validate(s(endpoint, db).json())
    
    return result_validation(result)


# Get all NEOs within a date range

@app.get("/asteroids/date_range")
def get_asteroids(db: Session = Depends(sess)):
    
    # prompt user for date range
    
    startDate = input("Enter a start date using this format YYYY-MM-DD: ")
    endDate = input("Enter an end date using this format YYYY-MM-DD: ")
    
    endpoint = f'https://api.nasa.gov/neo/rest/v1/feed?start_date={startDate}&end_date={endDate}&api_key={api_key}'

    try:
        r = rq.get(endpoint)
        r.raise_for_status()
    except rq.exceptions.HTTPError: # catching 400
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Bad Request -- please enter a valid date range and try again.")
    
    result = NeoMetaData.model_validate(s(endpoint, db).json())
    
    return result_validation(result)

        
    

# Get an individual NEO

@app.get("/asteroid/{id}")
def get_individual_asteroid(id: int, db: Session = Depends(sess)):
    
    endpoint = f'https://api.nasa.gov/neo/rest/v1/neo/{id}?api_key={api_key}'
    
    try:
        r = rq.get(endpoint)
        r.raise_for_status()
    except rq.exceptions.HTTPError: # catching 400
        if r.status_code == 400:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    
    result = Neo.model_validate(s(endpoint, db).json())
    
    return result_validation(result)



# Get search history

@app.get("/search_history")
def get_search_history(db: Session =  Depends(sess)):
    query = db.query(SaveSearch).all()

    if query:
        return query
    else:
        raise ConnectionError

@app.get("/search_history/{id}")
def get_search(id: int, db: Session = Depends(sess)):
    query = db.query(SaveSearch).filter(id == SaveSearch.id).first()
    
    if query:
        return query
    else:
        raise ConnectionError
    
'''
Optional Features:

Notifications: Send alerts or notifications when a significant asteroid is approaching Earth.
    ??
    I guess use the NEO query date range (relevancy )to check if there are potentially hazardous asteroids == True then return those ?
    

Save info about a specific asteroid to a persistent database.
    instead of saving search query, just s the json returned

Update only the necessary fields for a specific asteroid.
    once the previous feature is created then work on this one
    
Finally just implement soft delete and pagination

'''