import json

import requests

from config.configuration import Configuration


class UserData:

    def requestUser(self,client_id):
        params = {"fields": "first_name,last_name,profile_pic,locale,timezone,gender",
                  "access_token": Configuration.PAGE_ACCESS_TOKEN}
        return json.loads(requests.get("https://graph.facebook.com/v2.6/"+str(client_id), params=params).text)

    def getFirstNameClient(self,client_id):
        result = self.requestUser(client_id)
        return result["first_name"]

    def getLastNameClient(self,client_id):
        return (self.requestUser(client_id))["last_name"]

    def getUrlProfilePictureClient(self,client_id):
        return (self.requestUser(client_id))["profile_pic"]

    def getGenderClient(self,client_id):
        return (self.requestUser(client_id))["gender"]

    def getNameClient(self,client_id):
        return (self.requestUser(client_id))["first_name"] +" "+ (self.requestUser(client_id))["last_name"]