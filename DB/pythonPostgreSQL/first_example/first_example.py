import psycopg2

# Global Constant
PSQL_HOST = "localhost"
PSQL_PORT = "5432"
PSQL_USER = "postgres"
PSQL_PASS = "12345"
PSQL_DB   = "testpython"

# Connection
connstr = "host=%s port=%s user=%s password=%s dbname=%s" % (PSQL_HOST, PSQL_PORT, PSQL_USER, PSQL_PASS, PSQL_DB)
conn = psycopg2.connect(connstr)

# Abrir un cursor para realizar operaciones sobre la base de datos
cur = conn.cursor()

# Ejecutar una consulta SELECT
sqlquery = "SELECT * FROM Prueba"
cur.execute(sqlquery)

# Obtener los resultados como objetos Python
one_values = cur.fetchone()
all_values = cur.fetchall()

# Cerrar la conexión con la base de datos
cur.close()
conn.close()

# Hacer algo con los datos
print('Get values with fetchone: ', one_values)
print('Get values with fetchall: ', all_values)