from db.MongoDbClient import MongoDbClient
from log_handler.LogHandler import LogHandler
from celery_stuff.celeryTask import process_task



if __name__== '__main__':
    MongoDbClient.init_db()
    # process_task.delay('C:/Users/aristo/Desktop/testbench/logs')
    LogHandler('C:/Users/aristo/Desktop/testbench/logs').isfileOrDir()





