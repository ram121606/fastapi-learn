from fastapi import FastAPI,Request
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"] 
)



class postReq(BaseModel):
    name : str

@app.get("/")
def hi():
    return "hi"

@app.get("/{name}")
def main(name):
    return name

@app.post("/data")
def post(name : postReq):
    result = name.name
    return "Hello "+result

if __name__ == "__main__":
    uvicorn.run("app:app",reload=True)
