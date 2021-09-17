from typing import Optional
from fastapi import FastAPI
print("Starting ")
app = FastAPI()

@app.get("/")
def index():
    return "heya There Bitches"

# @app.get("/item/{item_id}")
# def read_item(item_id: int ,q :Optional[str] = None):
#     return {"item_it" : item_id,"q":q}