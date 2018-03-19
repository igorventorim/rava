from app import db

class Person(db.Model):

    __tablename__ = "person"

    id = db.Column(db.BIGINT, primary_key=True)
    name = db.Column(db.String(100))

    def __init__(self, person_id):
        self.id = person_id

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def set_name(self,name):
        self.name = name

    def set_id(self,id):
        self.id = id