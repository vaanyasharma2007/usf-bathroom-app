from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the bathroom availability app!"}
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
        "status":"available"},
        {
            "id":2,
            "building":"Castor hall",
            "floor":1,
            "gender":"women",
            "area_type":"shower",
            "total_units":6,
            "available_units":2,
            "status":"available"
        }

    ]
    