from core.pyba_logic import PybaLogic


class EndPointsLogic(PybaLogic):
    def init(self):
        super().init()

    # Parámetro get
    def getAll(self, endpoint):
        database = self.createDatabaseObj()
        sql = f"SELECT * FROM heroku_b1d10f4065d1053.{endpoint};"
        result = database.executeQuery(sql)
        if len(result) != 0:
            return result
        else:
            return []
