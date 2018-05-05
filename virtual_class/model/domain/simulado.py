# from app import db
from config.configuration import Configuration

class Simulado(Configuration.db.Model):

    __tablename__ = "simulado"
    id = Configuration.db.Column(Configuration.db.BIGINT, autoincrement=True, primary_key=True)
    questao = Configuration.db.Column(Configuration.db.String(50), unique=True, nullable=False)
    resposta = Configuration.db.Column(Configuration.db.String(1000), nullable=False)
    conteudo = Configuration.db.Column(Configuration.db.String(50), unique=True, nullable=False)

    def __init__(self, questao, resposta, curso):
        self.questao = questao
        self.resposta = resposta
        self.conteudo = curso

    def getId(self):
        return self.id

    def getQuestao(self):
        return self.questao

    def getResposta(self):
        return self.resposta

    def getConteudo(self):
        return self.conteudo

    def setQuestao(self,questao):
        self.questao = questao

    def setResposta(self,resposta):
        self.resposta = resposta

    def setConteudo(self,curso):
        self.conteudo = curso