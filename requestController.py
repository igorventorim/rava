from authentication import Authentication
from message import Message
import requests
import answerViewTemplates
from strings import Strings
from userData import UserData


class RequestController:

    def __init__(self):
        self.__PARAMS = {"access_token": Authentication.PAGE_ACCESS_TOKEN}
        self.__HEADERS = {"Content-Type": "application/json"}
        self.__cursos = []


    def unpackMessage(self,data):
        if data["object"] == "page":
            for entry in data["entry"]:
                for messaging_event in entry["messaging"]:
                    message = Message(messaging_event)
                    self.__selector(message)


    def __sendMessage(self,data):
        r = requests.post("https://graph.facebook.com/v2.6/me/messages", params=self.__PARAMS, headers=self.__HEADERS, data=data)
        if r.status_code != 200:
            print(r.status_code)
            print(r.text)


    def __selector(self,message):
        try:
            cmd = message.getContentMessage().split(' ', 1)[0]
            if(cmd[0] != "#"):
                self.__options[cmd.upper()](self,message)
            else:
                self.__answer(message)
        except:
            self.__erro(message)

    # V1.0 - OK
    def __started(self,message):
        user_id = message.getClientID()
        msgText = Strings.GREETING_KNOWN_USER.format(UserData().getFirstNameClient(user_id))
        data = answerViewTemplates.text(user_id, msgText)
        self.__sendMessage(data)
        msgText = Strings.APRESENTATION
        data = answerViewTemplates.quick_reply(user_id, msgText, [Strings.PROFESSOR, Strings.ALUNO])
        self.__sendMessage(data)

    # V1.0 - OK
    def __help(self,message):
        user_id = message.getClientID()
        data = answerViewTemplates.text(user_id, Strings.HELP_INFO_PROFESSOR)
        self.__sendMessage(data)
        data = answerViewTemplates.text(user_id, Strings.HELP_INFO_ALUNO)
        self.__sendMessage(data)

    # V1.0 - OK
    def __professor(self,message):
        user_id = message.getClientID()
        data = answerViewTemplates.text(user_id, Strings.PROFESSOR_INFO)
        self.__sendMessage(data)

    # V1.0 - OK
    def __aluno(self,message):
        user_id = message.getClientID()
        data = answerViewTemplates.text(user_id, Strings.ALUNO_INFO)
        self.__sendMessage(data)

    # V1.0 - OK
    def __erro(self,message):
        user_id = message.getClientID()
        data = answerViewTemplates.text(user_id, Strings.APOLOGIZE_USER_FOR_ERROR)
        self.__sendMessage(data)

    #TODO: REGISTER COURSE IN THE FILE WITH HIS CREATOR USER
    def __criar_curso(self,message):
        content_message = message.getContentMessage()
        course_name = content_message[content_message.find(" "):]
        user_id = message.getClientID()
        data = answerViewTemplates.text(user_id, "Voce criou o curso "+course_name)
        self.__sendMessage(data)

    #TODO: REGISTER ACTIVITY IN THE FILE WITH HIS COURSE
    def __criar_atividade(self,message):
        content_message = message.getContentMessage()
        curso = None
        user_id = message.getClientID()
        data = answerViewTemplates.text(user_id, "Vamos criar uma atividade :)")
        self.__sendMessage(data)
        self.__info_nova_atividade(curso)

    #TODO: READ FILE COURSES AND SHOW HIS NAME AND CODE
    def __listar_cursos(self,message):
        content_message = message.getContentMessage()
        user_id = message.getClientID()
        data = answerViewTemplates.text(user_id, "Vamos listar os meus cursos criados :)")
        self.__sendMessage(data)

    # TODO: READ FILE ACTIVITYS AND SHOW HIS NAME AND CODE
    def __listar_atividades(self,message):
        content_message = message.getContentMessage()
        user_id = message.getClientID()
        data = answerViewTemplates.text(user_id, "Vamos listar minhas atividades criadas :)")
        self.__sendMessage(data)

    # TODO: REGISTER USER IN THE COURSE
    def __login_curso(self,message):
        content_message = message.getContentMessage()
        user_id = message.getClientID()
        data = answerViewTemplates.text(user_id, "Me cadastrei em um curso :)")
        self.__sendMessage(data)

    # TODO: SHOW ACTIVITYS THE USER HAVE FOR ANSWER
    def __visualizar_atividades(self,message):
        content_message = message.getContentMessage()
        user_id = message.getClientID()
        data = answerViewTemplates.text(user_id, "Visualizar as atividades dos cursos que estou cadastrado :)")
        self.__sendMessage(data)

    # TODO: SHOW FEEDBACK FOR USER
    def __visualizar_notas(self,message):
        content_message = message.getContentMessage()
        user_id = message.getClientID()
        data = answerViewTemplates.text(user_id, "Visualizar as notas das atividades que eu respondi :)")
        self.__sendMessage(data)

    def __info_nova_atividade(self,curso):
        #TODO: GET IDs REGISTERED IN THE COURSES AND SEND MESSAGE OF NEW ACTIVITY!
        pass

    def info_feedback(self):
        #TODO: AFTER CORRECTION PNOTA SEND RESULTS FOR USERS
        pass

    def __answer(self,message):
        #TODO: REGISTER ANSWER IN THE SERVER ON STRUCT FOR PNOTA
        content_message = message.getContentMessage()
        user_id = message.getClientID()
        data = answerViewTemplates.text(user_id, "Resposta enviada com sucesso :)")
        self.__sendMessage(data)

    __options = {Strings.GET_STARTED.upper(): __started,
               Strings.HELP.upper(): __help,
               Strings.PROFESSOR.upper(): __professor,
               Strings.ALUNO.upper(): __aluno,
               Strings.CMD_CRIAR_CURSO.upper(): __criar_curso,
               Strings.CMD_CRIAR_ATIVIDADE.upper(): __criar_atividade,
               Strings.CMD_LISTAR_CURSOS.upper(): __listar_cursos,
               Strings.CMD_LISTAR_ATIVIDADES.upper(): __listar_atividades,
               Strings.CMD_LOGIN_CURSO.upper(): __login_curso,
               Strings.CMD_VISUALIZAR_ATIVIDADES.upper(): __visualizar_atividades,
               Strings.CMD_VISUALIZAR_NOTAS.upper(): __visualizar_notas,
               Strings.CMD_ALUNO.upper(): __aluno,
               Strings.CMD_PROFESSOR.upper(): __professor
               }