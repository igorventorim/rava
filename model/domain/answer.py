class Answer(object):

    id = 0

    def __init__(self,answer_text, user_id, question_id):
        Answer.id += 1
        self.__id = Answer.id
        self.__answer_text = answer_text
        self.__user_id = user_id
        self.__question_id = question_id
        self.__feedback = ""

    def getAnswerText(self):
        return self.__answer_text

    def getUserId(self):
        return self.__user_id

    def getQuestionId(self):
        return self.__question_id

    def getFeedback(self):
        return self.__feedback

    def getItemId(self):
        return self.__id

    def addFeedback(self,feedback):
        self.__feedback = feedback