from mongoengine import *


class User(document):
    fullname = StringField()
    email = StringField()
    username = StringField()
    password = StringField()
