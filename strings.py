# encoding: utf-8

# teste git
class Strings():

    REQUEST_RETRY = u"Desculpe, nao entendi o que disse. Poderia tentar novamente ?"
    TYPE_OBS = u"Digite sua observacao:"
    YES = u"Sim"
    NO = u"Nao"
    GREETING_TEXT = u"Seja bem vindo ao rava !"
    GREETING_KNOWN_USER = u"Ola, {}"
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



    # CONFIG MESSENGER PROFILE
    GET_STARTED = u"START_BOT"
    # GREETING must be UTF-8 and has a 160 character limit.
    GREETING = u"Robô de Auxílio Virtual ao Aprendizado!" # TEXT: Texto a ser exibido no cumprimento, exemplo de cumprimento "text":"Hello {{user_first_name}}!"
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
    APOLOGIZE_USER_FOR_ERROR = u"Desculpe, algo deu errado, inicie novamente."

    # TO DO
    @staticmethod 
    def cmp(string_one,string_two):  # compara semanticamente. Nao pode ser: NAo, n, nao. Sim pode ser: S, s, sim, aham, claro, etc
        if type(string_one) == str or type(string_two) == str:
            raise TypeError("Strings must be type of unicode not str.")
        return string_one.lower() == string_two.lower()
