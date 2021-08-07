from flask_restful import Resource, reqparse
from logic.cuadrimotos_logic import cuadrimotosLogic


class Cuadrimotos(Resource):
    def __init__(self):
        self.cuadrimotos_put_args = self.createParser()
        self.logic = cuadrimotosLogic()

    def createParser(self):
        args = reqparse.RequestParser()
        args.add_argument("codigo", type=str, help="codigo de la cuadrimoto")
        args.add_argument("tamagno", type=str, help="tamagno de la cuadrimoto")
        args.add_argument("precio", type=float, help="precio de la cuadrimoto")
        args.add_argument("horario_abre", type=str, help="horario de apertura de la cuadrimoto")
        args.add_argument("horario_cierre", type=str, help="horario de cierre de la cuadrimoto")
        return args

    def get(self, tamagno):
        result = self.logic.getCuadrimotosByTamagno(tamagno)
        return result, 200

    def post(self, tamagno):
        result = self.logic.getAllCuadrimotos(tamagno)
        return result, 200

    def put(self, id):
        cuadrimoto = self.cuadrimotos_put_args.parse_args()
        rows = self.logic.insertCuadrimoto(cuadrimoto)
        return {"rowsAffected": rows}

    def delete(self, id):
        cuadrimoto = self.cuadrimotos_put_args.parse_args()
        rows = self.logic.deleteCuadrimoto(id)
        return {"rowsAffected": rows}