# Classe responsavel pela conexao com o Banco de Dados

import psycopg2
import psycopg2.extras

class Connection:

    def __init__(self,db,usr,pwd,hst,prt):
        self.__conn = None
        self.__database=db
        self.__user=usr
        self.__password=pwd
        self.__host=hst
        self.__port=prt
        self.open()

    #Try open connection with database
    def open(self):
        try:
            self.__conn = psycopg2.connect(database=self.__database, user=self.__user, password=self.__password,
                                           host=self.__host, port=self.__port)
        except Exception as error:
            print("Erro: ", error)

    #Restart connection with database
    def restart(self):
        self.close()
        self.open()

    # Close connection with database
    def close(self):
        self.__conn.cursor.close()
        self.__conn.close()
        self.__conn = None

    # Will return a cursor object. You can use this cursor to perform queries PostgreSQL
    def getCursorSQL(self):
        return self.__conn.cursor()

    # Will return a cursor object. You can use this cursor to perform queries PostgreSQL
    # Dictionary cursor so COLUMNS will be returned as a dictionary so can access columns
    # by their name instead of index.
    def getCursor(self):
        return self.__conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    # Check database connection
    def isConnected(self):
        return not self.__conn is None

    def commit(self):
        self.__conn.commit()