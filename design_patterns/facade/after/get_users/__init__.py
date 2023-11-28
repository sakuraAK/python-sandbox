PROVIDER = 'sqllite'

CONNSTR = (
    "..\\..\\..\\dao\\app.db"
)

QUERY = '''
    SELECT name, email 
    FROM users
    ORDER BY name;
'''
