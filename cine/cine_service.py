from utils.strings import Strings
from messenger import answer_view_templates
import datetime
from config.configuration import Configuration
from cine.domain.programacao import Programacao
from cine.domain.filme import Filme

class CineService:

    def __init__(self):
        pass


    def getProgramacao(self,message):
        user_id = message.getClientID()
        if 'datetime' in message.getEntities():
            datenow = datetime.datetime.strptime(message.getEntities()['datetime'][0]['value'][:10], "%Y-%m-%d")
            type = message.getEntities()['datetime'][0]['grain']
            if type == "day":
                programacoes = Programacao.query.filter_by(data=datenow.date())
            elif type == "week":
                programacoes = Programacao.query.filter(
                    Programacao.data.between(datenow.date(), datenow.date() + datetime.timedelta(days=7)))
            elif type == "month":
                programacoes = Programacao.query.filter(
                    Programacao.data.between(datenow.date(), datenow.date() + datetime.timedelta(days=30)))
            elif type == "year":
                programacoes = Programacao.query.filter(
                    Programacao.data.between(datenow.date(), datenow.date() + datetime.timedelta(days=365)))
        else:
            weekday = datetime.datetime.today().weekday()
            if weekday < 3:
                weekday = -4 - weekday
            else:
                weekday = 3 - weekday
            programacoes = Programacao.query.filter(
                Programacao.data.between(datetime.datetime.now().date()+ datetime.timedelta(days=weekday), datetime.datetime.now().date()+ datetime.timedelta(days=weekday)+ datetime.timedelta(days=6)))



            for programacao in programacoes:
                print("Filme")
                print(programacao.get_date())
                print(programacao.get_horario())
                print(programacao.get_filme())
                print("====================================")



    options = {Strings.CMD_PROGRAMACAO.upper(): getProgramacao}