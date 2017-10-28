from authentication import Authentication
from message import Message
import json
import requests
import os

from strings import Strings
from userData import UserData


class RequestController:

    def __init__(self):
        self.__PARAMS = {"access_token": Authentication.PAGE_ACCESS_TOKEN}
        self.__HEADERS = {"Content-Type": "application/json"}

    def unpackMessage(self,data):
        if data["object"] == "page":
            for entry in data["entry"]:
                for messaging_event in entry["messaging"]:
                    message = Message(messaging_event)
                    user = message.getClientID()

                    if(message.getContentMessage() == Strings.GET_STARTED):
                        msgText = Strings.GREETING_KNOWN_USER.format(UserData().getFirstNameClient())
                        data = self.__getResponse(user, msgText)
                        self.__sendMessage(data)
                        msgText = Strings.APRESENTATION
                        data = self.__getResponse(user, msgText)
                        self.__sendMessage(data)

                    else:
                        msgText = message.getContentMessage()
                        data = self.__getResponse(user,msgText)
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

    # def __getNameUser

    def __sendMessage(self,data):
        r = requests.post("https://graph.facebook.com/v2.6/me/messages", params=self.__PARAMS, headers=self.__HEADERS, data=data)
        if r.status_code != 200:
            print(r.status_code)
            print(r.text)