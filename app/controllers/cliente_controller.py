from app.models.cliente_model import ClienteModel

class ClienteController:
    def __init__(self):
        self.model = ClienteModel()

    def listar_clientes(self):
        """Retorna a lista de clientes cadastrados."""
        return self.model.listar_clientes()

    def cadastrar_cliente(self, nome, telefone, email):
        """Cadastra um novo cliente."""
        self.model.cadastrar_cliente(nome, telefone, email)

    def deletar_cliente(self, cliente_id):
        """Deleta um cliente pelo ID."""
        self.model.deletar_cliente(cliente_id)
