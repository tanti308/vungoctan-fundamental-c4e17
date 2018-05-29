from mongoengine import * #StringField, IntField, BooleanField, Document, ListField, ImageField

import mlab

class Service(Document):
    name = StringField()
    yob = IntField()
    gender = IntField()
    height = IntField()
    phone = StringField()
    address = StringField()
    status = BooleanField()
    description = StringField()
    measurements = ListField()
    image = StringField()
    email = StringField()
    company = StringField()
    job = StringField()
