import tkinter as tk
from tkinter import ttk, messagebox
from app.controllers.produto_controller import ProdutoController

class ProdutoView(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.controller = ProdutoController()
        self.pack()
        self.create_widgets()
        self.atualizar_lista()

    def create_widgets(self):
        self.master.title("Cadastro de Produtos")

        # Título
        tk.Label(self, text="Cadastro de Produtos", font=("Arial", 16)).pack(pady=10)

        # Formulário
        form_frame = tk.Frame(self)
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Nome:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        self.nome_entry = tk.Entry(form_frame, width=30)
        self.nome_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Preço:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.preco_entry = tk.Entry(form_frame, width=30)
        self.preco_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Estoque:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
        self.estoque_entry = tk.Entry(form_frame, width=30)
        self.estoque_entry.grid(row=2, column=1, padx=5, pady=5)

        # Botões
        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=10)

        self.btn_cadastrar = tk.Button(btn_frame, text="Cadastrar Produto", command=self.cadastrar_produto)
        self.btn_cadastrar.grid(row=0, column=0, padx=5)

        self.btn_editar = tk.Button(btn_frame, text="Editar Produto", command=self.editar_produto)
        self.btn_editar.grid(row=0, column=1, padx=5)

        self.btn_deletar = tk.Button(btn_frame, text="Deletar Produto", command=self.deletar_produto)
        self.btn_deletar.grid(row=0, column=2, padx=5)

        # Lista de produtos
        self.tree = ttk.Treeview(self, columns=("ID", "Nome", "Preço", "Estoque"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Preço", text="Preço")
        self.tree.heading("Estoque", text="Estoque")
        self.tree.pack(pady=10)

        # Vincula seleção da árvore ao método para carregar dados no formulário
        self.tree.bind("<<TreeviewSelect>>", self.carregar_produto_selecionado)

    def atualizar_lista(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        produtos = self.controller.listar_produtos()
        for produto in produtos:
            self.tree.insert("", "end", values=(produto['id'], produto['nome'], produto['preco'], produto['estoque']))

    def cadastrar_produto(self):
        nome = self.nome_entry.get()
        preco = self.preco_entry.get()
        estoque = self.estoque_entry.get()

        if not nome or not preco or not estoque:
            messagebox.showwarning("Aviso", "Todos os campos são obrigatórios.")
            return

        try:
            preco = float(preco)
            estoque = int(estoque)
        except ValueError:
            messagebox.showwarning("Aviso", "Preço deve ser número decimal e estoque um inteiro.")
            return

        self.controller.cadastrar_produto(nome, preco, estoque)
        messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso!")
        self.limpar_campos()
        self.atualizar_lista()

    def carregar_produto_selecionado(self, event):
        selecionado = self.tree.selection()
        if selecionado:
            item = self.tree.item(selecionado[0])
            produto = item['values']
            self.nome_entry.delete(0, tk.END)
            self.nome_entry.insert(0, produto[1])
            self.preco_entry.delete(0, tk.END)
            self.preco_entry.insert(0, produto[2])
            self.estoque_entry.delete(0, tk.END)
            self.estoque_entry.insert(0, produto[3])

    def editar_produto(self):
        selecionado = self.tree.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione um produto para editar.")
            return

        produto_id = self.tree.item(selecionado[0])['values'][0]
        nome = self.nome_entry.get()
        preco = self.preco_entry.get()
        estoque = self.estoque_entry.get()

        if not nome or not preco or not estoque:
            messagebox.showwarning("Aviso", "Todos os campos são obrigatórios.")
            return

        try:
            preco = float(preco)
            estoque = int(estoque)
        except ValueError:
            messagebox.showwarning("Aviso", "Preço deve ser número decimal e estoque um inteiro.")
            return

        self.controller.editar_produto(produto_id, nome, preco, estoque)
        messagebox.showinfo("Sucesso", "Produto atualizado com sucesso!")
        self.limpar_campos()
        self.atualizar_lista()

    def deletar_produto(self):
        selecionado = self.tree.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione um produto para deletar.")
            return
        produto_id = self.tree.item(selecionado[0])['values'][0]
        self.controller.deletar_produto(produto_id)
        messagebox.showinfo("Sucesso", "Produto deletado com sucesso!")
        self.limpar_campos()
        self.atualizar_lista()

    def limpar_campos(self):
        self.nome_entry.delete(0, tk.END)
        self.preco_entry.delete(0, tk.END)
        self.estoque_entry.delete(0, tk.END)
