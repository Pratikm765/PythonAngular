import mysql.connector

class Database:
    def __init__(self):
        self.__connection= mysql.connector.connect(host='localhost'
                                                   ,user='root',
                                                   password='Pm@9867600493',
                                                   port='3306',
                                                   database='tempDB'
                                                   )
        self.__cursor=self.__connection.cursor()

    def __del__(self):
        self.__connection.close()
        self.__cursor.close()

    def select(self,statement):
        self.__cursor.execute(statement)
        return self.__cursor.fetchall()

    def selectone(self,statement):
        self.__cursor.execute(statement)
        return self.__cursor.fetchone()

    def execute(self,statement):
        self.__cursor.execute(statement)
        self.__connection.commit()