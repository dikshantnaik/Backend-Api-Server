from .db_schem import *

def register(input_name,input_pass,email):
    try:
        s1 = Users(user_name=input_name,password=input_pass,email=email)
        s1.save()
        print("Registerd ",input_name)
        return "Registered"
    except mongoengine.errors.NotUniqueError:
        return {"error":"username Exists"}
    except Exception as e:
        # raise e;
        return {"error":str(e)}
        
def check_student():
    data = {}
    for x in Users.objects:
        data[x.user_name]={'password':x.password,'email':x.email}
    return data
def login(input_user,input_pass):
    resp = ""
    for x in Users.objects:
        if x.user_name==input_user:
            if x.password==input_pass:
                resp=  "Logged-in"
            else:
                resp = "Wrong pass"
                
        else:
            resp = "No user"
    return resp;
def add_aval_course():
    cname = input("Course name ; ")
    cduar = input("Duaration : ")
    cdisr = input("Discription :")
    obj  = AvailCourse(course_name=cname,course_duration=cduar,course_discription=cdisr)
    obj.save()
    print("Added ! ")

def avail_course():
    data = {}
    for course in AvailCourse.objects:
        data[course.cid] = {'course_name':course.course_name,'course_duration':course.course_duration,'course_discription':course.course_discription}
    return data;
def enroled_course():
    stud = input("user :")
    course = input("")

    for x in Users.objects:
        if x.user_name == stud:
            for y in AvailCourse.objects:
                if y.course_name==course:
                    obj = EnroledCourse(Studentid=x,course_id=y)
                    obj.save()
        else:
            print("HEHEHE")
avail_course()