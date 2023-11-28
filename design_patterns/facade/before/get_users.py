import sqlite3
import pyodbc

CONNSTR = (
    "..\\..\\..\\dao\\app.db"
)

def get_users():
    connection = pyodbc.connect(CONNSTR)
    query = '''
        SELECT name, email
        FROM users
        ORDER BY name;
    '''
    cursor = connection.cursor()
    cursor.execute(query)
    for row in cursor:
        print(row[0], row[1])
    connection.commit()
    connection.close()

get_users()