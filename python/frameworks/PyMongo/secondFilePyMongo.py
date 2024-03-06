import  pymongo as pyM
import datetime
import pprint

client = pyM.MongoClient("mongodb+srv://pymongo:pymongo@cluster0.lwevttd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = client.test

posts = db.posts

print('\n Documentos presentes na coleção posts')
for post in posts.find():
    pprint.pprint(post)

print('\nQuantidade de documentos')
print(posts.count_documents({}))

print('\nBusca específica por author')
print(posts.count_documents({'author':'Mike'}))

print('\nBusca específica por tags')
print(posts.count_documents({'tags':'mongodb'}))

pprint.pprint(posts.find_one({'tags':'insert'}))

print('\nRecuperando informaçõs da coleção post de maneira ordenada')
for post in posts.find({}).sort('date'):
    pprint.pprint(post)

result = db.profiles.create_index([('author', pyM.ASCENDING)], unique=True)

print(sorted(list(db.profiles.index_information())))

user_profile_user = [
    {'user_id': 211, 'name': 'Luke'},
    {'user_id': 212, 'name': 'João'}
]

result = db.profiles_user.insert_many(user_profile_user)

print('\nColeções armazenadas no mongoDB')



for collection in db.list_collection_names():
    print(collection)
    # db[collection].drop()
client.drop_database('test')
print(posts.delete_one({"author":"Mike"}))