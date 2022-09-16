from mysql.connector import Error
from mysql import connector

def Connection():
    config = {
        'user': 'root',
        'password': '',
        'host': 'localhost',
        'database': 'pension',
        'raise_on_warnings': True
    }

    connect = None

    try:
        connect = connector.connect(**config)
        # if connect.is_connected():
        #     print('Conectado...')
        return connect
    except Error as e:
        print('Fallo en la conexion', e)
