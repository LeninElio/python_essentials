import pandas as pd
from bd import Connection

connect = Connection()

query = '''SELECT p.id, p.primer_apellido, p.segundo_apellido, p.nombres, 
           p.comentario FROM padron AS p LIMIT 200'''

# cursor = connect.cursor()
# cursor.execute(query)
# data = cursor.fetchall()

# for i in data:
#     print(i)

data = pd.read_sql_query(query, con=connect)
# print(data)

data.to_excel('excel_mysql/Datos.xlsx', index=False)

connect.close()