from app.models.usuario_model import UsuarioModel

class UsuarioController:
    def __init__(self):
        self.model = UsuarioModel()

    def login(self, username, senha):
        """
        Valida o login do usuário.
        Retorna os dados do usuário se sucesso, ou None se inválido.
        """
        return self.model.validar_login(username, senha)

    def cadastrar(self, username, senha):
        """
        Cadastra um novo usuário.
        """
        self.model.cadastrar_usuario(username, senha)
