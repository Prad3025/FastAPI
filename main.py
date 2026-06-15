from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/name")
def read_name ():
    return {"name": "Pradeep"}