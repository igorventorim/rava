class Course:

    def __init__(self, code, name, teatcher_id):
        self.__code = code
        self.__name = name
        self.__teatcher_id = teatcher_id
        self.__questions = []
        self.__students = []

    def __init__(self, name, teatcher_id):
        self.__code = name[0]+teatcher_id[0:4]
        self.__name = name
        self.__teatcher_id = teatcher_id
        self.__questions = []
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
        self.__questions.append(question)

    def getStudents(self):
        return self.__students

    def addStudent(self, student):
        self.__students.append(student)

    def getQuestionsToString(self):
        result=""
        for question in self.__questions:
            result += str(question.getCode()) + question.getDesc()+"\n"
        return result


    @staticmethod
    def getCurso(cursos,code):
        for course in cursos:
            if course.getCode() == code:
                return course
        return None

    # TODO: REFORMULAR FUNÇÃO
    @staticmethod
    def listCourses(cursos, teatcher_id):
        list = ""
        courses=[]
        for course in cursos:
            if course.getTeatcher() == teatcher_id:
                list = str(course.getCode())+":"+course.getName()+" "
                courses.append(course)
        return [courses,list]