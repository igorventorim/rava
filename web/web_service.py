from config.configuration import Configuration
from virtual_class.model.domain.simulado import Simulado
import json

class WebService:

    def __init__(self):
        pass


    def register_simulado(self,list,test_name,teacher):
        simulado = Simulado.query.filter_by(conteudo=test_name).first()
        if(simulado != None):
            return "Erro: Já possui um simulado cadastrado com este nome!"
        column_error = 0
        list.pop(0)
        for line in list:
            element = str(line, 'utf-8').split(';')
            if (len(element) != 2):
                column_error = column_error + 1
                continue
            else:
                simulado =  Simulado(questao=element[0],resposta=element[1],curso=test_name)
                Configuration.db.session.add(simulado)
        Configuration.db.session.commit()
        if (column_error > 0):
            return "Foi encontrado " + str(
                column_error) + " linha(s) com colunas diferentes de 2., porém o simulado foi cadastrado sem essas perguntas."
        return 'Simulado cadastrado com sucesso!'

    def getSimulado(self, test_name):
        simulado = Simulado.query.filter_by(conteudo=test_name)
        data = {test_name:[]}
        for item in simulado:
            elements = {}
            elements['id'] = item.getId()
            elements['questao'] = item.getQuestao()
            elements['resposta'] = item.getResposta()
            data[test_name].append(elements)
        return json.dumps(data)