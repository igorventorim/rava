import json

from authentication import Authentication
from message import Message
import requests
import answerViewTemplates
from model.domain.answer import Answer
from model.domain.course import Course
from model.domain.object import Object
from model.domain.question import Question
from model.domain.student import Student
from model.domain.teatcher import Teatcher
from model.domain.courseStudent import CourseStudent
from myEncoder import MyEncoder
from strings import Strings
from userData import UserData
from route import db

class RequestController:


    def __init__(self):
        self.__PARAMS = {"access_token": Authentication.PAGE_ACCESS_TOKEN}
        self.__HEADERS = {"Content-Type": "application/json"}
        self.__cursos = []   #TODO: CHANGE DICT COURSES
        self.__alunos = {}

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

    # V1.0 - OK
    def __criar_curso(self,message):
        content_message = message.getContentMessage()
        user_id = message.getClientID()
        course_name = content_message[content_message.find(" ")+1:]
        teatcher = Teatcher(teatcher_id=user_id)
        check = Teatcher.query.filter_by(id=user_id).first()
        if check is None:
            db.session.add(teatcher)
            db.session.commit()
        course = Course(name=course_name, teatcher_id=user_id)
        self.__cursos.append(course)
        db.session.add(course)
        db.session.commit()
        # print(self.__cursos)
        data = answerViewTemplates.text(user_id, "Voce criou o curso "+course_name+", seu código de curso é "+str(course.getCode()))
        self.__sendMessage(data)

    # V1.0 - OK
    def __criar_atividade(self,message):
        # content_message = message.getContentMessage()
        user_id = message.getClientID()
        split = message.getContentMessage().split(' ',2)
        # course = Course.getCurso(self.__cursos,split[1])
        course = Course.query.filter_by(course_code=split[1].upper()).first()
        if course != None:
            if str(course.getTeatcher()) == str(user_id):
                course_id = course.getId()
                questionNumber = len(Question.query.filter_by(course_id=course_id).all()) + 1   # VAI DAR PAU, PENSAR EM LÓGICA MELHOR
                # questionNumber = Question.query.filter_by(course_id=course_id).count() + 1
                question = Question(course.getCode()+"Q"+str(questionNumber),split[2],course_id)
                # course.addQuestion(question)
                db.session.add(question)
                db.session.commit()
                data = answerViewTemplates.text(user_id, "Questão criada com sucesso. Question code: "+str(question.getCode()))
                self.__sendMessage(data)
                self.__info_nova_atividade(course_id)
            else:
                data = answerViewTemplates.text(user_id,"Você não está autorizado a cadastrar questões neste curso!")
                self.__sendMessage(data)
        else:
            data = answerViewTemplates.text(user_id,"Código de curso inválido, confira se informou o código corretamente")
            self.__sendMessage(data)

    # V1.0 - OK
    def __listar_cursos(self,message):
        content_message = message.getContentMessage()
        user_id = message.getClientID()
        courses_list = Course.listCourses(self.__cursos,user_id)[1]
        courses_list = self.coursesToStr(Course.query.filter_by(teatcher_id=user_id).all())
        msg = courses_list if len(courses_list) else "Desculpe, mas você não possui curso cadastrado!"
        data = answerViewTemplates.text(user_id, "Seus cursos são :\n"+msg)
        self.__sendMessage(data)

    # V1.0 - OK
    def __listar_atividades(self,message):
        content_message = message.getContentMessage()
        user_id = message.getClientID()
        # courses_list = self.coursesToStr(Course.query.filter_by(teatcher_id=user_id).all())
        courses_list = Course.query.filter_by(teatcher_id=user_id).all()
        if( len(courses_list) > 0):
            for course in courses_list:
                questions = course.getQuestionsToString() if course.getQuestionsToString() != "" else "Este curso ainda não possui atividades cadastradas."
                data = answerViewTemplates.text(user_id, "Atividades do curso "+str(course.getName())+"\n"+questions)
                self.__sendMessage(data)
        else:
            data = answerViewTemplates.text(user_id, "Você não possui nenhum curso cadastrado, por isso não pode ter nenhuma questão cadastrada!")
            self.__sendMessage(data)

    # V1.0 - OK
    def __login_curso(self,message):
        content_message = message.getContentMessage()
        user_id = message.getClientID()
        course_code = content_message[content_message.find(" ")+1:]
        # course = Course.getCurso(self.__cursos,course_code)
        course = Course.query.filter_by(course_code=course_code.upper()).first()
        if course != None:
            student = Student.query.filter_by(id=user_id).first()
            if student == None:
                student = Student(user_id)
                # self.__alunos[user_id] = student
                db.session.add(student)
                db.session.commit()

            courseStudent = CourseStudent(student_id=user_id,course_id=course.getId())
            db.session.add(courseStudent)
            db.session.commit()
            # course.addStudent(user_id)
            # self.__alunos.get(user_id).addCourse(course_code)
            data = answerViewTemplates.text(user_id, "Bem vindo ao curso "+course.getName()+"!\nAgora você pode responder as atividades relacionadas a este curso!")
            self.__sendMessage(data)
        else:
            data = answerViewTemplates.text(user_id,"Código de curso inválido, confira se informou o código corretamente")
            self.__sendMessage(data)

    # V1.0 - OK
    def __visualizar_atividades(self,message):
        # content_message = message.getContentMessage()
        user_id = message.getClientID()
        coursesActivate = CourseStudent.query.filter_by(student_id=user_id).all()
        if coursesActivate == []:
            data = answerViewTemplates.text(user_id, "Você não está cadastrado em nenhum curso.")
            self.__sendMessage(data)
        else:
            for ca in coursesActivate:
                course = Course.query.filter_by(id=ca.getCourseId()).first()
                msg = "Questões do curso: "+course.getName()+"\n"
                for question in Question.query.filter_by(course_id=course.getId()):
                    msg += question.getCode()+":"+question.getDesc()+"\n"
                data = answerViewTemplates.text(user_id, msg)
                self.__sendMessage(data)
            data = answerViewTemplates.text(user_id,"Para responder uma questão digite #códigodaquestão e sua resposta.\nExemplo: \nPergunta: #cc50q3 Quem descobriu o Brasil?\nResposta: #cc1q0 Pedrinho")
            self.__sendMessage(data)

    # V1.0 - OK
    def __visualizar_notas(self,message):
        content_message = message.getContentMessage()
        user_id = message.getClientID()
        # student = self.__alunos.get(user_id)
        student = Student.query.filter_by(id=user_id).first()
        if student != None:
            student_answers = Answer.query.filter_by(student_id=user_id).all()
            if( len(student_answers) > 0):
                for answer in student_answers:
                    question = Question.query.filter_by(id=answer.getQuestionId()).first()
                    feedback = answer.getFeedback() if answer.getFeedback() != None else ""
                    msg = "Pergunta:"+ question.getDesc() +"\nResposta:"+answer.getAnswerText()+"\n\nNota:"+feedback
                    data = answerViewTemplates.text(user_id, msg)
                    self.__sendMessage(data)
            else:
                data = answerViewTemplates.text(user_id, "Você não possui nenhuma resposta cadastrada.")
                self.__sendMessage(data)
        else:
            data = answerViewTemplates.text(user_id, "Você não está cadastrado em nenhum curso.")
            self.__sendMessage(data)

    # V1.0 - OK
    def __info_nova_atividade(self,curso_id):
        for courseStudent in CourseStudent.query.filter_by(course_id=curso_id).all():
            data = answerViewTemplates.text(courseStudent.getStudentId(), "Você tem uma nova atividade, para visualizar envie /tarefas")
            self.__sendMessage(data)

    def info_feedback(self):
        #TODO: AFTER CORRECTION PNOTA SEND RESULTS FOR USERS
        pass

    # V1.0 - OK
    def __answer(self,message):
        content_message = message.getContentMessage()
        user_id = message.getClientID()
        course_code = content_message[1:content_message.upper().find("Q")]
        question_code = content_message[1:content_message.find(" ")].upper()
        response = content_message[content_message.find(" ")+1:]
        # course = Course.getCurso(self.__cursos,course_code)
        course = Course.query.filter_by(course_code=course_code.upper()).first()
        if course == None:
            data = answerViewTemplates.text(user_id, "Código de curso inválido, confira se digitou o código corretamente.")
            self.__sendMessage(data)
        else:
            courseStudents = CourseStudent.query.filter_by(course_id=course.getId()).all()
            studentInCourse = False
            for courseStudent in courseStudents:
                if str(courseStudent.getStudentId()) == str(user_id):
                    studentInCourse = True
                    break
            if studentInCourse:
                question = Question.query.filter_by(question_code=question_code).first()
                if question != None:
                    answer = Answer(response,user_id,question.getId())
                    # course.getQuestions().get(question_code).addAnswer(answer=answer)
                    # self.__alunos.get(user_id).registerAnswer(answer)
                    db.session.add(answer)
                    db.session.commit()
                    data = answerViewTemplates.text(user_id,"Resposta enviada com sucesso. Você receberá uma mensagem quando sua resposta for corrigida.")
                    self.__sendMessage(data)
                else:
                    data = answerViewTemplates.text(user_id,"Código de questão inválido, confira se digitou o código corretamente.")
                    self.__sendMessage(data)
            else:
                data = answerViewTemplates.text(user_id,"Você não está cadastrado neste curso.")
                self.__sendMessage(data)

    def sampleSimulation(self):
        data = answerViewTemplates.text(1807409562632930,
                                        # "Por favor, nos informe as notas para a seguintes respostas, informando o código do aluno e sua nota:\n\n"
                                        # "QUESTÃO CC2Q0: Quem descobriu o Brasil?\n"
                                        # "ST001: Pedrinho\n"
                                        # "ST002: Dom Pedro\n"
                                        # "ST009: Pedro Álvares Cabral\n"
                                        # "ST022: Pedro\n"
                                        # "ST311: Vasco da Game\n\n"
                                        # "Para informar a nota, digite #codigodoaluno nota\n"
                                        # "Exemplo: #ST001 5")
                                          "Por favor, nos informe as notas para a seguintes respostas, informando o código do aluno e sua nota:\n\n"
                                          "QUESTÃO CC2Q0: Quais são os planetas do sistema solar?\n"
                                          "ST001: Terra, Marte, Saturno, Plutão, Júpiter, Mercúrio, Vênus, Saturno, Urano e Netuno\n"
                                          "ST002: Mercúrio, Vênus, Terra, Marte, Júpiter, Saturno, Urano e Netuno\n"
                                          "ST009: Marte, Saturno, Terra, Vênus, Saturno, Urano e Netuno\n"
                                          "ST022: Terra, Marte, Vênus, Saturno, Urano e Netuno\n"
                                          "ST311: Vênus, Saturno, Urano, Terra, Marte e Saturno\n\n"
                                          "Para informar a nota, digite #codigodoaluno nota\n"
                                          "Exemplo: #ST001 5")
        self.__sendMessage(data)

    def sendMessageTest(self,message):
        data = answerViewTemplates.text(1807409562632930,message)
        self.__sendMessage(data)

    def generateStructPNota(self):
        pNota = {"facebook":{}}
        for curso in Course.query.all():
            pNota["facebook"][curso.getId()] = {}

            for atividade in Question.query.filter_by(course_id=curso.getId()).all():
                pNota["facebook"][curso.getId()][atividade.getId()] = {}

                for resposta in Answer.query.filter_by(question_id=atividade.getId()):
                    if not resposta.getStudentId() in pNota["facebook"][curso.getId()][atividade.getId()].keys():
                        pNota["facebook"][curso.getId()][atividade.getId()][resposta.getStudentId()] = []
                    obj = Object()
                    obj.setCourse(str(curso.getId()))
                    obj.setInstanceId(str(atividade.getId()))
                    obj.setUserId(str(resposta.getStudentId()))
                    obj.setContextId(str(curso.getTeatcher()))
                    obj.setQuestion(str(atividade.getDesc()))
                    obj.setItemId(str(resposta.getId()))
                    obj.setFileName("facebook")
                    obj.setRawGradeMin("0.00000")
                    obj.setRawGradeMax("100.00000")
                    obj.setIdGradeGrades("0")
                    obj.setNotaProfessor("-1.00000")
                    obj.setCourseName(curso.getName())
                    obj.setResposta(resposta.getAnswerText())
                    # obj.setFeedback()
                    # obj.setUrl()
                    pNota["facebook"][curso.getId()][atividade.getId()][resposta.getStudentId()].append(obj)

                # if not bool(pNota["facebook"][curso.getId()][atividade.getId()]):
                #     pNota["facebook"][curso.getId()].pop(atividade.getId())
                self.removeElementVoid(pNota["facebook"][curso.getId()],atividade.getId())

            # if not bool(pNota["facebook"][curso.getId()]):
            #     pNota["facebook"].pop(curso.getId())
            self.removeElementVoid(pNota["facebook"],curso.getId())
        return json.dumps(pNota, cls=MyEncoder)


    def removeElementVoid(self,dict,key):
        if not bool(dict[key]):
            dict.pop(key)


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


    def coursesToStr(self,cursos):
        list = ""
        for course in cursos:
                list += str(course.getCode()) + ":" + course.getName() + "\n"
        return list