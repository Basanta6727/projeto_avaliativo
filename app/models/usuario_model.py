from app.database.conexao import get_connection

class UsuarioModel:
    def __init__(self):
        self.conn = get_connection()

    def validar_login(self, username, senha):
        """
        Verifica se existe um usuário com o username e senha informados.
        Retorna o usuário se existir, senão retorna None.
        """
        cursor = self.conn.cursor(dictionary=True)
        query = "SELECT * FROM usuarios WHERE username = %s AND senha = %s"
        cursor.execute(query, (username, senha))
        usuario = cursor.fetchone()
        cursor.close()
        return usuario

    def cadastrar_usuario(self, username, senha):
        """
        Cadastra um novo usuário no sistema.
        """
        cursor = self.conn.cursor()
        query = "INSERT INTO usuarios (username, senha) VALUES (%s, %s)"
        cursor.execute(query, (username, senha))
        self.conn.commit()
        cursor.close()
