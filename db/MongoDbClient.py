import pymongo


class MongoDbClient:
    ROUTER_STRING = "mongodb+srv://test:test@cluster0.lzghrso.mongodb.net/?retryWrites=true&w=majority"
    DATABASE = None

    @staticmethod
    def init_db():
        client = pymongo.MongoClient(MongoDbClient.ROUTER_STRING)
        MongoDbClient.DATABASE = client['log_db']
        print("connect successfull")

    @staticmethod
    def insert_one(collection, data):
        MongoDbClient.DATABASE[collection].insert_one(data)
        print("Inserted")

MongoDbClient.init_db()
MongoDbClient.insert_one('log_tb',{'name':'frahan'})

