from mysql import connector

def Connection():
    connect = None

    config = {
        'user': 'root',
        'password': '',
        'host': 'localhost',
        'database': 'pension',
        'raise_on_warnings': True
    }

    try:
        connect = connector.connect(**config)
        return connect
    except:
        print('Error en la conexion.')