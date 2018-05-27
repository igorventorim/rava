import json

import requests

from messenger import answer_view_templates
from virtual_class.model.domain.answer import Answer
from virtual_class.model.domain.course import Course
from virtual_class.model.domain.object import Object
from virtual_class.model.domain.question import Question
from virtual_class.model.domain.student import Student
from virtual_class.model.domain.teatcher import Teatcher
from virtual_class.model.domain.courseStudent import CourseStudent
from virtual_class.model.domain.simulado import Simulado
from utils.my_encoder import MyEncoder
from utils.strings import Strings
from messenger.user_data import UserData
import random
# from app import db
from config.configuration import Configuration
class VirtualClassService:


    def __init__(self):
        self.cursos = []   #TODO: CHANGE DICT COURSES
        self.alunos = {}

    # V1.0 - OK
    def __started(self,message):
        user_id = message.getClientID()
        msgText = Strings.GREETING_KNOWN_USER.format(UserData().getFirstNameClient(user_id))
        data = answer_view_templates.text(user_id, msgText)
        MessengerService.sendMessage(data)
        msgText = Strings.APRESENTATION
        data = answer_view_templates.quick_reply(user_id, msgText, [Strings.PROFESSOR, Strings.ALUNO])
        MessengerService.sendMessage(data)

    # V1.0 - OK
    def __help(self,message):
        user_id = message.getClientID()
        data = answer_view_templates.text(user_id, Strings.HELP_INFO_PROFESSOR)
        MessengerService.sendMessage(data)
        data = answer_view_templates.text(user_id, Strings.HELP_INFO_ALUNO)
        MessengerService.sendMessage(data)

    # V1.0 - OK
    def __professor(self,message):
        user_id = message.getClientID()
        data = answer_view_templates.text(user_id, Strings.PROFESSOR_INFO)
        MessengerService.sendMessage(data)

    # V1.0 - OK
    def __aluno(self,message):
        user_id = message.getClientID()
        data = answer_view_templates.text(user_id, Strings.ALUNO_INFO)
        MessengerService.sendMessage(data)



    # V1.0 - OK
    def __criar_curso(self,message):
        content_message = message.getContentMessage()
        user_id = message.getClientID()
        course_name = content_message[content_message.find("curso")+len("curso")+1:]
        teatcher = Teatcher(teatcher_id=user_id)
        check = Teatcher.query.filter_by(id=user_id).first()
        if check is None:
            Configuration.db.session.add(teatcher)
            Configuration.db.session.commit()
        course = Course(name=course_name, teatcher_id=user_id)
        self.cursos.append(course)
        Configuration.db.session.add(course)
        Configuration.db.session.commit()
        # print(self.__cursos)
        data = answer_view_templates.text(user_id, "Voce criou o curso " + course_name + ", seu código de curso é " + str(course.getCode()))
        MessengerService.sendMessage(data)

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
                Configuration.db.session.add(question)
                Configuration.db.session.commit()
                data = answer_view_templates.text(user_id, "Questão criada com sucesso. Question code: " + str(question.getCode()))
                MessengerService.sendMessage(data)
                self.__info_nova_atividade(course_id)
            else:
                data = answer_view_templates.text(user_id, "Você não está autorizado a cadastrar questões neste curso!")
                MessengerService.sendMessage(data)
        else:
            data = answer_view_templates.text(user_id, "Código de curso inválido, confira se informou o código corretamente")
            MessengerService.sendMessage(data)

    # V1.0 - OK
    def __listar_cursos(self,message):
        content_message = message.getContentMessage()
        user_id = message.getClientID()
        courses_list = Course.listCourses(self.cursos, user_id)[1]
        courses_list = self.coursesToStr(Course.query.filter_by(teatcher_id=user_id).all())
        msg = courses_list if len(courses_list) else "Desculpe, mas você não possui curso cadastrado!"
        data = answer_view_templates.text(user_id, "Seus cursos são :\n" + msg)
        MessengerService.sendMessage(data)

    # V1.0 - OK
    def __listar_atividades(self,message):
        content_message = message.getContentMessage()
        user_id = message.getClientID()
        # courses_list = self.coursesToStr(Course.query.filter_by(teatcher_id=user_id).all())
        courses_list = Course.query.filter_by(teatcher_id=user_id).all()
        if( len(courses_list) > 0):
            for course in courses_list:
                questions = course.getQuestionsToString() if course.getQuestionsToString() != "" else "Este curso ainda não possui atividades cadastradas."
                data = answer_view_templates.text(user_id, "Atividades do curso " + str(course.getName()) + "\n" + questions)
                MessengerService.sendMessage(data)
        else:
            data = answer_view_templates.text(user_id, "Você não possui nenhum curso cadastrado, por isso não pode ter nenhuma questão cadastrada!")
            MessengerService.sendMessage(data)

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
                Configuration.db.session.add(student)
                Configuration.db.session.commit()

            courseStudent = CourseStudent(student_id=user_id,course_id=course.getId())
            Configuration.db.session.add(courseStudent)
            Configuration.db.session.commit()
            # course.addStudent(user_id)
            # self.__alunos.get(user_id).addCourse(course_code)
            data = answer_view_templates.text(user_id, "Bem vindo ao curso " + course.getName() + "!\nAgora você pode responder as atividades relacionadas a este curso!")
            MessengerService.sendMessage(data)
        else:
            data = answer_view_templates.text(user_id, "Código de curso inválido, confira se informou o código corretamente")
            MessengerService.sendMessage(data)

    # V1.0 - OK
    def __visualizar_atividades(self,message):
        # content_message = message.getContentMessage()
        user_id = message.getClientID()
        coursesActivate = CourseStudent.query.filter_by(student_id=user_id).all()
        if coursesActivate == []:
            data = answer_view_templates.text(user_id, "Você não está cadastrado em nenhum curso.")
            MessengerService.sendMessage(data)
        else:
            for ca in coursesActivate:
                course = Course.query.filter_by(id=ca.getCourseId()).first()
                msg = "Questões do curso: "+course.getName()+"\n"
                for question in Question.query.filter_by(course_id=course.getId()):
                    msg += question.getCode()+":"+question.getDesc()+"\n"
                data = answer_view_templates.text(user_id, msg)
                MessengerService.sendMessage(data)
            data = answer_view_templates.text(user_id, "Para responder uma questão digite #códigodaquestão e sua resposta.\nExemplo: \nPergunta: #cc50q3 Quem descobriu o Brasil?\nResposta: #cc1q0 Pedrinho")
            MessengerService.sendMessage(data)

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
                    data = answer_view_templates.text(user_id, msg)
                    MessengerService.sendMessage(data)
            else:
                data = answer_view_templates.text(user_id, "Você não possui nenhuma resposta cadastrada.")
                MessengerService.sendMessage(data)
        else:
            data = answer_view_templates.text(user_id, "Você não está cadastrado em nenhum curso.")
            MessengerService.sendMessage(data)

    # V1.0 - OK
    def __info_nova_atividade(self,curso_id):
        for courseStudent in CourseStudent.query.filter_by(course_id=curso_id).all():
            data = answer_view_templates.text(courseStudent.getStudentId(), "Você tem uma nova atividade, para visualizar envie /tarefas")
            MessengerService.sendMessage(data)

    def info_feedback(self,answer):
        data = answer_view_templates.text(answer.getStudentId(), "Saiu a nota da atividade :" + answer.getAnswerText())

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
            data = answer_view_templates.text(user_id, "Código de curso inválido, confira se digitou o código corretamente.")
            MessengerService.sendMessage(data)
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
                    Configuration.db.session.add(answer)
                    Configuration.db.session.commit()
                    data = answer_view_templates.text(user_id, "Resposta enviada com sucesso. Você receberá uma mensagem quando sua resposta for corrigida.")
                    MessengerService.sendMessage(data)
                else:
                    data = answer_view_templates.text(user_id, "Código de questão inválido, confira se digitou o código corretamente.")
                    MessengerService.sendMessage(data)
            else:
                data = answer_view_templates.text(user_id, "Você não está cadastrado neste curso.")
                MessengerService.sendMessage(data)

    def sampleSimulation(self):
        data = answer_view_templates.text(1807409562632930,
                                          "Por favor, nos informe as notas para a seguintes respostas, informando o código do aluno e sua nota:\n\n"
                                          "QUESTÃO CC2Q0: Quais são os planetas do sistema solar?\n"
                                          "ST001: Terra, Marte, Saturno, Plutão, Júpiter, Mercúrio, Vênus, Saturno, Urano e Netuno\n"
                                          "ST002: Mercúrio, Vênus, Terra, Marte, Júpiter, Saturno, Urano e Netuno\n"
                                          "ST009: Marte, Saturno, Terra, Vênus, Saturno, Urano e Netuno\n"
                                          "ST022: Terra, Marte, Vênus, Saturno, Urano e Netuno\n"
                                          "ST311: Vênus, Saturno, Urano, Terra, Marte e Saturno\n\n"
                                          "Para informar a nota, digite #codigodoaluno nota\n"
                                          "Exemplo: #ST001 5")
        MessengerService.sendMessage(data)


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
                    obj.setIdGradeGrades(str(resposta.getId()))
                    obj.setNotaProfessor("-1.00000")
                    obj.setCourseName(curso.getName())
                    obj.setResposta(resposta.getAnswerText())
                    # obj.setFeedback()
                    # obj.setUrl()
                    pNota["facebook"][curso.getId()][atividade.getId()][resposta.getStudentId()].append(obj)

                self.removeElementVoid(pNota["facebook"][curso.getId()],atividade.getId())

            self.removeElementVoid(pNota["facebook"],curso.getId())
        return json.dumps(pNota, cls=MyEncoder)

    def generateStructToSimulado(self,user_id,element):
        pNota = {"facebook":{}}
        # for curso in Course.query.all():
        pNota["facebook"][element["curso"]] = {}
        count = 0
        for idQuestion,resposta in element["respostas"].items():
            count = count +1
            pNota["facebook"][element["curso"]][idQuestion] = {}
            if not user_id in pNota["facebook"][element["curso"]][idQuestion].keys():
                pNota["facebook"][element["curso"]][idQuestion][user_id] = []

            obj = Object()
            obj.setCourse("")
            obj.setInstanceId(str(idQuestion))
            obj.setUserId(user_id)
            obj.setContextId("")
            obj.setQuestion((Simulado.query.filter_by(id=idQuestion).first().getQuestao()))
            obj.setItemId(str(count))
            obj.setFileName("facebook")
            obj.setRawGradeMin("0.00000")
            obj.setRawGradeMax("100.00000")
            obj.setIdGradeGrades(str(count))
            obj.setNotaProfessor("-1.00000")
            obj.setCourseName(element["curso"])
            obj.setResposta(resposta)
            # obj.setFeedback()
            # obj.setUrl()
            pNota["facebook"][element["curso"]][idQuestion][user_id].append(obj)

            self.removeElementVoid(pNota["facebook"][element["curso"]],idQuestion)

            self.removeElementVoid(pNota["facebook"],element["curso"])
        return json.dumps(pNota, cls=MyEncoder)


    def removeElementVoid(self,dict,key):
        if not bool(dict[key]):
            dict.pop(key)

    def __simulado(self,message):
        redis = Configuration.redis
        user_id = message.getClientID()
        if not redis.existsUserOn(user_id):
            struct = {}
            struct["curso"] = None
            redis.setKey(user_id,struct)
            redis.setExpire(user_id,14400)
            data = answer_view_templates.text(user_id,"Você poderia me informar de qual matéria você deseja responder o simulado? (Caso não queira mais fazer, digite: sair)")
            MessengerService.sendMessage(message,data)
        elif message.getContentMessage().upper() == "SAIR":
            data = answer_view_templates.text(user_id,"É para já, deixa o simulado para outra hora.")
            MessengerService.sendMessage(message,data)
            redis.delete(user_id)
        elif redis.getValue(user_id)["curso"] == None:
            list = Simulado.query.filter_by(conteudo=message.getContentMessage().lower()).all()
            if list == []:
                data = answer_view_templates.text(user_id,"Não tenho simulado da matéria "+message.getContentMessage()+" na minha base de dados, você poderia informar outra? (Caso não queira mais fazer, digite: sair)")
                MessengerService.sendMessage(message,data)
            else:
                struct = redis.getValue(user_id)
                struct["curso"] = message.getContentMessage()
                struct["respostas"] = {}
                question = random.choice(list)
                struct["respostas"][str(question.getId())] = None
                redis.setKey(user_id,struct)
                data = answer_view_templates.text(user_id,question.getQuestao())
                MessengerService.sendMessage(message,data)
        elif len(redis.getValue(user_id)["respostas"]) < 5 :
            struct = redis.getValue(user_id)
            list = Simulado.query.filter_by(conteudo=struct["curso"].lower()).all()
            respostas = struct["respostas"]
            for key, value in respostas.items():
                if value == None:
                    respostas[key] = message.getContentMessage()
                    break
            question = random.choice(list)

            while str(question.getId()) in struct["respostas"].keys():
                question = random.choice(list)

            respostas[question.getId()] = None
            struct["respostas"] = respostas
            redis.setKey(user_id, struct)
            data = answer_view_templates.text(user_id, question.getQuestao())
            MessengerService.sendMessage(message,data)
        else:
            struct = redis.getValue(user_id)
            respostas = struct["respostas"]
            for key, value in respostas.items():
                if value == None:
                    respostas[key] = message.getContentMessage()
                    break
            redis.delete(user_id)
            data = answer_view_templates.text(user_id,"Corrigindo...")
            MessengerService.sendMessage(message,data)
            struct_plugin = self.generateStructToSimulado(user_id,struct)
            respostaPlugin = self.requestPlugin(struct_plugin)
            data = answer_view_templates.text(user_id, "Nota :"+str(respostaPlugin['nota']))
            MessengerService.sendMessage(message,data)


    def requestPlugin(self,data):
        HEADERS = {"Content-Type": "application/json"}
        r = requests.post("http://35.230.6.53:8080/execute", headers=HEADERS, data=data)
        if r.status_code != 200:
            return json.loads(r.text)
        else:
            return "Não foi possível calcular a sua nota."

    options = {Strings.GET_STARTED.upper(): __started,
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
               Strings.CMD_PROFESSOR.upper(): __professor,
               Strings.CMD_SIMULADO.upper():__simulado
               }


    def coursesToStr(self,cursos):
        list = ""
        for course in cursos:
                list += str(course.getCode()) + ":" + course.getName() + "\n"
        return list

    def updateAnswers(self,data):
        for response in data:
            idAnswer = response["id_grade_grades"]
            nota = response["nota"]
            feedback = response["feedback"]
            answer = Answer.query.filter_by(id=idAnswer).first()
            answer.feedback = feedback
            answer.nota = nota
            Configuration.db.session.commit()
            self.info_feedback(answer)


        print("OK")
from messenger.messenger_service import MessengerService