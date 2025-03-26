from typing import List, Dict
from datetime import datetime
from . import main
from pydantic import BaseModel, Field

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
    close_approach_date: datetime
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
    
class NeoCount(IgnoreExtraBase):
    count: int
    
class Neo(IgnoreExtraBase):
    id: int
    name: str
    estimated_diameter: NeoSize
    is_potentially_hazardous_asteroid: bool
    close_approach_data: List[ApproachData] 
    
    
class NeoMetaData(IgnoreExtraBase):
    element_count: int
    near_earth_objects: Dict[str, List[Neo]]
    
    # {hello: neo, hi: neo, gm: neo}