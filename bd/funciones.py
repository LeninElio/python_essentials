from bd import Connection

connect = Connection()

def crear_tabla(query):
    cursor = connect.cursor()
    try:
        cursor.execute(query)
    except:
        print('Error en la creacion de la tabla.')
    cursor.close()


def eliminar_tabla(nombre_tabla):
    cursor = connect.cursor()
    try:
        cursor.execute(f'DROP TABLE {nombre_tabla}')
    except:
        print('Error en la eliminacion la tabla.')
    cursor.close()


def insertar_datos(query):
    cursor = connect.cursor()
    try:
        cursor.execute(query)
        connect.commit()
    except:
        print('Error en la insersion de datos.')
        connect.rollback()
    cursor.close()

def actualizar_datos(query):
    cursor = connect.cursor()
    try:
        cursor.execute(query)
        # connect.commit()
    except:
        print('Error en la actualizacion de datos.')
        connect.rollback()
    cursor.close()

def eliminar_datos(id):
    cursor = connect.cursor()
    try:
        cursor.execute(f'DELETE FROM usuario WHERE id={id}')
        # connect.commit()
    except:
        print('Error en la eliminacion de datos.')
        connect.rollback()
    cursor.close()
