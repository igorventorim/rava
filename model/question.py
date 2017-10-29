class Question:

    def __init__(self, code, desc):
        self.__code = code
        self.__desc = desc
        self.__answers = []

    def getCode(self):
        return self.__code

    def getDesc(self):
        return self.__desc

    def getAnswers(self):
        return self.__answers

    def addAnswer(self,answer):
        self.__answers.append(answer)
