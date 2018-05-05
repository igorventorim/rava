import json
import redis

class Redis:

    def __init__(self, url):
        self.__r = redis.from_url(url)

    def clearAll(self):
        self.__r.flushall()

    def existsUserOn(self, client):
        return self.__exists(client)

    def delete(self, client):
        self.__r.delete(str(client))

    def __exists(self, key):
        return self.__r.exists(str(key))

    def setKey(self, key, value):
        self.__r.set(str(key), json.dumps(value))

    def getValue(self, key):
        return json.loads(self.__r.get(str(key)))

    def show(self, key):
        return str(self.getValue(key))

    def setExpire(self,key,time):
        self.__r.expire(key,time)


























