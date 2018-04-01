import requests
from bs4 import BeautifulSoup

class SincCineData():

    def __init__(self):
        pass

    def extract_data_cine(self):
        _URL = "http://www.cinema.ufes.br/programa-semana"
        r = requests.get(_URL)
        soup = BeautifulSoup(r.content, "html5lib")
        table_row = 0
        dict = {}
        table = soup.find("table")
        if(table != None):
            for item in table.find_all("tr"):
                table_row += 1
                table_column = 0
                for cell in item.find_all("td"):
                    table_column +=1
                    if(table_row == 1):
                         date = cell.find("h1").get_text().replace('\n\t\t\t\t\t','')
                         day_of_week = cell.find("h3").get_text().replace('\n\t\t\t\t\t','')
                         dict[table_column] = "["+day_of_week+" - "+date+"] "
                    else:
                        title_or_hour = cell.find_all("p")
                        if len(title_or_hour) >= 2 :
                            title = title_or_hour[1].get_text().replace('\n\t\t\t\t\t','')
                            hour = title_or_hour[0].get_text().replace('\n\t\t\t\t\t','')

                        if title != None and hour != None:
                            print(dict[table_column] + title + " : "+hour)
                        title = None
                        hour = None

        #TODO: CONTINUAR ALGORITMO DE EXTRAÇÃO!!!
        pass