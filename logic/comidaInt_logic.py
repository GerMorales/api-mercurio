from core.pyba_logic import PybaLogic

class comidaIntLogic(PybaLogic):
    def __init__(self):
        super().__init__()

    #Parámetro get
    def getComidaByCountry(self, pais):
        database = self.createDatabaseObj()
        sql = f"SELECT * FROM comida where pais = '{pais}';"
        result = database.executeQuery(sql)
        if len(result) != 0:
            return result
        else:
            return {}

    #Parámetro post
    def getAllComidas(self, pais):
        database = self.createDatabaseObj()
        sql = f"SELECT * FROM `comida`;"
        result = database.executeQuery(sql)
        if len(result) != 0:
            return result
        else:
            return []

    #Parámetro put
    def insertComida(self, comida):
        database = self.createDatabaseObj()
        sql = (
            f"INSERT INTO `comida`"
            +f"(`id`,`nombre`,`pais`,`precio`)"
            +f"VALUES(0,'{comida['nombre']}','{comida['pais']}','{comida['precio']}');")
        rows = database.executeNonQueryRows(sql)
        return rows

     #Parámetro patch
    def updateComida(self, id, comida):
        database = self.createDatabaseObj()
        sql = (
            f"UPDATE `comida`"
            +f"SET `nombre` = '{comida['nombre']}',`pais` = '{comida['pais']}',`precio` = '{comida['precio']}'"
            +f"WHERE `id` = {id};"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

     #Parámetro delete
    def deleteComida(self, id):
        database = self.createDatabaseObj()
        sql = f"DELETE FROM `comida` WHERE id = {id};"
        rows = database.executeNonQueryRows(sql)
        return rows