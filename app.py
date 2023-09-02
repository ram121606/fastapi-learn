from fastapi import FastAPI,Request
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pymongo import MongoClient

app = FastAPI()
client = MongoClient("mongodb://localhost:27017/")

db = client['react-db']
coll = db['users']


app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"] 
)



class main(BaseModel):
    name : str
    password : str
    

@app.get("/")
def hi():
    return "hi"

# @app.get("/{name}")
# def main(name):
#     return name

# @app.post("/data")
# def post(name : postReq):
#     result = name.name
#     return "Hello "+result

@app.post("/signup")
def register(obj:main):
    data = obj.model_dump()
    result = coll.find_one(data)
    if(result):
        print(result)
        return "false"
    else:
        coll.insert_one(data)
        print("Inserted")
        return "true"
    
@app.get('/login/{name}')
def login(name):
    result = coll.find_one({"name":name})
    print(result)
    if(result):
        return {"name":result['name'] , "password":result['password']}
    else:
        return "false"
    
    


if __name__ == "__main__":
    uvicorn.run("app:app",reload=True)
