from pydantic import BaseModel

class Person(BaseModel):
    name:str
    age:int
    city:str

validData=Person(name="Pradeep",age=21,city="Hosur")
print(validData)