from pydantic_core import Url
import requests
from fastapi import Depends
from database import get_db
from sqlalchemy.orm import Session
from models import SaveSearch

# there is still a problem here 

'''
this is the solution:

https://github.com/fastapi/fastapi/issues/1693#issuecomment-665833384

'''

def save(endpoint: Url, db: Session = Depends(get_db)):
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