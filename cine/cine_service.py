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
                programacoes = Programacao.query.filter_by(data=datenow.date()).order_by(Programacao.data.asc())
            elif type == "week":
                programacoes = Programacao.query.filter(
                    Programacao.data.between(datenow.date(), datenow.date() + datetime.timedelta(days=7))).order_by(Programacao.data.asc())
            elif type == "month":
                programacoes = Programacao.query.filter(
                    Programacao.data.between(datenow.date(), datenow.date() + datetime.timedelta(days=30))).order_by(Programacao.data.asc())
            elif type == "year":
                programacoes = Programacao.query.filter(
                    Programacao.data.between(datenow.date(), datenow.date() + datetime.timedelta(days=365))).order_by(Programacao.data.asc())
        else:
            weekday = datetime.datetime.today().weekday()
            if weekday < 3:
                weekday = -4 - weekday
            else:
                weekday = 3 - weekday
            programacoes = Programacao.query.filter(
                Programacao.data.between(datetime.datetime.now().date()+ datetime.timedelta(days=weekday), datetime.datetime.now().date()+ datetime.timedelta(days=weekday)+ datetime.timedelta(days=6))).order_by(Programacao.data.asc())
        msg = ""
        for programacao in programacoes:
            msg += str(programacao.get_filme().get_titulo()) + "\n"
            msg += str(programacao.get_date())+" - " + str(programacao.get_horario())+"\n\n"

        data = answer_view_templates.text(user_id, msg)
        MessengerService.sendMessage(message, data)



    options = {Strings.CMD_PROGRAMACAO.upper(): getProgramacao}

from messenger.messenger_service import MessengerService
