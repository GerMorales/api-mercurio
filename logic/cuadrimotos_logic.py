from core.pyba_logic import PybaLogic


class cuadrimotosLogic(PybaLogic):
    def __init__(self):
        super().__init__()

    # Parámetro get
    def getCuadrimotosById(self, id):
        database = self.createDatabaseObj()
        sql = f"SELECT * FROM cuadrimotos where id = '{id}';"
        result = database.executeQuery(sql)
        if len(result) != 0:
            return result
        else:
            return {}

    # Parámetro post
    def getAllCuadrimotos(self):
        database = self.createDatabaseObj()
        sql = f"SELECT * FROM `cuadrimotos`;"
        result = database.executeQuery(sql)
        if len(result) != 0:
            return result
        else:
            return []
