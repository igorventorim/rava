from utils.strings import Strings
from messenger.message import Message
from config.configuration import Configuration
from messenger import answer_view_templates
from wit import Wit
from messenger.domain.usuario import Usuario
import json
from messenger.domain.log import Log
from datetime import datetime
from messenger.user_data import UserData
import requests

class MessengerService:

    def __init__(self):
        self.__options = {}
        self.service_virtual_class = VirtualClassService()
        self.service_atribuna = AtribunaService()
        self.service_ru = RUService()
        self.service_generics = GenericsService()
        self.service_cine = CineService()
        self.client = Wit(Configuration.WIT_TOKEN)
        self.__options.update(self.service_virtual_class.options)
        self.__options.update(self.service_atribuna.options)
        self.__options.update(self.service_ru.options)
        self.__options.update(self.service_generics.options)
        self.__options.update(self.service_cine.options)

    def unpackMessage(self,data):
        if data["object"] == "page":
            for entry in data["entry"]:
                for messaging_event in entry["messaging"]:
                    message = Message(messaging_event)
                    check = Usuario.query.filter_by(code=message.getClientID()).first()
                    if check is None:
                        user = Usuario()
                        user.set_code(message.getClientID())
                        user.set_nome(UserData().getFirstNameClient(message.getClientID()))
                        Configuration.db.session.add(user)
                        Configuration.db.session.commit()
                    self.__selector(message)


    @staticmethod
    def sendMessage(message,data):
        PARAMS = {"access_token": Configuration.PAGE_ACCESS_TOKEN}
        HEADERS = {"Content-Type": "application/json"}
        r = requests.post("https://graph.facebook.com/v2.6/me/messages", params=PARAMS, headers=HEADERS, data=data)
        if r.status_code != 200:
            print(r.status_code)
            print(r.text)
        else:
            MessengerService.saveLog(message,data)

    def sendMessageTest(self,message):
        data = answer_view_templates.text(1807409562632930, message)
        MessengerService.sendMessage(message,data)

    def __selector(self,message):
        # try:
            result = self.client.message(message.getContentMessage())
            cmd = self.__handleResponseWit(result,message)
            self.__options[cmd.upper()](self.selectModule(cmd.upper()),message)
        # except:
        #     self.__erro(message)

    def __erro(self, message):
        user_id = message.getClientID()
        data = answer_view_templates.text(user_id, Strings.APOLOGIZE_USER_FOR_ERROR)
        MessengerService.sendMessage(message,data)

    def __handleResponseWit(self,response,message):
        entidades = response['entities']
        if entidades == {}:
            return ""
        else:
            max = 0
            chave = ""
            message.setEntities(entidades)
            for key, value in entidades.items():
               if key == 'datetime' or key == 'keywords': #TODO: COLOCAR PARA CONFERIR NA LISTA DE ENTIDADES AUXILIARES
                continue
               elif value[0]['confidence'] > max and value[0]['confidence'] > 0.55:
                   max = value[0]['confidence']
                   chave = key
            message.setIntent(entidades[chave][0]['value'])
            return entidades[chave][0]['value']

    def selectModule(self, element):
        if element in self.service_virtual_class.options:
            return self.service_virtual_class
        elif element in self.service_ru.options:
            return self.service_ru
        elif element in self.service_atribuna.options:
            return self.service_atribuna
        elif element in self.service_generics.options:
            return self.service_generics
        elif element in self.service_cine.options:
            return self.service_cine
        else:
            return None

    @staticmethod
    def saveLog(message,data):
        if message != None:
            items = json.loads(data)
            code = items['recipient']['id']
            user = Usuario.query.filter_by(code=code).first()
            response = items['message']['text']
            if(code != None):
                log = Log()
                log.set_entities(message.getEntities())
                log.set_usuario_id(user.get_id())
                log.set_response(response)
                log.set_message(message.getContentMessage())
                log.set_intent(message.getIntent())
                log.set_data(datetime.now())
                Configuration.db.session.add(log)
                Configuration.db.session.commit()
            else:
                print("Não foi possível encontrar o usuário na base de dados.")

from virtual_class.virtual_class_service import VirtualClassService
from ru.ru_service import RUService
from atribuna.atribuna_service import AtribunaService
from messenger.generics_service import GenericsService
from cine.cine_service import CineService