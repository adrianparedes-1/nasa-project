from pydantic import PositiveInt
import requests
from dotenv import load_dotenv
import os
from fastapi import FastAPI, Depends, status, HTTPException
from sqlalchemy.orm import Session
from schemas import NeoMetaData, BrowseNeos, Neo
from models import SaveSearch
from database import get_db

app =  FastAPI()

# load env variables
load_dotenv()
api_key = os.getenv("API_KEY")


@app.get("/test")
def testing(db: Session =  Depends(get_db)):
    
    # prompt user for date range
    # startDate = input("Enter a start date using this format YYYY-MM-DD: ")
    # endDate = input("Enter an end date using this format YYYY-MM-DD: ")
    # r = requests.get(f'https://api.nasa.gov/neo/rest/v1/feed?start_date={startDate}&end_date={endDate}&api_key={api_key}')
    
    #test request (default: start date = today, end date = 7 days from today)
    
    # single asteroid
    # r = requests.get(f'https://api.nasa.gov/neo/rest/v1/neo/3542519?api_key={api_key}')    
    
    #get all asteroids within the default range
    # r = requests.get(f'https://api.nasa.gov/neo/rest/v1/feed?detailed=false&api_key={api_key}')    
    endpoint = f'https://api.nasa.gov/neo/rest/v1/feed?detailed=false&api_key={api_key}'
    # print(r.status_code)  # check for any issues
    x: bool = True
    while x:
        try:
            user = input("save: [Y]es or [N]o ?")
        finally:
            if user.lower() == ('y' or 'yes'):
                x = False
                
                r = requests.get(endpoint)
                y = SaveSearch(url=endpoint)
                db.add(y)
                db.commit()
                
            elif user.lower() == ('n' or 'no'):
                x = False
                return "success"
            else:
                print("Enter a valid response.")
    
            
        
    # print(NeoMetaData.model_validate(r.json()))
    
    # single asteroid
    # return Neo.model_validate(r.json())
    
    #all asteroids
    return NeoMetaData.model_validate(r.json())


# Get all NEOs

@app.get("/asteroids")
def get_asteroids():
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
        
    try:
        r = requests.get(f'https://api.nasa.gov/neo/rest/v1/neo/browse?&page={page}&size={page_size}&api_key={api_key}')
        r.raise_for_status()
    except requests.exceptions.HTTPError: # catching 400
        if r.status_code == 400:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

    return BrowseNeos.model_validate(r.json())

# Get all NEOs within a date range

@app.get("/asteroids/date_range")
def get_asteroids():
    
    # prompt user for date range

    startDate = input("Enter a start date using this format YYYY-MM-DD: ")
    endDate = input("Enter an end date using this format YYYY-MM-DD: ")
    
    try:
        r = requests.get(f'https://api.nasa.gov/neo/rest/v1/feed?start_date={startDate}&end_date={endDate}&api_key={api_key}')
        r.raise_for_status()
    except requests.exceptions.HTTPError: # catching 400
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Bad Request -- please enter a valid date range and try again.")

    return NeoMetaData.model_validate(r.json())
    

# Get an individual NEO

@app.get("/asteroid/{id}")
def get_individual_asteroid(id: int):
    try:
        r = requests.get(f'https://api.nasa.gov/neo/rest/v1/neo/{id}?api_key={api_key}')
        print(r.raise_for_status())
    except requests.exceptions.HTTPError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
        
    return Neo.model_validate(r.json())


# Search History: Let users save their asteroid searches (by date, id, etc.) to a database for quick access.
'''
 Instead of saving the output of a recent search, we can save the query itself to avoid cluttering our db.
 
 Plan:
 1. add the post to db functionality to get requests
 2. it can be under any get request since we only need to save the url string with the query parameters
 3. create a new get request from the db instead of nasa api
 4. retrieve the url from db and run it with the requests module
 
'''
@app.get("/")
def get_search(db: Session =  Depends(get_db)):
    pass

'''
Optional Features:


Notifications: Send alerts or notifications when a significant asteroid is approaching Earth.

Save info about a specific asteroid to a persistent database.

Update only the necessary fields for a specific asteroid.

'''