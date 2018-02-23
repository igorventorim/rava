class Object(object):

    def __init__(self):
        self.__course = None
        self.__instanceid = None
        self.__userid = None
        self.__contextid = None
        self.__itemid = None
        self.__filename = None
        self.__rawgrademin = None
        self.__rawgrademax = None
        self.__id_grade_grades = None
        self.__notaProfessor = None
        self.__course_name = None
        self.__resposta = None
        self.__url = None
        self.__feedback = None
        self.__question = None

    def getFeedback(self):
        return self.__feedback

    def getCourse(self):
        return self.__course

    def getInstanceId(self):
        return self.__instanceid

    def getUserId(self):
        return self.__userid

    def getContextId(self):
        return self.__contextid

    def getItemId(self):
        return self.__itemid

    def getFileName(self):
        return self.__filename

    def getRawGradeMin(self):
        return self.__rawgrademin

    def getRawGradeMax(self):
        return self.__rawgrademax

    def getIdGradeGrades(self):
        return self.__id_grade_grades

    def getNotaProfessor(self):
        return self.__notaProfessor

    def getCourseName(self):
        return self.__course_name

    def getResposta(self):
        return self.__resposta

    def getUrl(self):
        return self.__url

    def getQuestion(self):
        return self.__question

    def setCourse(self, value):
        self.__course = value

    def setInstanceId(self, value ):
        self.__instanceid = value

    def setUserId(self, value):
        self.__userid = value

    def setContextId(self, value):
        self.__contextid = value

    def setItemId(self, value):
        self.__itemid = value

    def setFileName(self, value):
        self.__filename = value

    def setRawGradeMin(self, value):
        self.__rawgrademin = value

    def setRawGradeMax(self, value):
        self.__rawgrademax = value

    def setIdGradeGrades(self, value):
        self.__id_grade_grades = value

    def setNotaProfessor(self, value):
        self.__notaProfessor = value

    def setCourseName(self, value):
        self.__course_name = value

    def setResposta(self, value):
        self.__resposta = value

    def setUrl(self, value):
        self.__url = value

    def setFeedback(self, value):
        self.__feedback = value

    def setQuestion(self,value):
        self.__question = value



