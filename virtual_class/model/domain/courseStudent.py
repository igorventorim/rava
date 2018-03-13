from app import db

class CourseStudent(db.Model):

    __tablename__ = "courseStudent"
    course_id = db.Column(db.BIGINT,db.ForeignKey('course.id'),primary_key=True)
    student_id = db.Column(db.BIGINT,db.ForeignKey('student.id'),primary_key=True)

    def __init__(self,course_id,student_id):
        self.course_id = course_id
        self.student_id = student_id

    def getCourseId(self):
        return self.course_id

    def getStudentId(self):
        return self.student_id
