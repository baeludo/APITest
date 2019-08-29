from flask_restful import Resource, reqparse

usuarios = [{
    "nome": "caveirinha",
    "idade": 20,
    "ocupacao": "mamador"
},
    {
        "nome": "bruno",
        "idade": 25,
        "ocupacao": "estagiario"
    },
    {
        "nome": "Juninho",
        "idade": 21,
        "ocupacao": "leitão"
    },
    {
        "nome": "Waguinho",
        "idade": 21,
        "ocupacao": "estagiario"
    }
]

class UsuarioModel:
    def __init__(self, nome, idade, ocupacao):
        self._nome = nome
        self._idade = idade
        self._ocupacao = ocupacao

    def json(self):
        return {
            "nome": self._nome,
            "idade": self._idade,
            "ocupacao": self._ocupacao
        }


class Usuarios(Resource):
    def get(self):
        return {"usuarios": usuarios}, 200


class Usuario(Resource):

    args = reqparse.RequestParser()
    args.add_argument("idade")
    args.add_argument("ocupacao")

    def encontrar_usuario(nome):
        for usuario in usuarios:
            if usuario["nome"] == nome:
                return usuario
            return False

    def get(self, nome):
        usuario = Usuario.encontrar_usuario(nome)
        if usuario:
            return usuario
        return {"'message': Usuário não encontrado."}, 404  #nao encontrado

    def post(self, nome):
        dados = Usuario.args.parse_args()
        usuario_obj = UsuarioModel(nome, **dados)
        novo_usuario = usuario_obj.json()

        usuarios.append(novo_usuario)
        return novo_usuario, 201

    def put(self, nome):
        dados = Usuario.args.parse_args()
        usuario_obj = UsuarioModel(nome, **dados)
        novo_usuario = usuario_obj.json()

        if novo_usuario:
            usuarios.update(novo_usuario)
            return novo_usuario, 200  # ok, atualizado

        usuarios.append(novo_usuario)
        return novo_usuario, 201  # ok, criado

    def delete(self, nome):
        global usuarios
        usuarios = [usuario for usuario in usuarios if usuario["nome"] != nome]
        return {"message": f"Pessoa de nome {nome} excluida."}
