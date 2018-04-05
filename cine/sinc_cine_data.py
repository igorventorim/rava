import requests
from bs4 import BeautifulSoup
from config.configuration import Configuration
from cine.domain.filme import Filme
from cine.domain.programacao import Programacao
import datetime

class SincCineData():


    def extract_data_cine(self):
        _URL = "http://www.cinema.ufes.br/programa-semana"
        r = requests.get(_URL)
        soup = BeautifulSoup(r.content, "html5lib")
        table_row = 0
        dict = {}
        dates = {}
        table = soup.find("table")
        if(table != None):
            for item in table.find_all("tr"):
                table_row += 1
                table_column = 0
                for cell in item.find_all("td"):
                    table_column +=1
                    movie = None
                    if(table_row == 1):
                         date = cell.find("h1").get_text().replace('\n\t\t\t\t\t','')+"/"+str(datetime.datetime.now().year)
                         day_of_week = cell.find("h3").get_text().replace('\n\t\t\t\t\t','')
                         dict[table_column] = "["+day_of_week+" - "+date+"] "
                         dates[table_column] = date
                    else:
                        title_or_hour = cell.find_all("p")
                        if len(title_or_hour) >= 2:
                            title = title_or_hour[1].get_text().replace('\n\t\t\t\t\t','')
                            hour = title_or_hour[0].get_text().replace('\n\t\t\t\t\t','')
                            movie_url = title_or_hour[1].find('a',href=True)
                            if title != None:
                                movie = self.getDataMovie(title,movie_url)

                                if movie != None and hour != None and dates[table_column] != None:
                                    check = Programacao.query.filter_by(filme_id=movie.get_id(),horario=hour,data=datetime.datetime.strptime(dates[table_column],"%d/%m/%Y")).first()
                                    if check is None:
                                        programacao = Programacao()
                                        programacao.set_horario(hour)
                                        programacao.set_filme_id(movie.get_id())
                                        programacao.set_date(datetime.datetime.strptime(dates[table_column],"%d/%m/%Y"))
                                        Configuration.db.session.add(programacao)
                                        Configuration.db.session.commit()

                        title = None
                        hour = None






    def getDataMovie(self,title,movie_url):
        sinopse = None
        classificacao = None
        if movie_url != None:
            r = requests.get(movie_url['href'])
            if r.status_code == 200:
                soup = BeautifulSoup(r.content, "html5lib")
                elements = soup.find("div", {"class": "field-item"})
                max = 0
                for p in elements.find_all("p"):
                    if max < len(p.get_text()):
                        max = len(p.get_text())
                        sinopse = p.get_text()
                    if "classi" in p.get_text().lower():
                        classificacao = p.get_text().lower()[p.get_text().find(':')+1:]

        check = Filme.query.filter_by(titulo=title.lower()).first()
        if check is None:
            filme = Filme()
            filme.set_titulo(title.lower())
            filme.set_sinopse(sinopse)
            filme.set_classificacao(classificacao)
            Configuration.db.session.add(filme)
            Configuration.db.session.commit()
            return filme
        else:
            return check