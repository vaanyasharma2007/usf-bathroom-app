from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
# Represents a bathroom area in the application
class BathroomArea(BaseModel):
    id:int
    building:str
    floor:int
    gender:str
    area_type:str
    total_units:int
    available_units:int
    is_out_of_service:bool
@app.get("/")
def home():
    return {"message": "Welcome to the bathroom availability app!"}
# determines bathroom availability based on occupany and maintance status
def get_status(available_units,is_out_of_service):
    if is_out_of_service:
        return "out_of_service"
    if available_units>0:
        return "available"
    elif available_units==0:
        return "occupied"
    elif available_units<0:
        return None
    
@app.get("/bathrooms")
def get_bathrooms():

    return [
        {"id":1,
        "building":"Castor hall",
        "floor":1,
        "gender":"women",
        "area_type":"toilet",
        "total_units":5,
        "available_units":3,
        "status":get_status(3,False)},
        {
            "id":2,
            "building":"Castor hall",
            "floor":1,
            "gender":"women",
            "area_type":"shower",
            "total_units":6,
            "available_units":2,
            "status":get_status(2,False)
        }

    ]
    