from utils.strings import Strings
from messenger.message import Message
from config.authentication import Authentication
from messenger import answer_view_templates
from virtual_class.virtual_class_service import VirtualClassService
from ru.ru_service import RUService
from atribuna.atribuna_service import AtribunaService
from wit import Wit
import requests

class MessengerService:

    def __init__(self):
        self.__options = {}
        service_virtual_class = VirtualClassService()
        service_atribuna = AtribunaService()
        service_ru = RUService()
        self.client = Wit(Authentication.WIT_TOKEN)
        self.__options.update(service_virtual_class.options)
        self.__options.update(service_atribuna.options)
        self.__options.update(service_ru.options)

    def unpackMessage(self,data):
        if data["object"] == "page":
            for entry in data["entry"]:
                for messaging_event in entry["messaging"]:
                    message = Message(messaging_event)
                    self.__selector(message)


    @staticmethod
    def sendMessage(data):
        PARAMS = {"access_token": Authentication.PAGE_ACCESS_TOKEN}
        HEADERS = {"Content-Type": "application/json"}
        r = requests.post("https://graph.facebook.com/v2.6/me/messages", params=PARAMS, headers=HEADERS, data=data)
        if r.status_code != 200:
            print(r.status_code)
            print(r.text)

    def sendMessageTest(self,message):
        data = answer_view_templates.text(1807409562632930, message)
        MessengerService.sendMessage(data)

    def __selector(self,message):
        try:
            # cmd = message.getContentMessage().split(' ', 1)[0]
            result = self.client.message(message.getContentMessage())
            cmd = self.__handleResponseWit(result)
            print("AQUI:"+cmd)
            self.__options[cmd.upper()](self,message)
        except:
            self.__erro(message)

    def __erro(self, message):
        user_id = message.getClientID()
        data = answer_view_templates.text(user_id, Strings.APOLOGIZE_USER_FOR_ERROR)
        MessengerService.sendMessage(data)

    def __handleResponseWit(self,response):
        entidades = response['entities']
        if entidades == {}:
            return ""
        else:
            max = 0
            chave = ""
            for key, value in entidades.items():
               if value[0]['confidence'] > max:
                   max = value[0]['confidence']
                   chave = key
            return entidades[chave][0]['value']


