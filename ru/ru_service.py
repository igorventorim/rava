from utils.strings import Strings
from messenger.messenger_service import MessengerService
from messenger import answer_view_templates

class RUService:

    def __init__(self):
        pass

    def visualizar_cardapio(self,message):
        user_id = message.getClientID()
        data = answer_view_templates.text(user_id, Strings.RESPOSTA_CARDAPIO)
        MessengerService.sendMessage(data)

    def visualizar_prato(self,message):
        user_id = message.getClientID()
        data = answer_view_templates.text(user_id, Strings.RESPOSTA_PRATO)
        MessengerService.sendMessage(data)

    options = {Strings.CMD_CARDAPIO: visualizar_cardapio,
               Strings.CMD_PRATO: visualizar_prato}