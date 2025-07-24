import tkinter as tk
from tkinter import messagebox
from app.views.cliente_view import ClienteView
from app.views.produto_view import ProdutoView
from app.views.venda_view import VendaView  # Você pode criar essa view depois

class MenuView(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Menu Principal - Sistema de Controle de Loja")
        self.pack(padx=20, pady=20)
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Menu Principal", font=("Arial", 18)).pack(pady=10)

        btn_clientes = tk.Button(self, text="Clientes", width=20, command=self.abrir_clientes)
        btn_clientes.pack(pady=5)

        btn_produtos = tk.Button(self, text="Produtos", width=20, command=self.abrir_produtos)
        btn_produtos.pack(pady=5)

        btn_vendas = tk.Button(self, text="Vendas", width=20, command=self.abrir_vendas)
        btn_vendas.pack(pady=5)

        btn_sair = tk.Button(self, text="Sair", width=20, command=self.master.quit)
        btn_sair.pack(pady=20)

    def abrir_clientes(self):
        self.nova_janela(ClienteView, "Clientes")

    def abrir_produtos(self):
        self.nova_janela(ProdutoView, "Produtos")

    def abrir_vendas(self):
        try:
            self.nova_janela(VendaView, "Vendas")
        except ImportError:
            messagebox.showinfo("Info", "Tela de vendas ainda não implementada.")

    def nova_janela(self, ViewClass, titulo):
        nova_janela = tk.Toplevel(self.master)
        nova_janela.title(titulo)
        ViewClass(nova_janela)
