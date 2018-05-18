import mlab
from mongoengine import *

mlab.connect()

class river(Document):
    name = StringField()
    continent = StringField()
    length = IntField()

all_river = river.objects(continent="Africa")
for i,river in enumerate(all_river):
    print("{0}. {1}, {2}: {3}".format(i+1, river['name'], river['continent'], river['length']))
