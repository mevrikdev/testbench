from db.MongoDbClient import MongoDbClient
from log_handler import LogHandler



if __name__== '__main__':
    MongoDbClient.init_db()
    LogHandler.LogHandler('C:/Users/aristo/Desktop/task', '').isfileOrDir()
