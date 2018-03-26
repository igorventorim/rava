# encoding: utf-8

# teste git
class Strings():

    REQUEST_RETRY = u"Desculpe, nao entendi o que disse. Poderia tentar novamente ?"
    TYPE_OBS = u"Digite sua observacao:"
    YES = u"Sim"
    NO = u"Nao"
    GREETING_TEXT = u"Seja bem vindo ao rava !"
    GREETING_KNOWN_USER = u"Olá {}, tudo bem?"
    APRESENTATION= "Eu sou o Robô de Auxílio Virtual e Aprendizado, para os mais íntimos rAVA.\n" \
                   "Hoje eu tenho informações do restaurante universitário da Universidade Federal do Espírito Santo, se você quiser informações me pergunte :)"

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
    CMD_CRIAR_CURSO="criar_curso"
    CMD_CRIAR_ATIVIDADE="/atividade"
    CMD_LISTAR_CURSOS="/listcursos"
    CMD_LISTAR_ATIVIDADES="/listatividades"
    CMD_LOGIN_CURSO="/cadastrar"
    CMD_VISUALIZAR_ATIVIDADES="/tarefas"
    CMD_VISUALIZAR_NOTAS="/notas"
    CMD_PROFESSOR="/professor"
    CMD_ALUNO="/aluno"

    CMD_PERGUNTA_SAUDACAO="pergunta_saudacao"
    CMD_AGRADECIMENTO="agradecimento"
    CMD_APRESENTACAO="cmd_apresentacao"
    CMD_SAUDACAO="cmd_saudacao"
    CMD_DESPEDIDA="cmd_despedida"
    CMD_IDADE="cmd_idade"

    CMD_PRATO = "cmd_prato"
    CMD_CARDAPIO = "cmd_cardapio"
    CMD_SPAM_RU = "cmd_spam_ru"
    CMD_DELETE_SPAM_RU = "cmd_delete_spam_ru"
    CMD_SPAM_RU_REGISTERED = "Uai, você já está recebendo minhas mensagens!"

    HELP_INFO_PROFESSOR = "Para uma melhor comunicação, definimos um dialeto a ser utilizado. Basta utilizar o comando que desta forma conseguirei compreender o que você quer fazer, veja:\n\n" \
                "Comandos para Professor:\n" \
                "/curso nomedocurso    - Cadastrar um novo curso. \n" \
                "exemplo: /curso cálculo 1\n\n" \
                "/atividade codcurso descricao    - Cadastra uma nova atividade a um curso." \
                "exemplo: /atividade cal01 Qual é a derivada de 2x? \n\n" \
                "/listcursos    - Lista os cursos criados por você.\n\n" \
                "/listatividades    - Lista a suas atividades criadas que estão em aberto.\n\n" \
                "/professor    - Exibe os comandos utilizados para professores.\n\n"
    HELP_INFO_ALUNO = "Aluno:\n" \
        "/cadastrar codcurso    - Se cadastra em um curso.\n" \
        "exemplo: /cadastrar cal01\n\n" \
        "/tarefas     - Exibe as tarefas em abertos com seus códigos, para responder digite #codigodatarefa resposta. (Obs.: Substitua codigoda tarefa pelo código exibido e resposta por sua resposta)\n\n" \
        "/notas     -  Exibe notas de tarefas respondidas.\n\n" \
        "/aluno     - Exibe os comandos utilizados para alunos.\n\n" \
        "Qualquer dúvida entre em contato pelo email: xxx@ufes.br\n"

    ALUNO_INFO =  "Bem vindo, você está na área do aluno, você pode realizar os seguintes comandos:\n" \
                "/cadastrar codcurso    - Se cadastra em um curso.\n" \
                "exemplo: /cadastrar cal01\n\n" \
                "/tarefas     - Exibe as tarefas em abertos com seus códigos, para responder digite #codigodatarefa resposta. (Obs.: Substitua codigoda tarefa pelo código exibido e resposta por sua resposta)\n\n" \
                "/notas     -  Exibe notas de tarefas respondidas.\n\n" \
                "/aluno     - Exibe os comandos utilizados para alunos.\n\n" \
                "Qualquer dúvida entre em contato pelo email: xxx@ufes.br\n"

    PROFESSOR_INFO = "Bem vindo, você está na área do professor, você pode realizar os seguintes comandos:\n" \
                 "/curso nomedocurso    - Cadastrar um novo curso. \n" \
                "exemplo: /curso cálculo 1\n\n" \
                "/atividade codcurso descricao    - Cadastra uma nova atividade a um curso.\n" \
                "exemplo: /atividade cal01 Qual é a derivada de 2x? \n\n" \
                "/listcursos    - Lista os cursos criados por você.\n\n" \
                "/listatividades    - Lista a suas atividades criadas que estão em aberto.\n\n" \
                "/professor    - Exibe os comandos utilizados para professores.\n\n"\
                "Qualquer dúvida entre em contato pelo email: xxx@ufes.br\n"



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
    APOLOGIZE_USER_FOR_ERROR = "Desculpe, não entendi. Caso tenha alguma dúvida me peça ajuda!"

    response_general = {
        CMD_PERGUNTA_SAUDACAO: "Estou ótimo, obrigado por perguntar.",
        CMD_AGRADECIMENTO: "Foi um prazer poder ajudá-lo.",
        CMD_APRESENTACAO: "Eu sou o Robô de Auxílio Virtual e Aprendizado, para os mais íntimos rAVA.\n" \
                   "Hoje eu tenho informações do restaurante universitário da Universidade Federal do Espírito Santo, se você quiser informações me pergunte :)",
        CMD_SAUDACAO: "E aí {}, que bom te ver por aqui, em que eu posso te ajudar?",
        CMD_DESPEDIDA: "Até mais!",
        CMD_IDADE: "Nós robôs não comemoramos aniversário, por isso não tenho uma idade, mas se fosse para escolher uma, acho que gostaria de ter 18."
    }

    response_ru = {
        CMD_PRATO: "Ainda não descobri, quando eu descobrir eu te falo...",
        CMD_CARDAPIO: "Ainda não descobri, quando eu descobrir eu te falo...",
        CMD_SPAM_RU: "É para já, te cadastrei, a partir de agora te enviarei mensagens com o cardápio do RU Ufes todos os dias, para que você possa receber é preciso que você tenha curtido nossa página. Caso queira se descadastrar é só falar :).",
        CMD_DELETE_SPAM_RU: "Tudo bem, não te incomodarei mais com isso."
    }


    # TO DO
    @staticmethod 
    def cmp(string_one,string_two):  # compara semanticamente. Nao pode ser: NAo, n, nao. Sim pode ser: S, s, sim, aham, claro, etc
        if type(string_one) == str or type(string_two) == str:
            raise TypeError("Strings must be type of unicode not str.")
        return string_one.lower() == string_two.lower()
