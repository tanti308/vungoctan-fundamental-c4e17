from models.service import Service
import mlab

mlab.connect()

all_service = Service.objects(gender=0)   # Lay tat ca cac object trong collection Service, co the filter cac field trong ()

for index, service in enumerate(all_service):
    print(service['name'])
    if index ==9:
        break
