from typing import Optional
from fastapi import FastAPI
from starlette.responses import RedirectResponse

app = FastAPI()
item = {
    1:{
        "item_name":"Khana",
        "item_prize":100,
        "item_disc":"TASYYYY"
    },
    2:{
        "item_name":"Pina",
        "item_prize":1344,
        "item_discL":"Need"
    }
}


@app.get("/")
async def root():
    res = RedirectResponse(url='/docs')
    return res
@app.get("/item/{item_id}")
def read_item(item_id: int ,q :Optional[str] = None):
    res = item[item_id]
    if q=="Hello":
        res="ha Hello,bol"
        
    return res;