# from app import db
from config.configuration import Configuration

class Question(Configuration.db.Model):

    __tablename__ = "question"
    id = Configuration.db.Column(Configuration.db.BIGINT, autoincrement=True, primary_key=True)
    question_code = Configuration.db.Column(Configuration.db.String(50), unique=True, nullable=False)
    description = Configuration.db.Column(Configuration.db.String(1000), nullable=False)
    course_id = Configuration.db.Column(Configuration.db.BIGINT, Configuration.db.ForeignKey('course.id'))

    def __init__(self, code, desc, course_id):
        self.__code = code
        self.__desc = desc
        self.__answers = []
        self.question_code = code
        self.description = desc
        self.course_id = course_id

    def getId(self):
        return self.id

    def getCode(self):
        return self.question_code

    def getDesc(self):
        return self.description

    def getAnswers(self):
        return self.__answers

    def addAnswer(self,answer):
        self.__answers.append(answer)
