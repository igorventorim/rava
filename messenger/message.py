class Message:
    def __init__(self, messaging_event):
        self.__client_id = messaging_event["sender"]["id"]
        self.__messaging_event = messaging_event
        self.__isMessage = "message" in self.__messaging_event
        self.__isPostback = "postback" in self.__messaging_event
        self.__content_message = self.__getPayloadOrText()
        self.__entities = None
        self.__intent = None

    def __getPayloadOrText(self): # just to instanciate the above
        if self.__isMessage:
            return self.__getMessageText()
        elif self.__isPostback:
            return self.__getPostbackPayload()
        else:
            raise TypeError("Message sent from client was not a text neither a payload.")

    def getContentMessage(self):
        return self.__content_message

    def isMessage(self):
        return self.__isMessage

    def isPostback(self):
        return self.__isPostback

    def getClientID(self):
        return self.__client_id

    def __getMessageText(self):
        if "attachments" in self.__messaging_event["message"]:
            return "attachments" # caso o usuario clicar no joinha da isso
        else:
            return self.__messaging_event["message"]["text"]

    def __getPostbackPayload(self):
        return self.__messaging_event["postback"]["payload"]

    def setEntities(self,entities):
        self.__entities = entities

    def getEntities(self):
        return self.__entities

    def setIntent(self,intent):
        self.__intent = intent

    def getIntent(self):
        return self.__intent
