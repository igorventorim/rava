from utils.strings import Strings
from messenger import answer_view_templates
# from app import db
from ru.domain.person import Person
from ru.domain.cardapio import Cardapio
import datetime
from config.configuration import Configuration
import requests

class RUService:

    def __init__(self):
        pass

    def visualizar_cardapio(self,message):
        user_id = message.getClientID()
        if 'datetime' in message.getEntities():
            datenow = datetime.datetime.strptime(message.getEntities()['datetime'][0]['value'][:10],"%Y-%m-%d")
            msg = "Este foi o cardápio do dia...\n"
        else:
            datenow = datetime.datetime.now()
            msg = "O que temos para hoje é ...\n"
        tipo = 1 if datenow.hour < 15 else 2
        cardapio = Cardapio.query.filter_by(data=datenow.date(), tipo=tipo).first()

        if (cardapio is None):
            print("Cardapio não encontrado para o dia...")
            msg = "Desculpe, ainda não consegui encontrar cardápio para este dia :("
        else:
            msg = msg + cardapio.get_texto()
        data = answer_view_templates.text(user_id, msg)
        MessengerService.sendMessage(message,data)

    def visualizar_prato(self,message):
        user_id = message.getClientID()
        data = answer_view_templates.text(user_id, Strings.response_ru[Strings.CMD_PRATO])
        MessengerService.sendMessage(message,data)

    def register_spam_ru(self,message):
        user_id = message.getClientID()
        person = Person(user_id)
        check = Person.query.filter_by(id=user_id).first()
        if(check is None):
            Configuration.db.session.add(person)
            Configuration.db.session.commit()
            data = answer_view_templates.text(user_id, Strings.response_ru[Strings.CMD_SPAM_RU])
        else:
            data = answer_view_templates.text(user_id, Strings.CMD_SPAM_RU_REGISTERED)
        MessengerService.sendMessage(message,data)

    def unregister_spam_ru(self,message):
        user_id = message.getClientID()
        data = answer_view_templates.text(user_id, Strings.response_ru[Strings.CMD_DELETE_SPAM_RU])
        person = Person.query.filter_by(id=user_id).first()
        if(person != None):
            Configuration.db.session.delete(person)
            Configuration.db.session.commit()
        MessengerService.sendMessage(message,data)

    def sendMenus(self):
        people = Person.query.all()
        datenow = datetime.datetime.now()
        tipo = 1 if datenow.hour < 15 else 2
        saudacao = "Bom dia! Isso é o que temos para hoje no almoço do RU:\n" if datenow.hour < 13 else "Boa tarde! Isso é o que temos para hoje na janta do RU:\n"
        cardapio = Cardapio.query.filter_by(data=datenow.date(),tipo=tipo).first()
        if(cardapio is None):
            print("Cardapio não encontrado para hoje...")
            return
        for person in people:
            data = answer_view_templates.textPublish(person.get_id(), saudacao + cardapio.get_texto())
            MessengerService.sendMessage(None,data)

    def cost(self,message):
        user_id = message.getClientID()
        data = answer_view_templates.text(user_id, Strings.response_ru[Strings.CMD_PRICE])
        MessengerService.sendMessage(message,data)

    def get_search_keyword_ru(self,texto):
        _url = Configuration.URL_API_NLP+"extractSKru"
        _data = {'texto':texto}
        _credentials = (Configuration.USER_API_NLP,Configuration.PASSWORD_API_NLP)
        result = requests.post(url=_url,auth=_credentials,data=_data)
        return result

    def hadThis(self,message):
        result = self.get_search_keyword_ru(message.getContentMessage())
        print(result.text)

    def get_frequency_menu(self,message):
        pass

    options = {Strings.CMD_CARDAPIO.upper(): visualizar_cardapio,
               Strings.CMD_PRATO.upper(): visualizar_prato,
               Strings.CMD_SPAM_RU.upper(): register_spam_ru,
               Strings.CMD_DELETE_SPAM_RU.upper(): unregister_spam_ru,
               Strings.CMD_PRICE.upper(): cost,
               Strings.CMD_SELECAO.upper(): hadThis,
               Strings.CMD_FREQUENCIA.upper(): get_frequency_menu}

from messenger.messenger_service import MessengerService