# from app import db
from config.configuration import Configuration


class Answer(Configuration.db.Model):

    __tablename__ = "answer"
    id = Configuration.db.Column(Configuration.db.BIGINT, primary_key = True, autoincrement=True)
    answer_text = Configuration.db.Column(Configuration.db.String(1000), nullable=False)
    feedback = Configuration.db.Column(Configuration.db.String(1000))
    student_id = Configuration.db.Column(Configuration.db.BIGINT, Configuration.db.ForeignKey('student.id'), nullable=False)
    question_id = Configuration.db.Column(Configuration.db.BIGINT, Configuration.db.ForeignKey('question.id'), nullable=False)
    nota = Configuration.db.Column(Configuration.db.DECIMAL)
    review = Configuration.db.Column(Configuration.db.Boolean, default=False)

    # id = 0

    def __init__(self,answer_text, user_id, question_id):
        # Answer.id += 1
        # self.__id = self.__getLastId()+1
        self.__answer_text = answer_text
        self.__user_id = user_id
        self.__question_id = question_id
        self.__feedback = ""
        self.answer_text = answer_text
        self.student_id = user_id
        self.question_id = question_id

    def getAnswerText(self):
        return self.answer_text

    def getUserId(self):
        return self.__user_id

    def getQuestionId(self):
        return self.question_id

    def getFeedback(self):
        return self.feedback

    def getItemId(self):
        return self.__id

    def addFeedback(self,feedback):
        self.__feedback = feedback

    def getId(self):
        return self.id

    def getStudentId(self):
        return self.student_id

    def __getLastId(self):
        id = Answer.query.order_by(Answer.id.desc()).first()
        if( id is None):
            return 0
        return id.getId()

    def getNota(self):
        return self.nota