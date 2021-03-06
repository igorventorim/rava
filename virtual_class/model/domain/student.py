# from authentication import Authentication
# db = Configuration.DATABASE
# from app import db
from config.configuration import Configuration

class Student(Configuration.db.Model):

    __tablename__ = "student"
    id = Configuration.db.Column(Configuration.db.BIGINT, primary_key = True)
    student_code = Configuration.db.Column(Configuration.db.String(50), unique = True, nullable=False)
    # id = 0

    def __init__(self,student_id):
        # Student.id += 1
        self.__student_id = student_id
        # self.__student_code = "ST"+str(self.__getLastId()+1)
        self.__courses = []
        self.__answers = []
        self.id = student_id
        self.student_code = "ST"+str(self.__getLastId()+1)

    def __repr__(self):
        return '<User %r>' % self.student_code

    def addCourse(self, course_id):
        self.__courses.append(course_id)

    def registerAnswer(self,answer):
        self.__answers.append(answer)

    def getCourses(self):
        return self.__courses

    def getAnswers(self):
        return self.__answers

    def getStudentCode(self):
        return self.__student_code

    def getId(self):
        return self.id

    def __getLastId(self):
        id = Student.query.order_by(Student.id.desc()).first()
        if( id is None):
            return 0
        return id.getId()