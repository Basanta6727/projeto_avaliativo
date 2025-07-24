import tkinter as tk
from tkinter import ttk, messagebox
from app.controllers.cliente_controller import ClienteController

class ClienteView(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.controller = ClienteController()
        self.pack()
        self.create_widgets()
        self.atualizar_lista()

    def create_widgets(self):
        # Título
        self.label = tk.Label(self, text="Cadastro de Clientes", font=("Arial", 16))
        self.label.pack(pady=10)

        # Formulário
        form_frame = tk.Frame(self)
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Nome:").grid(row=0, column=0, sticky="e")
        self.nome_entry = tk.Entry(form_frame, width=30)
        self.nome_entry.grid(row=0, column=1)

        tk.Label(form_frame, text="Telefone:").grid(row=1, column=0, sticky="e")
        self.telefone_entry = tk.Entry(form_frame, width=30)
        self.telefone_entry.grid(row=1, column=1)

        tk.Label(form_frame, text="Email:").grid(row=2, column=0, sticky="e")
        self.email_entry = tk.Entry(form_frame, width=30)
        self.email_entry.grid(row=2, column=1)

        # Botão cadastrar
        self.btn_cadastrar = tk.Button(self, text="Cadastrar Cliente", command=self.cadastrar_cliente)
        self.btn_cadastrar.pack(pady=5)

        # Lista de clientes
        self.tree = ttk.Treeview(self, columns=("ID", "Nome", "Telefone", "Email"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Telefone", text="Telefone")
        self.tree.heading("Email", text="Email")
        self.tree.pack(pady=10)

        # Botão deletar
        self.btn_deletar = tk.Button(self, text="Deletar Cliente Selecionado", command=self.deletar_cliente)
        self.btn_deletar.pack(pady=5)

    def atualizar_lista(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        clientes = self.controller.listar_clientes()
        for cliente in clientes:
            self.tree.insert("", "end", values=(cliente['id'], cliente['nome'], cliente['telefone'], cliente['email']))

    def cadastrar_cliente(self):
        nome = self.nome_entry.get()
        telefone = self.telefone_entry.get()
        email = self.email_entry.get()

        if not nome:
            messagebox.showwarning("Aviso", "O nome é obrigatório.")
            return

        self.controller.cadastrar_cliente(nome, telefone, email)
        messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
        self.limpar_campos()
        self.atualizar_lista()

    def deletar_cliente(self):
        selecionado = self.tree.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione um cliente para deletar.")
            return
        cliente_id = self.tree.item(selecionado[0])['values'][0]
        self.controller.deletar_cliente(cliente_id)
        messagebox.showinfo("Sucesso", "Cliente deletado com sucesso!")
        self.atualizar_lista()

    def limpar_campos(self):
        self.nome_entry.delete(0, tk.END)
        self.telefone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
