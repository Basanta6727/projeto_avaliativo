import tkinter as tk
from tkinter import messagebox
from app.controllers.usuario_controller import UsuarioController

class LoginView(tk.Frame):
    def __init__(self, master=None, on_login_success=None):
        super().__init__(master)
        self.master = master
        self.controller = UsuarioController()
        self.on_login_success = on_login_success  # Callback ao logar
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.master.title("Login - Sistema de Controle de Loja")

        tk.Label(self, text="Usuário:").grid(row=0, column=0, pady=5, padx=5)
        self.username_entry = tk.Entry(self)
        self.username_entry.grid(row=0, column=1, pady=5, padx=5)

        tk.Label(self, text="Senha:").grid(row=1, column=0, pady=5, padx=5)
        self.senha_entry = tk.Entry(self, show="*")
        self.senha_entry.grid(row=1, column=1, pady=5, padx=5)

        self.login_button = tk.Button(self, text="Entrar", command=self.tentar_login)
        self.login_button.grid(row=2, column=0, columnspan=2, pady=10)

    def tentar_login(self):
        username = self.username_entry.get()
        senha = self.senha_entry.get()

        if not username or not senha:
            messagebox.showwarning("Aviso", "Informe usuário e senha.")
            return

        usuario = self.controller.login(username, senha)
        if usuario:
            messagebox.showinfo("Sucesso", f"Bem-vindo(a), {username}!")
            if self.on_login_success:
                self.on_login_success()
            else:
                self.master.destroy()
        else:
            messagebox.showerror("Erro", "Usuário ou senha inválidos.")
