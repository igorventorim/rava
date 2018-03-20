import threading
import time
from bs4 import BeautifulSoup
import requests
import datetime
import re
from ru.domain.cardapio import Cardapio
from app import db


class SincData(object):

    def __init__(self, interval=60,tipo="almoco"):

        self.interval = interval
        self.tipo = tipo

        thread = threading.Thread(target=self.run, args=())
        # thread.daemon = True                            # Daemonize thread
        thread.start()                                  # Start the execution

    def getType(self,tipo):
        if "almo" in tipo.lower():
            return "Almoço"
        else:
            return "Jantar"

    def run(self):

        _URL = "http://ru.ufes.br/cardapio/"
        while True:

            now = datetime.datetime.now()
            if(now.hour > 6 and now.hour < 15):
                self.tipo = "Almoço"
                tipo = 1
            elif(now.hour > 15 and now.hour < 23):
                self.tipo = "Jantar"
                tipo = 2

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
                                menu = tipo  + "- Data: "+ str(now.day) + "/" + str(now.year) + "/" + str(now.month) + "\n"
                                for element in cardapio:
                                    menu += re.sub(' +',' ',element.get_text())+"\n"

                                check = Cardapio.query.filter_by(data=now.date(),tipo=tipo).first()

                                if check is None:
                                    cardapio = Cardapio()
                                    cardapio.set_data(now.date())
                                    cardapio.set_texto(menu)
                                    cardapio.set_tipo(tipo)
                                    db.session.add(cardapio)
                                    db.session.commit()

                                print(menu)

                    print("Request " + searchURL + " realizado com sucesso!")
                else:
                    print("NÃO POSTARAM O CARDAPIO AINDA!!!")

            print('Rodando em background')

            time.sleep(self.interval)