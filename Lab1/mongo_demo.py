from pymongo import MongoClient

#1. Connect Database server
uri = "mongodb://admin:admin@ds155299.mlab.com:55299/c4e17_tanti308_1"      #thay <username> <password> = ten tk mk cua user database
client = MongoClient(uri)               #Thiet lap ket noi thong qua database

#2. Get default Database
db = client.get_default_database()

#3. Get blog collection
blog = db["blog"]

#4. Write a new blog (gia lap 1 trang chua blog)
post = {
    'title': "Hôm nay trời râm, không mưa không nắng",
    'content': "Tôi bâng khuâng qweytey",
}
# blog.insert_one(post)         #chay lan nua thi se insert them 1 cai blog moi

#lay tat ca cac post
all_posts = blog.find()
for post in all_posts:
    print(post, sep="")
