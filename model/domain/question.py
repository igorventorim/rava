from route import db

class Question(db.Model):

    __tablename__ = "question"
    id = db.Column(db.BIGINT,autoincrement=True,primary_key=True)
    question_code = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.String(1000),nullable=False)
    course_id = db.Column(db.BIGINT,db.ForeignKey('course_id'))

    def __init__(self, code, desc):
        self.__code = code
        self.__desc = desc
        self.__answers = []
        self.question_code = code
        self.description = desc

    def getCode(self):
        return self.__code

    def getDesc(self):
        return self.__desc

    def getAnswers(self):
        return self.__answers

    def addAnswer(self,answer):
        self.__answers.append(answer)
