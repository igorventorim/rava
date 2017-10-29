from authentication import Authentication
from message import Message
import requests
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
                    self.__selector(message)


    def __sendMessage(self,data):
        r = requests.post("https://graph.facebook.com/v2.6/me/messages", params=self.__PARAMS, headers=self.__HEADERS, data=data)
        if r.status_code != 200:
            print(r.status_code)
            print(r.text)


    def __selector(self,message):
        try:
            self.options[message.getContentMessage().upper()](self,message)
        except:
            self.erro(message)

    def started(self,message):
        user_id = message.getClientID()
        msgText = Strings.GREETING_KNOWN_USER.format(UserData().getFirstNameClient(user_id))
        data = answerViewTemplates.text(user_id, msgText)
        self.__sendMessage(data)
        msgText = Strings.APRESENTATION
        data = answerViewTemplates.quick_reply(user_id, msgText, [Strings.PROFESSOR, Strings.ALUNO])
        self.__sendMessage(data)

    def help(self,message):
        user_id = message.getClientID()
        data = answerViewTemplates.text(user_id, Strings.HELP_INFO)
        self.__sendMessage(data)

    def professor(self,message):
        user_id = message.getClientID()
        data = answerViewTemplates.text(user_id, Strings.PROFESSOR_INFO)
        self.__sendMessage(data)

    def aluno(self,message):
        user_id = message.getClientID()
        data = answerViewTemplates.text(user_id, Strings.ALUNO_INFO)
        self.__sendMessage(data)

    def erro(self,message):
        user_id = message.getClientID()
        # msgText = message.getContentMessage()
        data = answerViewTemplates.text(user_id, Strings.APOLOGIZE_USER_FOR_ERROR)
        self.__sendMessage(data)

    options = {Strings.GET_STARTED.upper(): started,
               Strings.HELP.upper(): help,
               Strings.PROFESSOR.upper(): professor,
               Strings.ALUNO.upper(): aluno
               }