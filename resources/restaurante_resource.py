from flask_restful import Resource, reqparse
from logic.restaurantes_logic import restaurantesLogic


class Restaurante(Resource):
    def __init__(self):
        self.restaurante_put_args = self.createParser()
        self.logic = restaurantesLogic()

    def createParser(self):
        args = reqparse.RequestParser()
        args.add_argument("nombre", type=str, help="nombre del restaurante")
        args.add_argument("horario_inicio", type=str, help="horario de apertura del restaurante")
        args.add_argument("horario_cierre", type=str, help="horario de cierre del restaurante")
        args.add_argument("precio_promedio", type=float, help="precio promedio del restaurante")
        args.add_argument("distancia_hotel", type=float, help="distancia del restaurante al hotel")
        args.add_argument("calificacion_cliente", type=float, help="calificacion del restaurante")
        return args

    def get(self, nombre):
        result = self.logic.getRestauranteByNombre(nombre)
        return result, 200

    def post(self, nombre):
        result = self.logic.getAllRestaurantes(nombre)
        return result, 200

    def put(self, id):
        restaurante = self.restaurante_put_args.parse_args()
        rows = self.logic.insertRestaurante(restaurante)
        return {"rowsAffected": rows}

    def patch(self, id):
        restaurante = self.restaurante_put_args.parse_args()
        rows = self.logic.updateRestaurante(id, restaurante)
        return {"rowsAffected": rows}

    def delete(self, id):
        restaurante = self.restaurante_put_args.parse_args()
        rows = self.logic.deleteRestaurante(id)
        return {"rowsAffected": rows}