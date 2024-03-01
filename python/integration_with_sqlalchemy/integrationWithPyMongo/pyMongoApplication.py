import  pymongo as pyM
import datetime
import pprint

client = pyM.MongoClient("mongodb+srv://maxwellchaves1844:3wqjjSGespZC2QN6@cluster0.lwevttd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = client.test

collection = db.test_collection
print(db.test_collection)

# definição de informação para compor o documento
post = {
    "author": "Mike",
    "text": "My first mongodb application based on python",
    "tags": ["mongodb", "python3", "pymongo"],
    "date": datetime.datetime.utcnow()
}

# preparando para submeter as informações
posts = db.posts
post_id = posts.insert_one(post).inserted_id
print(post_id)

# print(db.posts.find_one())
pprint.pprint(db.posts.find_one())

# bulk inserts
new_posts = [{
        "author": "Mike",
        "text": "Another post",
        "tags": ["bulk", "post", "insert"],
        "date": datetime.datetime.utcnow()
    },
    {
        "author": "João",
        "text": "Post from João. New post available",
        "title": "Mongo is fun",
        "date": datetime.datetime(2009, 11, 10, 10, 45)
    }]

result = posts.insert_many(new_posts)
print(result.inserted_ids)
print('\nRecuperação Final')
pprint.pprint(db.posts.find_one({"author":"João"}))