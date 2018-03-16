from utils.strings import Strings
from messenger import answer_view_templates
from messenger.user_data import UserData

class GenericsService:

    def __init__(self):
        pass

    def __comoestou(self,message):
        user_id = message.getClientID()
        data = answer_view_templates.text(user_id, Strings.RESPOSTA_COMO_ESTOU)
        MessengerService.sendMessage(data)

    def __apresentacao(self,message):
        user_id = message.getClientID()
        data = answer_view_templates.text(user_id, Strings.APRESENTATION)
        MessengerService.sendMessage(data)

    def __agradecimento(self,message):
        user_id = message.getClientID()
        data = answer_view_templates.text(user_id, Strings.RESPOSTA_AGRADECIMENTO)
        MessengerService.sendMessage(data)

    def __saudacao(self,message):
        user_id = message.getClientID()
        data = answer_view_templates.text(user_id, Strings.RESPOSTA_SAUDACAO.format(UserData().getFirstNameClient(user_id)))
        MessengerService.sendMessage(data)

    options = {Strings.CMD_PERGUNTA_SAUDACAO.upper(): __comoestou,
               Strings.CMD_AGRADECIMENTO.upper(): __agradecimento,
               Strings.CMD_APRESENTACAO.upper(): __apresentacao,
               Strings.CMD_SAUDACAO.upper(): __saudacao}

from messenger.messenger_service import MessengerService
