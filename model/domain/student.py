# from authentication import Authentication
# db = Authentication.DATABASE
from route import db

class Student(db.Model):

    __tablename__ = "student"
    Id = db.Column(db.Integer, primary_key = True)
    student_code = db.Column(db.String(50), unique = True)
    id = 0

    def __init__(self,student_id):
        Student.id += 1
        self.__student_id = student_id
        self.__student_code = "ST"+str(Student.id)
        self.__courses = []
        self.__answers = []
        self.Id = student_id
        self.student_code = "ST"+str(Student.id)

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