from route import db

class Teatcher(db.Model):

    __tablename__ = "teatcher"
    Id = db.Column(db.BIGINT, primary_key = True)
    teatcher_code = db.Column(db.String(50), unique = True,nullable=False)
    id = 0

    def __init__(self,teatcher_id):
        Teatcher.id += 1
        self.Id = teatcher_id
        self.teacher_code = "TC"+str(Teatcher.id)

    def __repr__(self):
        return '<User %r>' % self.student_code

    def addCourse(self, course_id):
        self.__courses.append(course_id)

    def getCourses(self):
        return self.__courses

    def getTeacherCode(self):
        return self.teacher_code

    def getId(self):
        return self.Id