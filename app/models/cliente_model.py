from app.database.conexao import get_connection

class ClienteModel:
    def __init__(self):
        self.conn = get_connection()

    def listar_clientes(self):
        """
        Retorna uma lista de todos os clientes cadastrados.
        """
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM clientes")
        clientes = cursor.fetchall()
        cursor.close()
        return clientes

    def cadastrar_cliente(self, nome, telefone, email):
        """
        Cadastra um novo cliente.
        """
        cursor = self.conn.cursor()
        query = "INSERT INTO clientes (nome, telefone, email) VALUES (%s, %s, %s)"
        cursor.execute(query, (nome, telefone, email))
        self.conn.commit()
        cursor.close()

    def deletar_cliente(self, cliente_id):
        """
        Remove um cliente pelo ID.
        """
        cursor = self.conn.cursor()
        query = "DELETE FROM clientes WHERE id = %s"
        cursor.execute(query, (cliente_id,))
        self.conn.commit()
        cursor.close()
