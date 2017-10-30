class Student:

    def __init__(self,student_id):
        self.__student_id = student_id
        self.__courses = []
        self.__answer = []

    def addCourse(self, course_id):
        self.__courses.append(course_id)

    def registerAnswer(self,answer):
        self.__answer.append(answer)