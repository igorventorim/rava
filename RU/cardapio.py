#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Cardapio(object):

    def __init__(self):
        pass

    # def __init__(self,data, tipo, salada, prato, opcao=None, acompanhamento=None,sobremesa=None, suco=None):
    #     self.__tipo = tipo
    #     self.__salada= salada
    #     self.__prato = prato
    #     self.__opcao = opcao
    #     self.__acompanhamento = acompanhamento
    #     self.__sobremesa = sobremesa
    #     self.__suco = suco
    #     self.__data = data

    def getGuarnicao(self):
        return self.__guarnicao

    def setGuarnicao(self,param):
        self.__guarnicao = param

    def getData(self):
        return self.__data

    def getTipo(self):
        return self.__tipo

    def getSalada(self):
        return self.__salada

    def getPrato(self):
        return self.__prato

    def getOpcao(self):
        return self.__opcao

    def getAcompanhamento(self):
        return self.__acompanhamento

    def getSobremesa(self,param):
         self.__sobremesa = param

    def getSuco(self):
        return self.__suco

    def setData(self,param):
        self.__data = param

    def setTipo(self,param):
        self.__tipo = param

    def setSalada(self,param):
        self.__salada = param

    def setPrato(self,param):
        self.__prato = param

    def setOpcao(self,param):
        self.__opcao = param

    def setAcompanhamento(self,param):
        self.__acompanhamento = param

    def setSobremesa(self,param):
        self.__sobremesa = param

    def setSuco(self,param):
        self.__suco = param

    def __repr__(self):
        return self.getTipo() +" - "+self.getData()