from sklearn.metrics.pairwise import pairwise_distances
from sklearn.feature_extraction.text import CountVectorizer
from utils.strings import Strings
from messenger import answer_view_templates
# from app import db
from ru.domain.person import Person
from ru.domain.cardapio import Cardapio
import datetime
from config.configuration import Configuration
import requests
import re
import nltk

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

        if 'keywords' in message.getEntities():
            if message.getEntities()['keywords'][0]['value'] == "janta":
                tipo = 2
            elif message.getEntities()['keywords'][0]['value'] == "almoco":
                tipo = 1

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
        return self.__std_words__(result.text)

    def hadThis(self,message):
        user_id = message.getClientID()
        query = self.get_search_keyword_ru(message.getContentMessage())

        if query != '':

            cardapios = None
            if 'datetime' in message.getEntities():
                datenow = datetime.datetime.strptime(message.getEntities()['datetime'][0]['value'][:10], "%Y-%m-%d")
                type = message.getEntities()['datetime'][0]['grain']
                if type == "day":
                    cardapios = Cardapio.query.filter_by(data=datenow.date())
                elif type == "week":
                    cardapios = Cardapio.query.filter(Cardapio.data.between(datenow.date(),datenow.date()+datetime.timedelta(days=7)))
                elif type == "month":
                    cardapios = Cardapio.query.filter(Cardapio.data.between(datenow.date(),datenow.date()+datetime.timedelta(days=30)))
                elif type == "year":
                    cardapios = Cardapio.query.filter(Cardapio.data.between(datenow.date(),datenow.date()+datetime.timedelta(days=365)))
            if cardapios == None:
                cardapios = Cardapio.query.all()

            items = []
            for cardapio in cardapios:
                if cardapio.get_prato() != None:
                    elements = cardapio.get_prato().split("/ ")
                    for element in elements:
                        element = self.__std_words__(element.lower())
                        items.append(element)
            if(items != []):
                near = self.vectorize(query, items)
            else:
                near = []

            if (len(near) > 0):
                msg = Strings.YES
            else:
                if datenow.date() > datenow.now().date():
                    msg = "Não sei"
                else:
                    msg = Strings.NO
        else:
            msg = "Desculpe, não consegui extrair todas as informações, poderia falar de outra forma?"
        data = answer_view_templates.text(user_id, msg)
        MessengerService.sendMessage(message, data)

    def get_frequency_menu(self,message):
        user_id = message.getClientID()
        query = self.get_search_keyword_ru(message.getContentMessage())

        if query != '':
            cardapios = Cardapio.query.all()
            items = []
            for cardapio in cardapios:
                if cardapio.get_prato() != None:
                    elements = cardapio.get_prato().split("/ ")
                    for element in elements:
                        element = self.__std_words__(element.lower())
                        items.append(element)
            if items != []:
                near = self.vectorize(query,items)
            else:
                near = []
            qtd = len(items)

            if len(near) == 0:
                msg = "Isso nunca teve no restaurante universitário, mas calma, talvez eu não tenha conseguido entender."
            elif len(near) <= (qtd * 0.01):
                msg = "Raramente tem isso."
            elif len(near) <= (qtd * 0.05):
                msg = "Isso é algo comum de se ter por aqui."
            elif len(near) <= (qtd * 0.1):
                msg = "Tem várias vezes."
            elif len(near) > 4 * (qtd * 0.2):
                msg = "Podemos dizer que tem isso todos os dias."
        else:
            msg = "Desculpe, não consegui extrair todas as informações, poderia falar de outra forma?"
        data = answer_view_templates.text(user_id, msg)
        MessengerService.sendMessage(message, data)

    def vectorize(self,query,items):
        vectorizer = CountVectorizer(analyzer="char_wb", ngram_range=(4, 8))
        vcnt = vectorizer.fit_transform([d for d in items])

        features = vectorizer.get_feature_names()
        vectorizer = CountVectorizer(analyzer="char_wb", ngram_range=(4, 8), vocabulary=features)
        query_vcnt = vectorizer.fit_transform([query])
        near = [items[idx] for idx, dist in
                sorted([(ids, pairwise_distances(query_vcnt, s, metric="cosine")[0][0]) for ids, s in enumerate(vcnt)],
                       key=lambda x: x[1]) if dist < 0.4]
        return near

    def __std_words__(self,string, blacklist=['maruipe', 'goiabeiras']):
        tokenizer = re.compile('\w+')
        tkn = tokenizer.findall(string)
        blacklist = blacklist + nltk.corpus.stopwords.words("portuguese")
        return " ".join([t for t in tkn if t not in blacklist])

    options = {Strings.CMD_CARDAPIO.upper(): visualizar_cardapio,
               Strings.CMD_PRATO.upper(): visualizar_prato,
               Strings.CMD_SPAM_RU.upper(): register_spam_ru,
               Strings.CMD_DELETE_SPAM_RU.upper(): unregister_spam_ru,
               Strings.CMD_PRICE.upper(): cost,
               Strings.CMD_SELECAO.upper(): hadThis,
               Strings.CMD_FREQUENCIA.upper(): get_frequency_menu}

from messenger.messenger_service import MessengerService