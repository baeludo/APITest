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