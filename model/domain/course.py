class Course:

    numberCourses = 0

    def __init__(self, code, name, teatcher_id):
        Course.numberCourses += 1
        self.__code = code
        self.__name = name
        self.__teatcher_id = teatcher_id
        self.__questions = {}
        self.__students = []

    def __init__(self, name, teatcher_id):
        Course.numberCourses += 1
        self.__code = "CC"+str(Course.numberCourses)
        self.__name = name
        self.__teatcher_id = teatcher_id
        self.__questions = {}
        self.__students = []

    def getCode(self):
        return self.__code

    def getName(self):
        return self.__name

    def getTeatcher(self):
        return self.__teatcher_id

    def getQuestions(self):
        return self.__questions

    def addQuestion(self,question):
        self.__questions[question.getCode()] = question

    def getStudents(self):
        return self.__students

    def addStudent(self, student_id):
        self.__students.append(student_id)

    def getQuestionsToString(self):
        result=""
        for question in self.__questions:
            result += str(question.getCode()) +":"+ question.getDesc()+"\n"
        return result


    @staticmethod
    def getCurso(cursos,code):
        for course in cursos:
            if course.getCode().upper() == code.upper():
                return course
        return None

    # TODO: REFORMULAR FUNÇÃO
    @staticmethod
    def listCourses(cursos, teatcher_id):
        list = ""
        courses=[]
        for course in cursos:
            if course.getTeatcher() == teatcher_id:
                list += str(course.getCode())+":"+course.getName()+"\n"
                courses.append(course)
        return [courses,list]