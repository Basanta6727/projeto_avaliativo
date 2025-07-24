import tkinter as tk
from tkinter import ttk, messagebox
from app.controllers.venda_controller import VendaController
from app.controllers.cliente_controller import ClienteController
from app.controllers.produto_controller import ProdutoController

class VendaView(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.venda_controller = VendaController()
        self.cliente_controller = ClienteController()
        self.produto_controller = ProdutoController()
        self.pack()
        self.itens_venda = []
        self.create_widgets()

    def create_widgets(self):
        self.master.title("Registro de Vendas")

        # Seleção do cliente
        tk.Label(self, text="Cliente:").grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.clientes = self.cliente_controller.listar_clientes()
        self.cliente_var = tk.StringVar()
        self.cliente_combo = ttk.Combobox(self, textvariable=self.cliente_var, state="readonly")
        self.cliente_combo['values'] = [f"{c['id']} - {c['nome']}" for c in self.clientes]
        self.cliente_combo.grid(row=0, column=1, padx=5, pady=5)

        # Seleção de produto
        tk.Label(self, text="Produto:").grid(row=1, column=0, padx=5, pady=5, sticky='e')
        self.produtos = self.produto_controller.listar_produtos()
        self.produto_var = tk.StringVar()
        self.produto_combo = ttk.Combobox(self, textvariable=self.produto_var, state="readonly")
        self.produto_combo['values'] = [f"{p['id']} - {p['nome']}" for p in self.produtos]
        self.produto_combo.grid(row=1, column=1, padx=5, pady=5)

        # Quantidade
        tk.Label(self, text="Quantidade:").grid(row=2, column=0, padx=5, pady=5, sticky='e')
        self.quantidade_entry = tk.Entry(self)
        self.quantidade_entry.grid(row=2, column=1, padx=5, pady=5)

        # Botão adicionar item
        self.btn_add_item = tk.Button(self, text="Adicionar Item", command=self.adicionar_item)
        self.btn_add_item.grid(row=3, column=0, columnspan=2, pady=10)

        # Lista de itens
        self.tree = ttk.Treeview(self, columns=("Produto", "Quantidade", "Preço Unitário", "Subtotal"), show="headings")
        self.tree.heading("Produto", text="Produto")
        self.tree.heading("Quantidade", text="Quantidade")
        self.tree.heading("Preço Unitário", text="Preço Unitário")
        self.tree.heading("Subtotal", text="Subtotal")
        self.tree.grid(row=4, column=0, columnspan=2, pady=10)

        # Botão registrar venda
        self.btn_registrar = tk.Button(self, text="Registrar Venda", command=self.registrar_venda)
        self.btn_registrar.grid(row=5, column=0, columnspan=2, pady=10)

    def adicionar_item(self):
        produto_selecionado = self.produto_var.get()
        quantidade = self.quantidade_entry.get()

        if not produto_selecionado:
            messagebox.showwarning("Aviso", "Selecione um produto.")
            return
        if not quantidade.isdigit() or int(quantidade) <= 0:
            messagebox.showwarning("Aviso", "Quantidade deve ser um número inteiro positivo.")
            return

        produto_id = int(produto_selecionado.split(" - ")[0])
        produto = next((p for p in self.produtos if p['id'] == produto_id), None)

        if produto is None:
            messagebox.showerror("Erro", "Produto não encontrado.")
            return

        quantidade = int(quantidade)

        if quantidade > produto['estoque']:
            messagebox.showwarning("Aviso", f"Estoque insuficiente. Disponível: {produto['estoque']}")
            return

        preco_unitario = produto['preco']
        subtotal = quantidade * preco_unitario

        # Adicionar ao array de itens
        self.itens_venda.append({
            'id_produto': produto_id,
            'quantidade': quantidade,
            'preco_unitario': preco_unitario
        })

        # Atualizar tabela
        self.tree.insert("", "end", values=(produto['nome'], quantidade, f"R$ {preco_unitario:.2f}", f"R$ {subtotal:.2f}"))

        # Limpar seleção
        self.produto_var.set('')
        self.quantidade_entry.delete(0, tk.END)

    def registrar_venda(self):
        cliente_selecionado = self.cliente_var.get()
        if not cliente_selecionado:
            messagebox.showwarning("Aviso", "Selecione um cliente.")
            return
        if not self.itens_venda:
            messagebox.showwarning("Aviso", "Adicione ao menos um item à venda.")
            return

        cliente_id = int(cliente_selecionado.split(" - ")[0])
        self.venda_controller.registrar_venda(cliente_id, self.itens_venda)

        messagebox.showinfo("Sucesso", "Venda registrada com sucesso!")

        # Limpar tudo
        self.itens_venda.clear()
        for i in self.tree.get_children():
            self.tree.delete(i)
        self.cliente_var.set('')
