from config.configuration import Configuration

class Filme(Configuration.db.Model):

    __tablename__ = "filme"

    id = Configuration.db.Column(Configuration.db.BIGINT, primary_key=True, autoincrement=True)
    titulo = Configuration.db.Column(Configuration.db.String(300), nullable=False)
    sinopse = Configuration.db.Column(Configuration.db.String(2000), nullable=True)
    classificacao = Configuration.db.Column(Configuration.db.String(15), nullable=True)


    def get_id(self):
        return self.id

    def get_titulo(self):
        return self.titulo

    def get_sinopse(self):
        return self.sinopse

    def get_classificacao(self):
        return self.classificacao

    def set_id(self,id):
        self.id = id

    def set_titulo(self,titulo):
        self.titulo = titulo

    def set_sinopse(self,sinopse):
        self.sinopse = sinopse

    def set_classificacao(self,classificacao):
        self.classificacao = classificacao