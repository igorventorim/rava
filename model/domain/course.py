from route import db

class Course(db.Model):

    __tablename__ = "course"
    id = db.Column(db.BIGINT, primary_key = True, autoincrement=True)
    course_code = db.Column(db.String(50),unique=True,nullable=False)
    name = db.Column(db.String(100),nullable=False)
    description = db.Column(db.String(200))
    teatcher_id = db.Column(db.BIGINT, db.ForeignKey('teacher.Id'),nullable=False)

    # numberCourses = 0

    def __init__(self, code, name, teatcher_id):
        # Course.numberCourses += 1
        self.__code = code
        self.__name = name
        self.__teatcher_id = teatcher_id
        self.__questions = {}
        self.__students = []
        self.teatcher_id = teatcher_id
        self.name = name
        self.course_code = code

    def __init__(self, name, teatcher_id):
        # Course.numberCourses += 1
        # self.__code = "CC"+str(Course.numberCourses)
        self.__name = name
        self.__teatcher_id = teatcher_id
        self.__questions = {}
        self.__students = []
        self.teatcher_id = teatcher_id
        self.name = name
        self.course_code = "CC"+str(self.__getLastId()+1)

    def getId(self):
        return self.id

    def getCode(self):
        return self.course_code

    def getName(self):
        return self.name

    def getTeatcher(self):
        return self.teatcher_id

    def __getLastId(self):
        id = Course.query.orde_by(Course.id.desc()).first()
        if( id is None):
            return 0
        return id

    # def getQuestions(self):
    #     return self.__questions
    #
    # def addQuestion(self,question):
    #     self.__questions[question.getCode()] = question

    def getStudents(self):
        return self.__students

    def addStudent(self, student_id):
        self.__students.append(student_id)

    # def getQuestionsToString(self):
    #     result=""
    #     for k,question in self.__questions.items():
    #         result += question.getCode() +":"+ question.getDesc()+"\n"
    #     return result


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