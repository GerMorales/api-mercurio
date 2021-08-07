from flask import Flask
from flask_restful import Api
from resources.comidaInt_resource import Comida
from resources.cuadrimotos_resource import Cuadrimotos
from resources.restaurante_resource import Restaurante

app = Flask(__name__)
api = Api(app)

api.add_resource(Comida, "/comidaInt_resource/<string:pais>")
api.add_resource(Cuadrimotos, "/cuadrimotos_resource/<string:tamagno>")
api.add_resource(Restaurante, "/restaurante_resource/<string:nombre>")


if __name__ == "__main__":
    app.run(debug=True)