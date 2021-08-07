from core.pyba_logic import PybaLogic

class restaurantesLogic(PybaLogic):
    def init(self):
        super().init()

    #Parámetro get
    def getRestauranteByNombre(self, nombre):
        database = self.createDatabaseObj()
        sql = f"SELECT * FROM restaurante where nombre = '{nombre}';"
        result = database.executeQuery(sql)
        if len(result) != 0:
            return result
        else:
            return {}

    #Parámetro post
    def getAllRestaurantes(self, nombre):
        database = self.createDatabaseObj()
        sql = f"SELECT * FROM `restaurante`;"
        result = database.executeQuery(sql)
        if len(result) != 0:
            return result
        else:
            return []

    #Parámetro put
    def insertRestaurante(self, restaurante):
        database = self.createDatabaseObj()
        sql = (
            f"INSERT INTO `restaurante`"
            +f"(`id`,`nombre`,`horario_inicio`,`horario_cierre`,`precio_promedio`,`distancia_hotel`,`calificacion_cliente`)"
            +f"VALUES(0,'{restaurante['nombre']}','{restaurante['horario_inicio']}','{restaurante['horario_cierre']}','{restaurante['precio_promedio']}','{restaurante['distancia_hotel']}','{restaurante['calificacion_cliente']}');")
        rows = database.executeNonQueryRows(sql)
        return rows

     #Parámetro patch
    def updateRestaurante(self, id, restaurante):
        database = self.createDatabaseObj()
        sql = (
            f"UPDATE `restaurante`"
            +f"SET `nombre` = '{restaurante['nombre']}',`horario_inicio` = '{restaurante['horario_inicio']}',`horario_cierre` = '{restaurante['horario_cierre']}',`precio_promedio` = '{restaurante['precio_promedio']}',`distancia_hotel` = '{restaurante['distancia_hotel']}',`calificacion_clientes` = '{restaurante['calificacion_clientes']}'"
            +f"WHERE `id` = {id};"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

     #Parámetro delete
    def deleteRestaurante(self, id):
        database = self.createDatabaseObj()
        sql = f"DELETE FROM `restaurante` WHERE id = {id};"
        rows = database.executeNonQueryRows(sql)
        return rows