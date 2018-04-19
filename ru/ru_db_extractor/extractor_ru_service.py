#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from utils.my_encoder import MyEncoder
# from ru.ru_db_extractor.cardapio import Cardapio
from ru.domain.cardapio import Cardapio
import requests
from bs4 import BeautifulSoup
import os
import json
from os import listdir
from os.path import isfile, join
from unicodedata import normalize
import re
from config.configuration import Configuration
import datetime

class ExtractorRUService:

    def __init__(self):
        self.tipo = None
        self.__URL = "http://ru.ufes.br/cardapio/"
        self.pp = {}

    def getType(self,tipo):
        if "almo" in tipo.lower():
            return "Almoço"
        else:
            return "Jantar"

    def menu(self):

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

    def createMenuFiles(self):
        #SET YEAR,MONTH and DAY
        for i in range(2015,2019):
            for j in range(4,5):

                if(j == 2):
                    limitMonth = 29
                elif (j % 2 == 0):
                    limitMonth = 31
                else:
                    limitMonth = 32


                for k in range(1,limitMonth):
                    if(j < 10):
                        month = "0"+str(j)
                    else:
                        month = str(j)
                    if(k < 10):
                        day = "0"+str(k)
                    else:
                        day = str(k)

                    searchURL = self.__URL + str(i) + "-" + month + "-" + day
                    print(searchURL)
                    date = day+"-"+month+"-"+str(i)
                    r = requests.get(searchURL)
                    soup = BeautifulSoup(r.content, "html5lib")

                    itens = soup.find("div", class_='view-display-id-page_1')
                    if(itens != None):
                        refeicoes = itens.find("div", class_='view-content')
                        if(refeicoes != None):
                            for refeicao in refeicoes.children:
                                cardapioDoDia = Cardapio()
                                if (refeicao.find("views-field-title") == None):
                                    tipo = refeicao.find("div", class_="views-field-title").find("span", class_="field-content")
                                    tipo = self.getType(tipo.get_text())
                                    file = open(os.path.join("ru/ru_db_extractor/files",date+"_"+tipo + ".txt"), "w")
                                    # print(tipo.get_text())
                                    cardapio = refeicao.find("div", class_="views-field-body").find_all("div", class_="field-content")

                                    for item in cardapio:
                                        file.write(item.get_text().strip())
                            print("Request " + searchURL + " realizado com sucesso!")

    def remover_acentos(self,txt):
       return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')

    def readFile(self,filename):
        fp = open(filename,"r")
        menu = fp.readlines()
        clean_menu = []
        for i in range(0,len(menu)):
            menu[i] = menu[i].replace('\xa0','')
            if menu[i] != '\n' and menu[i] != '\t\n':
                clean_menu.append(menu[i])
        return clean_menu

    def buildObjectByFile(self,filename):
        cardapio = Cardapio()
        menu = self.readFile(filename)
        tipo = 1 if self.getType(filename) == "Almoço" else 2
        cardapio.set_tipo(tipo)

        cardapio.set_data(datetime.datetime.strptime(filename[25:35],'%d-%m-%Y'))

        for i in range(0, len(menu)):
            if "salada\n" in menu[i].lower():
                saladas = menu[i+1].replace('\t', '')
                cardapio.set_salada(self.remover_acentos(saladas))
            elif "prato" in menu[i].lower() or "sopa/" in menu[i].lower():
                pratos = menu[i + 1].replace('\n', '').replace('\t', '')
                cardapio.set_prato(self.remover_acentos(pratos))
                self.getPrato(pratos)
            elif "opção" in menu[i].lower():
                opt = menu[i + 1].replace('\n', '')
                cardapio.set_opcao(self.remover_acentos(opt))
            elif "guarnição" in menu[i].lower():
                guarnicoes = menu[i + 1].replace('\n', '')
                cardapio.set_guarnicao(self.remover_acentos(guarnicoes))
            elif "sobremesa" in menu[i].lower():
                sobremesa = menu[i + 1].replace('\n', '')
                cardapio.set_sobremesa(self.remover_acentos(sobremesa))
            elif "suco" in menu[i].lower():
                suco = menu[i].replace('\n', '').replace('\t', '')
                cardapio.set_suco(self.remover_acentos(suco))
            elif "acompanhamento" in menu[i].lower():
                acompanhamento = menu[i+1].replace('\n', '').replace('\t', '')
                cardapio.set_acompanhamento(acompanhamento)

        return cardapio

    def buildObjectByText(self,menu,tipo,data):
        cardapio = Cardapio()
        cardapio.set_tipo(tipo)
        cardapio.set_data(datetime.datetime.strptime(data,'%d-%m-%Y'))

        for i in range(0, len(menu)):
            if "salada\n" in menu[i].lower():
                saladas = menu[i + 1].replace('\t', '')
                cardapio.set_salada(self.remover_acentos(saladas))
            elif "prato" in menu[i].lower() or "sopa/" in menu[i].lower():
                pratos = menu[i + 1].replace('\n', '').replace('\t', '')
                cardapio.set_prato(self.remover_acentos(pratos))
                self.getPrato(pratos)
            elif "opção" in menu[i].lower():
                opt = menu[i + 1].replace('\n', '')
                cardapio.set_opcao(self.remover_acentos(opt))
            elif "guarnição" in menu[i].lower():
                guarnicoes = menu[i + 1].replace('\n', '')
                cardapio.set_guarnicao(self.remover_acentos(guarnicoes))
            elif "sobremesa" in menu[i].lower():
                sobremesa = menu[i + 1].replace('\n', '')
                cardapio.set_sobremesa(self.remover_acentos(sobremesa))
            elif "suco" in menu[i].lower():
                suco = menu[i].replace('\n', '').replace('\t', '')
                cardapio.set_suco(self.remover_acentos(suco))

            elif "acompanhamento" in menu[i].lower():
                acompanhamento = menu[i + 1].replace('\n', '').replace('\t', '')
                cardapio.set_acompanhamento(acompanhamento)

        print(cardapio)
        return cardapio



    def getPrato(self, pratos):

        it = pratos.split("/")

        for p in it:
            # print(p)
            if(p[0] == " "):
                word = p[1:-1].lower()
            elif(p[-1] == " "):
                word = p[0:-2].lower()
            else:
                word = p.lower()

            if word not in self.pp:
                self.pp[word] = 0

            self.pp[word] += 1



    def printDict(self):
        count = 0
        for key,value in self.pp.items():
            count += 1
            print(str(count)+ ";"+key+";"+str(value))


    def generateJson(self):
        file = open("db.json","w")
        databaseRU = []
        onlyfiles = [f for f in os.listdir("ru/ru_db_extractor/files") if isfile(join("ru/ru_db_extractor/files", f))]
        for filename in onlyfiles:
            cardapio = self.buildObjectByFile(os.path.join("ru/ru_db_extractor/files", filename))
            print(cardapio)
            # databaseRU.append(cardapio)
        # print(json.dumps(databaseRU,cls=MyEncoder))
        # file.write('{\"cardapio\":'+json.dumps(databaseRU,cls=MyEncoder)+'}')


    # obj = buildObject(os.path.join("files", "01-02-2016_almoco.txt"))
    # print(json.dumps(obj.__dict__))



# generateJson()
# printDict()
# createMenuFiles()