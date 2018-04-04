from config.configuration import Configuration
from sqlalchemy.dialects.postgresql import ARRAY, array

class Log(Configuration.db.Model):

    __tablename__ = "log"

    id = Configuration.db.Column(Configuration.db.BIGINT, primary_key=True, autoincrement=True)
    data = Configuration.db.Column(Configuration.db.DateTime,nullable=False)
    message = Configuration.db.Column(Configuration.db.String(1500), nullable=False)
    response = Configuration.db.Column(Configuration.db.String(1500), nullable=False)
    entities = Configuration.db.Column(ARRAY(Configuration.db.Text), nullable=True)
    usuario_id = Configuration.db.Column(Configuration.db.BIGINT,Configuration.db.ForeignKey('usuario.id'), nullable=False)
    usuario = Configuration.db.relationship('Usuario', backref = Configuration.db.backref('log', lazy=True))

    def get_id(self):
        return self.id

    def get_data(self):
        return self.data

    def get_message(self):
        return self.message

    def get_response(self):
        return self.response

    def get_entities(self):
        return self.entities

    def get_usuario_id(self):
        return self.usuario_id

    def set_id(self,id):
        self.id = id

    def set_data(self,data):
        self.data = data

    def set_message(self,message):
        self.message = message

    def set_response(self,response):
        self.response = response

    def set_entities(self,entities):
        self.entities = entities

    def set_usuario_id(self,usuario_id):
        self.usuario_id = usuario_id

    def __repr__(self):
        return '<Log %r>' % self.id