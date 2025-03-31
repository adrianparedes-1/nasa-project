from pydantic_core import Url
import requests as rq
from models import SaveSearch
from fastapi import HTTPException, status

# there is still a problem here --- fixed!

'''
this is the solution:

https://github.com/fastapi/fastapi/issues/1693#issuecomment-665833384

'''

def save(endpoint: Url, db):
    x: bool = True
    # check if it's a valid request before asking to save search
    try:
        r = rq.get(endpoint)
        r.raise_for_status()
    except rq.exceptions.HTTPError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    
    while x:
        try:
            user = input("Do you want to save this search? : [Y]es or [N]o ? ")
        finally:
            if user.lower() == ('y' or 'yes'):
                x = False
                
                validate_endpoint = SaveSearch(url=endpoint)
                db.add(validate_endpoint)
                db.commit()
                
            elif user.lower() == ('n' or 'no'):
                x = False
                
            else:
                print("Enter a valid response.")

    return r

    