from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Allow all origins
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

class Name(BaseModel):
    first_name: str
    last_name: str

@app.post('/login')
async def welcome(name: Name):
    return {"message": f"Request confirmation: Welcome Mister/Miss {name.first_name} {name.last_name}"}
