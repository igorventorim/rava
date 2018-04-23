from config.configuration import Configuration

class Programacao(Configuration.db.Model):

    __tablename__ = "programacao"

    id = Configuration.db.Column(Configuration.db.BIGINT, primary_key=True, autoincrement=True)
    data = Configuration.db.Column(Configuration.db.Date,nullable=False)
    filme_id = Configuration.db.Column(Configuration.db.BIGINT,Configuration.db.ForeignKey('filme.id'), nullable=False)
    filme = Configuration.db.relationship('Filme', backref = Configuration.db.backref('programacao', lazy=True))
    horario = Configuration.db.Column(Configuration.db.String(50),nullable=True)

    def __repr__(self):
        return '<Programacao %r>' % self.id

    def get_id(self):
        return self.id

    def get_date(self):
        return self.data

    def get_filme_id(self):
        return self.filme_id

    def get_filme(self):
        return self.filme

    def get_horario(self):
        return self.horario

    def set_date(self,date):
        self.data = date

    def set_horario(self,horario):
        self.horario = horario

    def set_filme_id(self,filme_id):
        self.filme_id = filme_id