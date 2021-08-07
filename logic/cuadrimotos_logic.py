from core.pyba_logic import PybaLogic

class cuadrimotosLogic(PybaLogic):
    def __init__(self):
        super().__init__()

    #Parámetro get
    def getCuadrimotosByTamagno(self, tamagno):
        database = self.createDatabaseObj()
        sql = f"SELECT * FROM cuadrimotos where tamagno = '{tamagno}';"
        result = database.executeQuery(sql)
        if len(result) != 0:
            return result
        else:
            return {}

    #Parámetro post
    def getAllCuadrimotos(self, tamagno):
        database = self.createDatabaseObj()
        sql = f"SELECT * FROM `cuadrimotos`;"
        result = database.executeQuery(sql)
        if len(result) != 0:
            return result
        else:
            return []

    #Parámetro put
    def insertCuadrimoto(self, cuadrimoto):
        database = self.createDatabaseObj()
        sql = (
            f"INSERT INTO `cuadrimotos`"
            +f"(`id`,`codigo_cuadri`,`tamagno`,`precio`,`horario_abre`,`horario_cierre`)"
            +f"VALUES(0,'{cuadrimoto['codigo_cuadri']}','{cuadrimoto['tamagno']}','{cuadrimoto['precio']}','{cuadrimoto['horario_abre']}','{cuadrimoto['horario_cierre']}');")
        rows = database.executeNonQueryRows(sql)
        return rows

    #Parámetro delete
    def deleteCuadrimoto(self, id):
        database = self.createDatabaseObj()
        sql = f"DELETE FROM `cuadrimotos` WHERE id = {id};"
        rows = database.executeNonQueryRows(sql)
        return rows