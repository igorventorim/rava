# from app import db
from config.configuration import Configuration

class Cardapio(Configuration.db.Model):

    __tablename__ = "cardapio"

    id = Configuration.db.Column(Configuration.db.BIGINT, primary_key=True, autoincrement=True)
    texto = Configuration.db.Column(Configuration.db.String(800), nullable=False)
    tipo = Configuration.db.Column(Configuration.db.Integer, nullable=False)
    data = Configuration.db.Column(Configuration.db.Date, nullable=False)
    salada = Configuration.db.Column(Configuration.db.String(150))
    prato = Configuration.db.Column(Configuration.db.String(150))
    # opcao = Configuration.db.Column(Configuration.db.String(150))
    acompanhamento = Configuration.db.Column(Configuration.db.String(150))
    guarnicao = Configuration.db.Column(Configuration.db.String(150))
    sobremesa = Configuration.db.Column(Configuration.db.String(150))
    suco = Configuration.db.Column(Configuration.db.String(150))

    def get_id(self):
        return self.id

    def get_texto(self):
        return self.texto

    def get_tipo(self):
        return self.tipo

    def get_data(self):
        return self.data

    def get_salada(self):
        return self.salada

    def get_prato(self):
        return self.prato

    def get_acompanhamento(self):
        return self.acompanhamento

    def get_guarnicao(self):
        return self.guarnicao

    def get_sobremesa(self):
        return self.sobremesa

    def get_suco(self):
        return self.suco

    # def get_opcao(self):
    #     return self.opcao

    def set_id(self,id):
        self.id = id

    def set_texto(self,texto):
        self.texto = texto

    def set_tipo(self, tipo):
        self.tipo = tipo

    def set_data(self, data):
        self.data = data

    def set_salada(self,salada):
        self.salada = salada

    def set_prato(self, prato):
        self.prato = prato

    def set_acompanhamento(self, acompanhamento):
        self.acompanhamento = acompanhamento

    def set_guarnicao(self, guarnicao):
        self.guarnicao = guarnicao

    def set_sobremesa(self,sobremesa):
        self.sobremesa = sobremesa

    def set_suco(self,suco):
        self.suco = suco

    # def set_opcao(self,opcao):
    #     self.opcao = opcao

    def __repr__(self):
        return "Cardápio:\n\nTipo: "+str(self.get_tipo()) +"\nData: "+str(self.get_data())+"\nSalada: "+str(self.get_salada())\
               +"Prato: "+str(self.get_prato())+"\nAcompanhamento: "+str(self.get_acompanhamento())+"\nGuarnição: "+str(self.get_guarnicao())\
               +"\nSobremesa: "+str(self.get_sobremesa())+"\nSuco: "+str(self.get_suco())+ \
               "\n=============================\n"
               # "\nOpcao: "+self.get_opcao()+\


