import pandas as pd 

df = pd.read_csv('data/tb_ubigeos.csv', dtype={'ubigeo_reniec': str}) 

print(df.columns)

"""['id_ubigeo', 'ubigeo_reniec', '2', '3',
       'departamento', '5', 'provincia', 'distrito', '8',
       '9', '10', '11', '12',
       '13', '14', 'latitud', 'longitud']"""

df = df.drop(df.columns[[2, 3, 5, 8, 9, 10, 11, 12, 13, 14]], axis=1) 

df.to_csv('data/ubigeo.csv', index=False)

if len(df.columns) >= 0:
       print()