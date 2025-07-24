from app.database.conexao import get_connection

class VendaModel:
    def __init__(self):
        self.conn = get_connection()

    def registrar_venda(self, id_cliente, itens):
        """
        Registra uma nova venda com os itens fornecidos.

        Parâmetros:
        - id_cliente: ID do cliente que realizou a compra
        - itens: lista de dicionários no formato:
            {
                'id_produto': int,
                'quantidade': int,
                'preco_unitario': float
            }
        """
        try:
            cursor = self.conn.cursor()
            total = sum(item['quantidade'] * item['preco_unitario'] for item in itens)

            # Inserir venda na tabela vendas
            cursor.execute(
                "INSERT INTO vendas (id_cliente, total) VALUES (%s, %s)",
                (id_cliente, total)
            )
            id_venda = cursor.lastrowid

            # Inserir cada item na tabela itens_venda
            for item in itens:
                cursor.execute(
                    """
                    INSERT INTO itens_venda (id_venda, id_produto, quantidade, preco_unitario)
                    VALUES (%s, %s, %s, %s)
                    """,
                    (id_venda, item['id_produto'], item['quantidade'], item['preco_unitario'])
                )

                # Atualizar estoque do produto
                cursor.execute(
                    "UPDATE produtos SET estoque = estoque - %s WHERE id = %s",
                    (item['quantidade'], item['id_produto'])
                )

            self.conn.commit()
        except Exception as e:
            print("Erro ao registrar venda:", e)
            self.conn.rollback()
        finally:
            cursor.close()
