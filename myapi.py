from fastapi import FastAPI,Response
from fastapi.responses import JSONResponse
from starlette.requests import Request
import starlette.responses as _responses
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = ["*"]
user = {}
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def index():
    return _responses.RedirectResponse("/docs")

@app.post("/signup")
async def register(request:Request):
    data  = await request.json()
    print(data["username"])
    res = {"req":"true"}
    return JSONResponse(content=res)

@app.post("/login")
async def login(req:Request):
    data = await req.json()
    print(data["username"])
    # i = 0
    # for i in range(user.__len__()):
    #     print(i)
    #     print(user[i])
    #     if(user[i]["username"]==username):
    #         if(user[i]["password"]==input_password):
    #             return "Loged In"
    #         else:
    #             return "Wrong Password Stupid !"
        
            
@app.get("/get_pass")
def get_pass(username:str):
    for i in range(user.__len__()):
        if(username == user[i]["username"]):
            return user[i]["password"]
    
    # return "Somthing is Fishy!lol"

@app.get('/check_user')
def check():
    return user;
    

        
    