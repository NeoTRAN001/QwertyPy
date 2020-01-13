import psycopg2

class DataAccess():
    # Global Constant
    PSQL_HOST = "localhost"
    PSQL_PORT = "5432"
    PSQL_USER = "postgres"
    PSQL_PASS = "12345"
    PSQL_DB   = "testpython"

    # Default: Class contructor
    def __init__(self):
        # Connection
        self.connection_str = "host=%s port=%s user=%s password=%s dbname=%s" % (self.PSQL_HOST, self.PSQL_PORT, self.PSQL_USER, self.PSQL_PASS, self.PSQL_DB)
        
        self.connection = psycopg2.connect(self.connection_str)
    # Method: 
    def get_query(self, query, parameters = None):
        cursor = self.connection.cursor()

        if parameters != None:
            cursor.execute(query, parameters)
        else:
            cursor.execute(query)

        values = cursor.fetchall()

        cursor.close()
        self.connection.close()

        return values

    def execute_query(self, query, parameters = None):
        try:
            cursor = self.connection.cursor()
        
            if parameters != None:
                cursor.execute(query, parameters)
            else:
                cursor.execute(query)

            self.connection.commit()
            cursor.close()
            self.connection.close()

            return True
        except:
            return False