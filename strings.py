# encoding: utf-8

# teste git
class Strings():

    REQUEST_RETRY = u"Desculpe, nao entendi o que disse. Poderia tentar novamente ?"
    TYPE_OBS = u"Digite sua observacao:"
    YES = u"Sim"
    NO = u"Nao"
    GREETING_TEXT = u"Seja bem vindo ao rava !"
    GREETING_KNOWN_USER = u"Olá {}, tudo bem?"
    APRESENTATION= "Eu sou o Robô de Auxílio Virtual ao Aprendizado, para os mais íntimos Rava.\n" \
                   "Eu auxílio o ensino virtual recebendo perguntas enviadas por professores, encaminho para os alunos e avalio suas respostas, você é um?"
    BACK = u"Voltar"
    WHAT_TO_DO_NOW = u"O que deseja fazer agora?"
    SELECT_OPTION = u"Entendiii, escolha a opcao abaixo que melhor te atende :)"
    ABOUT = u" Lorem ipsum ..."
    DATA= u"Data: "
    HORA= u"Hora: "
    SPC= u" "
    NL= u"\n"
    VOID= u""
    HASHTAG= u"#"
    CONSULTAR = u"Consultar"
    MAIS= u"+"
    MORE = u"Mais"
    OK = u"Ok"
    WAIT_TIME = u"Tempo de espera aproximado: {} minutos."

    PROFESSOR="Professor"
    ALUNO="Aluno"
    CRIAR_CURSO="/curso"
    CRIAR_ATIVIDADE="/atividade"
    LISTAR_CURSOS="/listcursos"
    LISTAR_ATIVIDADES="/listatividades"
    LOGIN_CURSO="/cadastrar"
    VISUALIZAR_ATIVIDADES="/tarefas"
    VISUALIZAR_NOTAS="/notas"

    HELP_INFO_PROFESSOR = "Para uma melhor comunicação, definimos um dialeto a ser utilizado. Basta utilizar o comando que desta forma conseguirei compreender o que você quer fazer, veja:\n\n" \
                "Comandos para Professor:\n" \
                "/curso nomedocurso - Substitua nomedocurso pelo curso que você deseja criar.\n\n" \
                "/atividade codcurso desc - Substitua codcurso pelo codigo do curso que foi criado e desc pela pergunta desejada.\n\n" \
                "/listcursos - Informa a lista de curso com seus códigos já criada pelo usuário.\n\n" \
                "/listatividades - Informa a lista de atividades em aberto já criadas.\n\n"
    HELP_INFO_ALUNO = "Aluno:\n" \
                "/cadastrar codcurso - Substitua codcurso pelo codigo do curso que se deseja cadastrar.\n\n" \
                "/tarefas - Exibe as tarefas em abertos com seus códigos, para responder digite #codigodatarefa resposta. (Obs.: Substitua codigoda tarefa pelo código exibido e resposta por sua resposta)\n\n" \
                "/notas -  Exibe notas de tarefas respondidas.\n\n" \
                "Qualquer dúvida entre em contato pelo email: xxx@ufes.br\n"

    ALUNO_INFO =  "Bem vindo, você está na área do aluno, você pode realizar os seguintes comandos:\n" \
                "/cadastrar codcurso - Substitua codcurso pelo codigo do curso que se deseja cadastrar.\n\n" \
                "/tarefas - Exibe as tarefas em abertos com seus códigos, para responder digite #codigodatarefa resposta. (Obs.: Substitua codigoda tarefa pelo código exibido e resposta por sua resposta)\n\n" \
                "/notas -  Exibe notas de tarefas respondidas.\n\n" \
                "Qualquer dúvida entre em contato pelo email: xxx@ufes.br\n"

    PROFESSOR_INFO = "Bem vindo, você está na área do professor, você pode realizar os seguintes comandos:\n" \
                "/curso nomedocurso - Substitua nomedocurso pelo curso que você deseja criar.\n\n" \
                "/atividade codcurso desc - Substitua codcurso pelo codigo do curso que foi criado e desc pela pergunta desejada.\n\n" \
                "/listcursos - Informa a lista de curso com seus códigos já criada pelo usuário.\n\n" \
                "/listatividades - Informa a lista de atividades em aberto já criadas.\n\n" \



    #Commands
    HELP="/help"



    # CONFIG MESSENGER PROFILE
    GET_STARTED = u"START_BOT"
    # GREETING must be UTF-8 and has a 160 character limit.
    GREETING = "Robô de Auxílio Virtual ao Aprendizado!" # TEXT: Texto a ser exibido no cumprimento, exemplo de cumprimento "text":"Hello {{user_first_name}}!"
    WHITELIST= u"[]" # list: A list of domains being used. All domains must be valid. Up to 10 domains allowed.
    URL_PAYMENT_POLICY_PRIVACY = u"" # SET URL PAYMENT POLICY PRIVACY
    PUBLIC_KEY = u"" # SET PUBLIC KEY
    ACCOUNT_LINKING_URL = u"" # SET ACCOUNT LINKING URL - example "https://www.example.com/oauth?response_type=code&client_id=1234567890&scope=basic"

    EXIT = u"Sair"

    NUMBER1= u"1"
    NUMBER2= u"2"
    NUMBER3= u"3"
    NUMBER4= u"4"
    NUMBER5= u"5"
    # except things
    APOLOGIZE_USER_FOR_ERROR = "Desculpe, não entendi. Caso tenha dúvida em quais comandos utilizar digite: /help"

    # TO DO
    @staticmethod 
    def cmp(string_one,string_two):  # compara semanticamente. Nao pode ser: NAo, n, nao. Sim pode ser: S, s, sim, aham, claro, etc
        if type(string_one) == str or type(string_two) == str:
            raise TypeError("Strings must be type of unicode not str.")
        return string_one.lower() == string_two.lower()
