import os
from db.MongoDbClient import MongoDbClient



class LogHandler:
    def __init__(self,file_paths,delimiter):
        self.file_paths=file_paths
        self.delimiter=delimiter

    def splitTheLine(self,line):
        obj = {}
        txt = line.replace('"', '').split()
        obj['authority'] = txt[0]
        obj['timestamp'] = txt[3] + ' ' + txt[4]
        obj['method'] = txt[5]
        obj['path'] = txt[6]
        obj['schema'] = txt[7]
        obj['status_code'] = txt[8]
        obj['content_length'] = txt[9]
        obj['response_time'] = txt[10]
        obj['origin'] = txt[11]
        obj['user_agent'] = ''.join(txt[13:len(txt) - 1])
        return obj



        
    def read_log_file(self,file_path):
        # MongoDbClient.init_db()
        with open(file_path,'r') as f:
            for line in f:
                # print(obj)
                MongoDbClient.insert_one('log_tb',self.splitTheLine(line))
        print("Done")





    def isfileOrDir(self):
        if os.path.isfile(self.file_paths) and self.file_paths.endswith(".log"):
            self.read_log_file(self.file_paths)
        elif os.path.isdir(self.file_paths):
            os.chdir(self.file_paths)
            for file in os.listdir():
                if file.endswith(".log"):
                    self.read_log_file(file)







