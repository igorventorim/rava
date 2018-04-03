from bs4 import BeautifulSoup
import requests
import datetime
import re
from config.configuration import Configuration
from ru.domain.cardapio import Cardapio
class SincData():

    def __init__(self):
        self.tipo = None
        pass

    def getType(self,tipo):
        if "almo" in tipo.lower():
            return "Almoço"
        else:
            return "Jantar"

    def run(self):

        _URL = "http://ru.ufes.br/cardapio/"

        now = datetime.datetime.now()
        if(now.hour > 6 and now.hour < 15):
            self.tipo = "Almoço"
            type = 1
        elif(now.hour < 23):
            self.tipo = "Jantar"
            type = 2

        searchURL = _URL + str(now.year) + "-" + str(now.month) + "-" + str(now.day)
        print(searchURL)

        r = requests.get(searchURL)
        soup = BeautifulSoup(r.content, "html5lib")

        itens = soup.find("div", class_='view-display-id-page_1')
        if (itens != None):
            refeicoes = itens.find("div", class_='view-content')
            if (refeicoes != None):

                for refeicao in refeicoes.children:
                    if (refeicao.find("views-field-title") == None):
                        tipo = refeicao.find("div", class_="views-field-title").find("span", class_="field-content")
                        tipo = self.getType(tipo.get_text())

                        if(tipo == self.tipo):
                            cardapio = refeicao.find("div", class_="views-field-body").find_all("div",class_="field-content")
                            menu = tipo + " - Data: "+ str(now.day) + "/" + str(now.month) + "/" + str(now.year) + "\n"
                            for element in cardapio:
                                menu += re.sub(' +',' ',element.get_text())+"\n"

                            check = Cardapio.query.filter_by(data=now.date(),tipo=type).first()

                            if check is None:
                                cardapio = Cardapio()
                                cardapio.set_data(now.date())
                                cardapio.set_texto(menu)
                                cardapio.set_tipo(type)
                                Configuration.db.session.add(cardapio)
                                Configuration.db.session.commit()
                                print("Cardápio atualizado com sucesso!")


                print("Request " + searchURL + " realizado com sucesso!")
            else:
                print("NÃO POSTARAM O CARDAPIO AINDA!!!")