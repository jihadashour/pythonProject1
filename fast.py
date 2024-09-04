from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def Hi():
    return {"message": "Hello World"}

@app.get("/bader")
def bader_washah(x: str , y : str , z: str):

    if x=="jihad" and y =="love" and z=="bader":
        p = "U GOT IT"

        return {"**" : p}
    else:
        return {"message": "NOOOO"}