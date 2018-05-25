import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds119090.mlab.com:19090/muadongratlanhc4e17

host = "ds119090.mlab.com"
port = 19090
db_name = "muadongratlanhc4e17"
user_name = "admin"
password = "admin"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())
