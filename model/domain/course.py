class Course:

    def __init__(self,code,name,teatcher):
        self.__code = code
        self.__name = name
        self.__teatcher = teatcher
        self.__questions = []

    def getCode(self):
        return self.__code

    def getName(self):
        return self.__name

    def getTeatcher(self):
        return self.__teatcher

    def getQuestions(self):
        return self.__questions

    def addActivity(self,question):
        self.__questions.append(question)
