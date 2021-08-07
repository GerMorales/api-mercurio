from flask_restful import Resource, reqparse
from logic.comidaInt_logic import comidaIntLogic


class Comida(Resource):
    def __init__(self):
        self.comida_put_args = self.createParser()
        self.logic = comidaIntLogic()

    def createParser(self):
        args = reqparse.RequestParser()
        args.add_argument("nombre", type=str, help="nombre de la comida")
        args.add_argument("pais", type=str, help="pais de la comida")
        args.add_argument("precio", type=float, help="precio de la comida")
        return args

    def get(self, pais):
        result = self.logic.getComidaByCountry(pais)
        return result, 200

    def post(self, pais):
        result = self.logic.getAllComidas(pais)
        return result, 200

    def put(self, id):
        comida = self.comida_put_args.parse_args()
        rows = self.logic.insertComida(comida)
        return {"rowsAffected": rows}

    def patch(self, id):
        comida = self.comida_put_args.parse_args()
        rows = self.logic.updateComida(id, comida)
        return {"rowsAffected": rows}

    def delete(self, id):
        comida = self.comida_put_args.parse_args()
        rows = self.logic.deleteComida(id)
        return {"rowsAffected": rows}