from virtual_class.model.domain.question import Question
# from app import db
from config.configuration import Configuration


class Course(Configuration.db.Model):

    __tablename__ = "course"
    id = Configuration.db.Column(Configuration.db.BIGINT, primary_key = True, autoincrement=True)
    course_code = Configuration.db.Column(Configuration.db.String(50), unique=True, nullable=False)
    name = Configuration.db.Column(Configuration.db.String(100), nullable=False)
    description = Configuration.db.Column(Configuration.db.String(200))
    teatcher_id = Configuration.db.Column(Configuration.db.BIGINT, Configuration.db.ForeignKey('teacher.id'), nullable=False)

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
        id = Course.query.order_by(Course.id.desc()).first()
        if( id is None):
            return 0
        return id.getId()

    # def getQuestions(self):
    #     return self.__questions
    #
    # def addQuestion(self,question):
    #     self.__questions[question.getCode()] = question

    def getStudents(self):
        return self.__students

    def addStudent(self, student_id):
        self.__students.append(student_id)

    def getQuestionsToString(self):
        result=""
        # for k,question in Question.query.filter_by(question_code=self.getCode()):
        #     result += question.getCode() +":"+ question.getDesc()+"\n"
        # return result
        questions = Question.query.filter_by(course_id=self.getId()).all()
        for question in questions:
            result += question.getCode()+":"+question.getDesc()+"\n"
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