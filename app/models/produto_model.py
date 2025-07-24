from app.database.conexao import get_connection

class ProdutoModel:
    def __init__(self):
        self.conn = get_connection()

    def listar_produtos(self):
        """
        Retorna todos os produtos cadastrados.
        """
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM produtos")
        produtos = cursor.fetchall()
        cursor.close()
        return produtos

    def cadastrar_produto(self, nome, preco, estoque):
        """
        Cadastra um novo produto.
        """
        cursor = self.conn.cursor()
        query = "INSERT INTO produtos (nome, preco, estoque) VALUES (%s, %s, %s)"
        cursor.execute(query, (nome, preco, estoque))
        self.conn.commit()
        cursor.close()

    def editar_produto(self, produto_id, nome, preco, estoque):
        """
        Atualiza os dados de um produto existente.
        """
        cursor = self.conn.cursor()
        query = "UPDATE produtos SET nome=%s, preco=%s, estoque=%s WHERE id=%s"
        cursor.execute(query, (nome, preco, estoque, produto_id))
        self.conn.commit()
        cursor.close()

    def deletar_produto(self, produto_id):
        """
        Remove um produto pelo ID.
        """
        cursor = self.conn.cursor()
        query = "DELETE FROM produtos WHERE id = %s"
        cursor.execute(query, (produto_id,))
        self.conn.commit()
        cursor.close()
