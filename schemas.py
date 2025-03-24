from datetime import datetime
from pydantic import BaseModel

class MissDistance(BaseModel):
    astronomical: float
    lunar: float
    kilometers: float
    miles: float
class RelativeVelocity(BaseModel):
    kilometers_per_second: float
    kilometers_per_hour: float
    miles_per_hour: float
class ApproachData(BaseModel):
    date: datetime
    relative_velocity: RelativeVelocity
    miss_distance: MissDistance
    orbiting_body: str
class NeoSize(BaseModel):
    diameter_min: float
    diameter_max: float
    
class Neo(BaseModel):
    id: int
    name: str
    size: NeoSize
    hazardous: bool
    approach_data: ApproachData
    