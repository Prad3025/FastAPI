from fastapi import FastAPI
from typing import List
from pydantic import BaseModel

app=FastAPI()

class User(BaseModel):
    name:str
    age:int
    interest:List[str]

class UserResponse(BaseModel):
    message:str
    user:User
    recommendation:List[str]

class Item(BaseModel):
    name:str
    price:float
    instock:bool

@app.get("/")
def read_root():
    return {"message":"Welcome to the recommendation API!"}

@app.get("/recommend")
def recommend_items(age:int,interest:str):
    if age<18:
        category="Teen"
    elif age<40:
        category="Adult"
    else:
        category="Senior"

    recommendations=[]
    if interest.lower()=='music':
        recommendations=["Spotify","Concert tickets"]
    elif interest.lower()=='sports':
        recommendations=["Sports equipment","Gym membership"]
    elif interest.lower()=='books':
        recommendations=["Bookstore gift card","E-book subscription"]
    else:
        recommendations=["General gift card","Online courses"]

    return {
        "category":category,
        "interest":interest,
        "recommendations":recommendations
    }

@app.post("/users",response_model=UserResponse)
def create_user(user:User):
    first_interest=user.interest[0] if user.interest else "General"
    recommendations=[]

    if first_interest.lower()=='music':
        recommendations=["Spotify","Concert tickets"]
    elif first_interest.lower()=='sports':
        recommendations=["Sports equipment","Gym membership"]
    elif first_interest.lower()=='books':
        recommendations=["Bookstore gift card","E-book subscription"]
    else:
        recommendations=["General gift card","Online courses"]

    return {
        "message":"User created successfully",
        "user":user,
        "recommendation":recommendations
    }

@app.post("/json")
def recieveJson(item:Item):
    return{
        "type":"JSON",
        "name":item.name,
        "price":item.price,
        "stock":item.instock
    }