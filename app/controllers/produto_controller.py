from app.models.produto_model import ProdutoModel

class ProdutoController:
    def __init__(self):
        self.model = ProdutoModel()

    def listar_produtos(self):
        """Retorna a lista de produtos cadastrados."""
        return self.model.listar_produtos()

    def cadastrar_produto(self, nome, preco, estoque):
        """Cadastra um novo produto."""
        self.model.cadastrar_produto(nome, preco, estoque)

    def editar_produto(self, produto_id, nome, preco, estoque):
        """Atualiza os dados de um produto existente."""
        self.model.editar_produto(produto_id, nome, preco, estoque)

    def deletar_produto(self, produto_id):
        """Deleta um produto pelo ID."""
        self.model.deletar_produto(produto_id)
