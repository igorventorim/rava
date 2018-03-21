from utils.strings import Strings
from messenger import answer_view_templates
# from app import db
from ru.domain.person import Person
from ru.domain.cardapio import Cardapio
import datetime
from config.configuration import Configuration

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
            Configuration.db.session.add(person)
            Configuration.db.session.commit()
        data = answer_view_templates.text(user_id, Strings.response_ru[Strings.CMD_SPAM_RU])
        MessengerService.sendMessage(data)

    def unregister_spam_ru(self,message):
        user_id = message.getClientID()
        data = answer_view_templates.text(user_id, Strings.response_ru[Strings.CMD_DELETE_SPAM_RU])
        person = Person.query.filter_by(id=user_id).first()
        if(person != None):
            Configuration.db.session.delete(person)
            Configuration.db.session.commit()
        MessengerService.sendMessage(data)

    def sendMenus(self):
        people = Person.query.all()
        datenow = datetime.datetime.now()
        tipo = 1 if datenow.hour < 15 else 2
        saudacao = "Bom dia! Isso é o que temos para hoje no almoço do RU:\n" if datenow.hour < 13 else "Boa tarde! Isso é o que temos para hoje na janta do RU:\n"
        cardapio = Cardapio.query.filter_by(data=datenow.date(),tipo=tipo).first()
        if(cardapio is None):
            print("Não Encontrei cardapio...")
            return
        for person in people:
            data = answer_view_templates.text(person.get_id(), saudacao + cardapio.get_texto())
            MessengerService.sendMessage(data)

    options = {Strings.CMD_CARDAPIO.upper(): visualizar_cardapio,
               Strings.CMD_PRATO.upper(): visualizar_prato,
               Strings.CMD_SPAM_RU.upper(): register_spam_ru,
               Strings.CMD_DELETE_SPAM_RU.upper(): unregister_spam_ru }

from messenger.messenger_service import MessengerService