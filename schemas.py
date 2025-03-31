from typing import List, Dict
from datetime import date
from pydantic_core import Url
from pydantic import BaseModel

class IgnoreExtraBase(BaseModel):
    model_config = {"extra": "ignore"} #ignore any field that is not part of the model

class MissDistance(IgnoreExtraBase):
    astronomical: float
    lunar: float
    kilometers: float
    miles: float
class RelativeVelocity(IgnoreExtraBase):
    kilometers_per_second: float
    kilometers_per_hour: float
    miles_per_hour: float
class ApproachData(IgnoreExtraBase):
    close_approach_date: date
    relative_velocity: RelativeVelocity
    miss_distance: MissDistance
    orbiting_body: str
    
class DiameterF(IgnoreExtraBase):
    estimated_diameter_min: float
    estimated_diameter_max: float
class DiameterMi(IgnoreExtraBase):
    estimated_diameter_min: float
    estimated_diameter_max: float
class DiameterM(IgnoreExtraBase):
    estimated_diameter_min: float
    estimated_diameter_max: float
class DiameterKil(IgnoreExtraBase):
    estimated_diameter_min: float
    estimated_diameter_max: float
class NeoSize(IgnoreExtraBase):
    kilometers: DiameterKil
    meters: DiameterM
    miles: DiameterMi
    feet: DiameterF
    
class Neo(IgnoreExtraBase):
    id: int
    name: str
    nasa_jpl_url: Url
    estimated_diameter: NeoSize
    is_potentially_hazardous_asteroid: bool
    close_approach_data: List[ApproachData] # close approach data is a list of ApproachData models
    
    
class NeoMetaData(IgnoreExtraBase):
    element_count: int
    near_earth_objects: Dict[str, List[Neo]] # str for dynamic date and list for Neo objects

class NeoPages(IgnoreExtraBase):
    size: int
    total_elements: int
    total_pages: int
    number: int
class BrowseNeos(IgnoreExtraBase):
    page: NeoPages
    near_earth_objects: List[Neo] # list of Neo objects
    
class UserInput(IgnoreExtraBase):
    url: Url