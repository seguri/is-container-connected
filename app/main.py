import requests
from typing import Union
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/ip")
def fetch_ip():
    r = requests.get("http://whatismyip.akamai.com")
    if r.status_code == 200:
        return r.text
    return f"{r.status_code} {r.reason}"


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
