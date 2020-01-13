from DataAccess import DataAccess

class Lenguage:

    id_lenguage = None
    name_lenguage = None
    type_lenguage = None

    # Default: Constructor
    def __init__(self, id = None):
        if isinstance(id, int):
            parameters = { 'int': id }
            sql = ("SELECT id, name, type FROM Lenguage WHERE id = %(int)s;") 
            lengauge = DataAccess().get_query(sql, parameters)

            self.id_lenguage = lengauge[0][0]
            self.name_lenguage = lengauge[0][1]
            self.type_lenguage = lengauge[0][2]
    
    #Method: Get values in Lenguage
    def get_lengauges(self, id = None):
        
        parameters = {}
        arguments = ''

        if id != None:
            parameters.update({'int': id})
        
        if len(parameters) == 1:
            arguments = "WHERE id = %(int)s"

        sql = "SELECT id, name, type FROM Lenguage " + arguments + ";"
        lst_lengauge = DataAccess().get_query(sql, parameters)
        return lst_lengauge

    # Method: Insert a new value in Lenguage
    def insert_lenguage(self, Lenguage):
        parameters = ( Lenguage.id_lenguage , Lenguage.name_lenguage, Lenguage.type_lenguage )
        sql = """
        INSERT INTO Lenguage (id, name, type)
            VALUES (%s, %s, %s);
        """
        execute = DataAccess().execute_query(sql, parameters)
        return execute
    
    # Method: Update a value Lenguage
    def update_lenguage(self, Lenguage):
        parameters = ( Lenguage.name_lenguage, Lenguage.type_lenguage, Lenguage.id_lenguage )
        sql = """
        UPDATE Lenguage SET name = %s, type = %s WHERE id = %s;
        """
        execute = DataAccess().execute_query(sql, parameters)
        return execute

    # Method: Delete lenguage
    def delete_lengauje(self, id):
        parameters = (id,)
        print(id)
        sql = """
        DELETE FROM Lenguage WHERE id = %s;
        """
        execute = DataAccess().execute_query(sql, parameters)
        return execute