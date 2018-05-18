import mlab
from mongoengine import *

mlab.connect()

class river(Document):
    name = StringField()
    continent = StringField()
    length = IntField()

# Chay 1 trong 2 cai
# Ex8:
af_river = river.objects(continent="Africa")
for i,river in enumerate(af_river):
    print("{0}. {1}, {2}: {3}".format(i+1, river['name'], river['continent'], river['length']))

# Ex9:
# am_river = river.objects(continent="S. America", length__lt=1000)
# for i,river in enumerate(am_river):
#     print("{0}. {1}, {2}: {3}".format(i+1, river['name'], river['continent'], river['length']))
