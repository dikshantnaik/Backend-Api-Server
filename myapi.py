from fastapi import FastAPI
import starlette.responses as _responses
user = {
    0: {
        "username":"dik",
        "password":"pass"
    },
     1: {
        "username":"dik2",
        "password":"pass2"
    }
}
i = 0

app = FastAPI()

@app.get("/")
def index():
    return _responses.RedirectResponse("/redoc")

@app.get("/register")
def register(user_id:int ,username: str,password:str):
    user[user_id] = {"username" : username ,"password":password}
    return "<h1>Register Succes for user " + username + "</h1>"

@app.get("/login")
def login(username:str,input_password:str):
    i = 0
    for i in range(user.__len__()):
        print(i)
        print(user[i])
        if(user[i]["username"]==username):
            if(user[i]["password"]==input_password):
                return "Loged In"
            else:
                return "Wrong Password Stupid !"
        
            
@app.get("/get_pass")
def get_pass(username:str):
    for i in range(user.__len__()):
        if(username == user[i]["username"]):
            return user[i]["password"]
    
    # return "Somthing is Fishy!lol"

@app.get('/check_user')
def check():
    return user;
    

        
    