from utils.strings import Strings
from messenger import answer_view_templates
from app import db
from ru.domain.person import Person

class RUService:

    def __init__(self):
        pass

    def visualizar_cardapio(self,message):
        user_id = message.getClientID()
        data = answer_view_templates.text(user_id, Strings.response_ru[Strings.CMD_CARDAPIO])
        MessengerService.sendMessage(data)

    def visualizar_prato(self,message):
        user_id = message.getClientID()
        data = answer_view_templates.text(user_id, Strings.response_ru[Strings.CMD_PRATO])
        MessengerService.sendMessage(data)

    def register_spam_ru(self,message):
        user_id = message.getClientID()
        person = Person(user_id)
        check = Person.query.filter_by(id=user_id).first()
        if(check is None):
            db.session.add(person)
            db.session.commit()
        data = answer_view_templates.text(user_id, Strings.response_ru[Strings.CMD_SPAM_RU])
        MessengerService.sendMessage(data)

    def unregister_spam_ru(self,message):
        user_id = message.getClientID()
        data = answer_view_templates.text(user_id, Strings.response_ru[Strings.CMD_DELETE_SPAM_RU])
        person = Person.query.filter_by(id=user_id).first()
        if(person != None):
            db.session.delete(person)
            db.session.commit()
        MessengerService.sendMessage(data)


    options = {Strings.CMD_CARDAPIO.upper(): visualizar_cardapio,
               Strings.CMD_PRATO.upper(): visualizar_prato,
               Strings.CMD_SPAM_RU.upper(): register_spam_ru,
               Strings.CMD_DELETE_SPAM_RU.upper(): unregister_spam_ru}

from messenger.messenger_service import MessengerService