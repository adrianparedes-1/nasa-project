from sqlalchemy import Boolean, DateTime, Float, ForeignKey, Integer, Text, func, sql
from sqlalchemy.orm import DeclarativeBase, mapped_column

class Base(DeclarativeBase):
    pass


class SaveSearch(Base):
    __tablename__ = 'search_history'
    id = mapped_column(Integer, primary_key=True)
    url = mapped_column(Text, nullable=False)
    # asteroid_name = mapped_column(Text)
    # date_range = mapped_column(DateTime)
    created_at = mapped_column(DateTime(timezone=True), server_default=func.now())
    
class NeoMetaData(Base):
    __tablename__ = 'metadata'
    id = mapped_column(Integer, primary_key=True)
    element_count = mapped_column(Integer)
    near_earth_objects = mapped_column(Integer)
    search_history = mapped_column(Integer, ForeignKey('search_history.id'))


class Neo(Base):
    __tablename__ = 'asteroid'
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(Text, nullable=False)
    nasa_jpl_url = mapped_column(Text, nullable=False)
    size = mapped_column(Integer, ForeignKey('neo_size.id'))
    hazardous = mapped_column(Boolean, nullable=False)
    close_approach_data = mapped_column(Integer, ForeignKey('approach_data.id'))
    search_history = mapped_column(Integer, ForeignKey('search_history.id'))
    created_at = mapped_column(DateTime(timezone=True), onupdate=sql.func.now())

    

class Neo_Size(Base):
    __tablename__ = 'neo_size'
    id = mapped_column(Integer, primary_key=True)
    kilometers = mapped_column(Integer, ForeignKey('size_in_kilometers_details.id'))
    meters = mapped_column(Integer, ForeignKey('size_in_meters_details.id'))
    miles = mapped_column(Integer, ForeignKey('size_in_miles_details.id'))
    feet = mapped_column(Integer, ForeignKey('size_in_feet_details.id'))

class Size_In_Kilometers(Base):
    __tablename__ = 'size_in_kilometers_details'
    id = mapped_column(Integer, primary_key=True)
    diameter_min_meters = mapped_column(Float, nullable=False)
    diameter_max_meters = mapped_column(Float, nullable=False)

class Size_In_Meters(Base):
    __tablename__ = 'size_in_meters_details'
    id = mapped_column(Integer, primary_key=True)
    diameter_min_meters = mapped_column(Float, nullable=False)
    diameter_max_meters = mapped_column(Float, nullable=False)
    
class Size_In_Miles(Base):
    __tablename__ = 'size_in_miles_details'
    id = mapped_column(Integer, primary_key=True)
    diameter_min_meters = mapped_column(Float, nullable=False)
    diameter_max_meters = mapped_column(Float, nullable=False)

class Size_In_Feet(Base):
    __tablename__ = 'size_in_feet_details'
    id = mapped_column(Integer, primary_key=True)
    diameter_min_meters = mapped_column(Float, nullable=False)
    diameter_max_meters = mapped_column(Float, nullable=False)

class Close_Approach_Data(Base):
    __tablename__ = 'approach_data'
    id = mapped_column(Integer, primary_key=True)
    date = mapped_column(DateTime, nullable=False)
    relative_velocity = mapped_column(Integer, ForeignKey('relative_velocity.id'))
    miss_distance = mapped_column(Integer, ForeignKey('miss_distance.id'))
    orbiting_body = mapped_column(Text, nullable=False)
    
    
class Relative_Velocity(Base):
    __tablename__ = 'relative_velocity'
    id = mapped_column(Integer, primary_key=True)
    kilometers_per_second = mapped_column(Float)
    kilometers_per_hour = mapped_column(Float)
    miles_per_hour = mapped_column(Float)
    

class Miss_Distance(Base):
    __tablename__ = 'miss_distance'
    id = mapped_column(Integer, primary_key=True)
    astronomical = mapped_column(Float)
    lunar = mapped_column(Float)
    kilometers = mapped_column(Float)
    miles = mapped_column(Float)