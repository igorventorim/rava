#!/usr/bin/env python
# -*- coding: utf-8 -*-

from myEncoder import MyEncoder
from cardapio import Cardapio
import requests
from bs4 import BeautifulSoup
import os
import json
from os import listdir
from os.path import isfile, join
from unicodedata import normalize

_URL = "http://ru.ufes.br/cardapio/"
pp = {}

def getType(tipo):
    if "almo" in tipo.lower():
        return "almoco"
    else:
        return "jantar"

def createMenuFiles():
    for i in range(2015,2018):
        for j in range(1,13):

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

                searchURL = _URL + str(i) + "-" + month + "-" + day
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
                                tipo = getType(tipo.get_text())
                                file = open(os.path.join("files",date+"_"+tipo + ".txt"), "w")
                                # print(tipo.get_text())
                                cardapio = refeicao.find("div", class_="views-field-body").find_all("div", class_="field-content")

                                for item in cardapio:
                                    file.write(item.get_text().strip())
                        print("Request " + searchURL + " realizado com sucesso!")

def remover_acentos(txt):
   return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')

def readFile(filename):
    fp = open(filename,"r")
    menu = fp.readlines()
    clean_menu = []
    for i in range(0,len(menu)):
        menu[i] = menu[i].replace('\xa0','')
        if menu[i] != '\n' and menu[i] != '\t\n':
            clean_menu.append(menu[i])
    return clean_menu

def buildObject(filename):
    cardapio = Cardapio()
    menu = readFile(filename)
    tipo = getType(filename)
    cardapio.setTipo(tipo)

    cardapio.setData(filename[6:16])
    for i in range(0, len(menu)):
        if "salada\n" in menu[i].lower():
            saladas = menu[i+1].replace('\t', '')
            cardapio.setSalada(remover_acentos(saladas))
            # print(saladas)
        elif "prato" in menu[i].lower():
            pratos = menu[i + 1].replace('\n', '').replace('\t', '')
            cardapio.setPrato(remover_acentos(pratos))
            getPrato(pratos)
            # print(pratos)
        elif "opção" in menu[i].lower():
            opt = menu[i + 1].replace('\n', '')
            cardapio.setOpcao(remover_acentos(opt))
            # print(opt)
        elif "guarnição" in menu[i].lower():
            guarnicoes = menu[i + 1].replace('\n', '')
            cardapio.setGuarnicao(remover_acentos(guarnicoes))
            # print(guarnicoes)
        elif "sobremesa" in menu[i].lower():
            sobremesa = menu[i + 1].replace('\n', '')
            cardapio.setSobremesa(remover_acentos(sobremesa))
            # print(sobremesa)
        elif "suco" in menu[i].lower():
            suco = menu[i].replace('\n', '').replace('\t', '')
            cardapio.setSuco(remover_acentos(suco))

        elif "acompanhamento" in menu[i].lower():
            acompanhamento = menu[i+1].replace('\n', '').replace('\t', '')
            cardapio.setAcompanhamento(acompanhamento)
            # print(suco)
    return cardapio

def getPrato(pratos):
    global pp
    it = pratos.split("/")

    for p in it:
        print(p)
        if(p[0] == " "):
            word = p[1:-1].lower()
        elif(p[-1] == " "):
            word = p[0:-2].lower()
        else:
            word = p.lower()

        if word not in pp:
            pp[word] = 0

        pp[word] += 1



def printDict():
    global pp
    count = 0
    for key,value in pp.items():
        count += 1
        print(str(count)+ ";"+key+";"+str(value))


def generateJson():
    file = open("db.json","w")
    databaseRU = []
    onlyfiles = [f for f in os.listdir("files") if isfile(join("files", f))]
    for filename in onlyfiles:
        cardapio = buildObject(os.path.join("files", filename))
        databaseRU.append(cardapio)
    # print(json.dumps(databaseRU,cls=MyEncoder))
    # file.write('{\"cardapio\":'+json.dumps(databaseRU,cls=MyEncoder)+'}')


# obj = buildObject(os.path.join("files", "01-02-2016_almoco.txt"))
# print(json.dumps(obj.__dict__))



generateJson()
# printDict()