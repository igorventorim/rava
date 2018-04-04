import bcrypt as bcrypt

from config.configuration import Configuration

class Usuario(Configuration.db.Model):

    __tablename__ = "usuario"

    id = Configuration.db.Column(Configuration.db.BIGINT, primary_key=True, autoincrement=True)
    code = Configuration.db.Column(Configuration.db.String(80), unique=True, nullable=False)
    email = Configuration.db.Column(Configuration.db.String(120),unique=True, nullable=True)
    senha = Configuration.db.Column(Configuration.db.String(300), nullable=True)
    nome = Configuration.db.Column(Configuration.db.String(100), nullable=True)


    def __repr__(self):
        return '<Usuario %r>' % self.id

    def get_id(self):
        return self.id

    def get_code(self):
        return self.code

    def get_email(self):
        return self.email

    def get_senha(self):
        return self.senha

    def get_nome(self):
        return self.nome

    def set_id(self,id):
        self.id = id

    def set_code(self,code):
        self.code = code

    def set_email(self,email):
        self.email = email

    def set_senha(self,senha):
        self.senha = bcrypt.encrypt(senha)

    def set_nome(self, nome):
        self.nome = nome

    def validate_password(self,senha):
        return bcrypt.verify(senha,self.senha)