import json
import psycopg2

# Lee el archivo JSON
with open('Fibrapticadetectada_3.json', 'r') as file:
    json_data = json.load(file)

# Conecta a la base de datos
conn = psycopg2.connect(database='test', user='test', password='test', host='localhost', port='5432')
cursor = conn.cursor()

# Extrae las claves del JSON para crear las columnas
column_names = list(json_data.keys())

# Crea la sentencia SQL para crear la tabla
create_table_query = f"CREATE TABLE fibra ({', '.join([f'{col} TEXT' for col in column_names])});"

# Ejecuta la sentencia SQL
cursor.execute(create_table_query)
conn.commit()

# Cierra la conexión
cursor.close()
conn.close()
