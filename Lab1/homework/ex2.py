from pymongo import MongoClient

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(uri)

db = client.get_default_database()

blog = db["posts"]

post = {
    "title": "Đia nhật ký: Tương tư ",
    "author": "Hoàng tử ! đùn",
    "content": '''
        Thôn Đoài ngồi nhớ thôn Đông
    Một người chín nhớ mười mong một người.
    Gió mưa là bệnh của giời
    Tương tư là bệnh của tôi yêu nàng.
    Hai thôn chung lại một làng,
    Cớ sao bên ấy chẳng sang bên này?...
    '''
}
# blog.insert_one(post)
