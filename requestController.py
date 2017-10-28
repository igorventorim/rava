from authentication import Authentication
from message import Message
import json
import requests
import os
import answerViewTemplates
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
                    user_id = message.getClientID()

                    if(message.getContentMessage() == Strings.GET_STARTED):
                        msgText = Strings.GREETING_KNOWN_USER.format(UserData().getFirstNameClient(user_id))
                        data = answerViewTemplates.text(user_id, msgText)
                        self.__sendMessage(data)
                        msgText = Strings.APRESENTATION
                        data = answerViewTemplates.text(user_id, msgText,["Cadastrar pergunta","Responder Pergunta"])
                        self.__sendMessage(data)

                    else:
                        msgText = message.getContentMessage()
                        data = answerViewTemplates.text(user_id,msgText)
                        self.__sendMessage(data)



    # def __getNameUser

    def __sendMessage(self,data):
        r = requests.post("https://graph.facebook.com/v2.6/me/messages", params=self.__PARAMS, headers=self.__HEADERS, data=data)
        if r.status_code != 200:
            print(r.status_code)
            print(r.text)