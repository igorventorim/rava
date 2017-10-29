class Answer:

    def __init__(self,answer_text, user_id):
        self.__answer_text = answer_text
        self.__user_id = user_id

    def getAnswerText(self):
        return self.__answer_text

    def getUserId(self):
        return self.__user_id