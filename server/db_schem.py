
from datetime import datetime
from enum import auto, unique

from mongoengine import Document
import mongoengine
from mongoengine.fields import DateField, IntField, ListField, ReferenceField, SequenceField, StringField
# x= mongoengine.connect(host='mongodb+srv://dikshant23:breadjamd23@cluster0.qnc2f.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
x = mongoengine.connect('test3')

class Student(Document):
   
   user_name = StringField(max_length=50,unique=True)
   age = IntField()
   password = StringField(required=True)

class AvailCourse(Document):
    cid= SequenceField()
    course_name = StringField(max_length=100)
    course_duration = StringField(max_length=50)
    course_discription = StringField(max_length=500)
    
class EnroledCourse(Document):
    Studentid = ReferenceField(Student)
    course_id = ReferenceField(AvailCourse)

    course_registration = DateField(default=datetime.today)


