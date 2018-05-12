from mongoengine import * #StringField, IntField, BooleanField, Document


# Design database
    # Create collection
class Customer(Document):
    name = StringField()
    gender = IntField()
    email = StringField()
    phone_number = StringField()
    job = StringField()
    company = StringField()
    contacted = BooleanField()
