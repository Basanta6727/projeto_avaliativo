from app.models.venda_model import VendaModel

class VendaController:
    def __init__(self):
        self.model = VendaModel()

    def registrar_venda(self, id_cliente, itens):
        """
        Registra uma venda para um cliente com os itens fornecidos.
        
        Parâmetros:
        - id_cliente: ID do cliente (int)
        - itens: lista de dicionários com os campos:
            {
                'id_produto': int,
                'quantidade': int,
                'preco_unitario': float
            }
        """
        self.model.registrar_venda(id_cliente, itens)
