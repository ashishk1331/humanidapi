from fastapi import FastAPI
from human_id import generate_id

app = FastAPI()


@app.get("/")
def read_root():
    return {"query": generate_id(separator=" ")}