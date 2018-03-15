from utils.strings import Strings
from messenger.messenger_service import MessengerService
from messenger import answer_view_templates

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

    options = {Strings.CMD_PERGUNTA_SAUDACAO: __comoestou,
               Strings.CMD_AGRADECIMENTO: __agradecimento,
               Strings.CMD_APRESENTACAO: __apresentacao}
