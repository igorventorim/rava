from app import db

class Teatcher(db.Model):

    __tablename__ = "teacher"
    id = db.Column(db.BIGINT, primary_key = True)
    teatcher_code = db.Column(db.String(50), unique = True,nullable=False)
    # courses = db.relationship('Course', backref='teatcher',lazy=True)

    def __init__(self,teatcher_id):
        # Teatcher.id = 1
        self.id = teatcher_id
        self.teatcher_code = "TC"+str(self.__getLastId()+1)

    def __repr__(self):
        return '<User %r>' % self.student_code

    def addCourse(self, course_id):
        self.__courses.append(course_id)

    def getCourses(self):
        return self.__courses

    def getTeacherCode(self):
        return self.teacher_code

    def getId(self):
        return self.id

    def __getLastId(self):
        id = Teatcher.query.order_by(Teatcher.id.desc()).first()
        if( id is None):
            return 0
        return id.getId()