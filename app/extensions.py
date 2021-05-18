from flask_pymongo import PyMongo

# Setup MongoDB here
# mongo = PyMongo(uri="mongodb://localhost:27017/database")

Mongo = pymongo.MongoClient("mongodb+srv://WebHook:msVkthDBF4a9KGw@mydatabase.9snxp.mongodb.net/WebHook?retryWrites=true&w=majority")

cluster = Mongo['WebHook']
db=cluster['Data']
