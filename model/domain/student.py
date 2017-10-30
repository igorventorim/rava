class Student:

    def __init__(self,student_id):
        self.__student_id = student_id
        self.__courses = []
        self.__answers = []

    def addCourse(self, course_id):
        self.__courses.append(course_id)

    def registerAnswer(self,answer):
        self.__answers.append(answer)

    def getCourses(self):
        return self.__courses

    def getAnswers(self):
        return self.__answers