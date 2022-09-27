from json import JSONEncoder

class AccessLog:
    def __init__(self, authority,timestamp,method,path,schema,status_code,content_length,response_time,origin,user_agent):
        self.authority = authority
        self.timestamp = timestamp
        self.method = method
        self.path = path
        self.schema = schema
        self.status_code = status_code
        self.content_length = content_length
        self.response_time = response_time
        self.origin = origin
        self.user_agent = user_agent




# obj['authority'] = txt[0]
# obj['timestamp'] = txt[3] + ' ' + txt[4]
# obj['method'] = txt[5]
# obj['path'] = txt[6]
# obj['schema'] = txt[7]
# obj['status_code'] = txt[8]
# obj['content_length'] = txt[9]
# obj['response_time'] = txt[10]
# obj['origin'] = txt[11]
# obj['user_agent'] = ''.join(txt[13:len(txt) - 1])

class AccessLogEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
