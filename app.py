from flask import Flask
from flask_restful import Api
from model.classes import *

app = Flask(__name__)
api = Api(app)

api.add_resource(Usuarios, "/usuarios/")
api.add_resource(Usuario, "/usuario/<string:nome>")

if __name__ == "__main__":
    app.run(debug=True)
