from mongoengine import *

class User(Document):
    name = StringField()
    email = StringField()
    account = StringField()
    password = StringField()
