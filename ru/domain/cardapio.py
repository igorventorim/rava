from app import db

class Cardapio(db.Model):

    __tablename__ = "cardapio"
    id = db.Column(db.BIGINT, primary_key=True, autoincrement=True)
    texto = db.Column(db.String(800), nullable=False)
    tipo = db.Column(db.Integer, nullable=False)
    data = db.Column(db.Date, nullable=False)
    salada = db.Column(db.String(150))
    prato = db.Column(db.String(150))
    acompanhamento = db.Column(db.String(150))
    guarnicao = db.Column(db.String(150))
    sobremesa = db.Column(db.String(150))
    suco = db.Column(db.String(150))

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