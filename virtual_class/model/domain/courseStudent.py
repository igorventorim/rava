# from app import db
from config.configuration import Configuration

class CourseStudent(Configuration.db.Model):

    __tablename__ = "courseStudent"
    course_id = Configuration.db.Column(Configuration.db.BIGINT, Configuration.db.ForeignKey('course.id'), primary_key=True)
    student_id = Configuration.db.Column(Configuration.db.BIGINT, Configuration.db.ForeignKey('student.id'), primary_key=True)

    def __init__(self,course_id,student_id):
        self.course_id = course_id
        self.student_id = student_id

    def getCourseId(self):
        return self.course_id

    def getStudentId(self):
        return self.student_id
