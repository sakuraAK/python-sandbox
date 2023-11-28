import sqlite3
from .facade import AbsFacade
from . import CONNSTR, QUERY

class GetEmployeesFacade(AbsFacade):
    def get_users(self):
        connection = sqlite3.connect(CONNSTR)
        cursor = connection.cursor()
        cursor.execute(QUERY)
        for row in cursor:
            print(row[0], row[1])
        connection.commit()
        connection.close()
