from utils.strings import Strings
from messenger import answer_view_templates
from messenger.user_data import UserData

class GenericsService:

    def __init__(self):
        pass

    def __comoestou(self,message):
        user_id = message.getClientID()
        data = answer_view_templates.text(user_id, Strings.response_general[Strings.CMD_PERGUNTA_SAUDACAO])
        MessengerService.sendMessage(message,data)

    def __apresentacao(self,message):
        user_id = message.getClientID()
        data = answer_view_templates.text(user_id, Strings.response_general[Strings.CMD_APRESENTACAO])
        MessengerService.sendMessage(message,data)

    def __agradecimento(self,message):
        user_id = message.getClientID()
        data = answer_view_templates.text(user_id, Strings.response_general[Strings.CMD_AGRADECIMENTO])
        MessengerService.sendMessage(message,data)

    def __saudacao(self,message):
        user_id = message.getClientID()
        data = answer_view_templates.text(user_id, Strings.response_general[Strings.CMD_SAUDACAO].format(UserData().getFirstNameClient(user_id)))
        MessengerService.sendMessage(message,data)

    def __despedida(self,message):
        user_id = message.getClientID()
        data = answer_view_templates.text(user_id, Strings.response_general[Strings.CMD_DESPEDIDA])
        MessengerService.sendMessage(message,data)

    def __idade(self,message):
        user_id = message.getClientID()
        data = answer_view_templates.text(user_id, Strings.response_general[Strings.CMD_IDADE])
        MessengerService.sendMessage(message,data)

    options = {Strings.CMD_PERGUNTA_SAUDACAO.upper(): __comoestou,
               Strings.CMD_AGRADECIMENTO.upper(): __agradecimento,
               Strings.CMD_APRESENTACAO.upper(): __apresentacao,
               Strings.CMD_SAUDACAO.upper(): __saudacao,
               Strings.CMD_DESPEDIDA.upper(): __despedida,
               Strings.CMD_IDADE.upper(): __idade}

from messenger.messenger_service import MessengerService
