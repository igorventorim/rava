from message import Message
import json
import requests
import os


class RequestController:

    def __init__(self):
        __PARAMS = {"access_token": os.environ["PAGE_ACCESS_TOKEN"]}
        __HEADERS = {"Content-Type": "application/json"}

    def unpackMessage(self,data):
        if data["object"] == "page":
            for entry in data["entry"]:
                for messaging_event in entry["messaging"]:
                    message = Message(messaging_event)
                    user = message.getClientID()

                    data = self.__getResponse(user,message.getContentMessage())
                    self.__sendMessage(data)


    def __getResponse(self,client_id, text):
        return json.dumps({
            "recipient": {
                "id": client_id
            },
            "message": {
                "text": text
            }
        })

    def __sendMessage(self,data):
        r = requests.post("https://graph.facebook.com/v2.6/me/messages", params=self.__PARAMS, headers=self.__HEADERS, data=data)
        if r.status_code != 200:
            print(r.status_code)
            print(r.text)