from datetime import timedelta,timezone
from functools import wraps

from flask import Flask
from flask.globals import session
from flask.wrappers import Request
from flask_restful import Resource,Api,reqparse
from flask_cors import CORS, cross_origin
from flask import request
from .views import *
from jwt import ExpiredSignatureError
import jwt
app = Flask(__name__)
cors = CORS(app)

app.config['SECRET_KEY'] = 'd6d37c6ade12464493ad0feb6105bd06'
app.config['CORS_HEADERS'] = 'Content-Type'
api = Api(app)

def genrate_token(username):
    try:
        token = jwt.encode({
            'user':username,
            "exp": datetime.now(tz=timezone.utc) + timedelta(seconds=20)
        },app.config["SECRET_KEY"])
        return token.decode('utf-8')

    except ExpiredSignatureError:
        return {"error":"Token Expired"}
    except Exception as e:
        return {"error":str(e)}
def token_required(func):
    # decorator factory which invoks update_wrapper() method and passes decorated function as an argument
    @wraps(func)
    def decorated(*args, **kwargs):
        try:
            token = request.headers["Authorization"]
            token = token[7:]
            
            if not token:
                return {'Alert!': 'Token is missing!'}, 401
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except KeyError:
            return {"error":"Header Missing"}
        except jwt.ExpiredSignatureError:
            return {"error":"Token Expired !"}
        except Exception as e:
            print(e)
            return {"error":str(e)}
        return func(*args, **kwargs)
    return decorated
    
@app.route("/auth")
@token_required
def auth():
    return {"Heya":"DONE"}


class availCourse(Resource):
    def post(self):
        return avail_course()
    def get(self):
        return avail_course()

@app.route('/')
def home():
    return "Hey ther This is The Api HomePage"
@app.route('/avail_course')
def get():
    return 
class Register(Resource):
    def post(self):
        data = request.get_json()
        print(data)
        username = data['username']
        password = data['password']
        email = data['email']
        return  {"resp":register(username,password,email)}

class Login(Resource):
    def get(self):
        return login(request.args.get("username"),request.args.get("password"))
    def post(self):
        data = request.get_json()
        username = data['username']
        password = data['password']
        temp_login = login(username,password)
        if temp_login=="Logged-in":
            session['logged_in'] = True
            token = genrate_token(username)
            return {"token":str(token)}
        else:
            return temp_login;
class check_users(Resource):
    def post(self):
        return check_student()
    def get(self):
        return check_student()


api.add_resource(Login,'/login')
api.add_resource(Register,'/register')
api.add_resource(availCourse,"/course")
api.add_resource(check_users,"/users")
