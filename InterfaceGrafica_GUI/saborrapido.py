import tkinter as tk
from tkinter import messagebox

class SaborRapidoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sabor Rápido - Protótipo")
        self.root.geometry("400x550")

        # Itens do menu e preços
        self.itens_menu = {"Hambúrguer": 10.00, "Batata Frita": 5.00, "Refrigerante": 3.00}
        self.pedido = []

        # --- Elementos da Interface (UI) ---
        tk.Label(root, text="Cardápio Sabor Rápido", font=("Arial", 20, "bold")).pack(pady=10)

        # Criar botões para cada item do menu
        for item, preco in self.itens_menu.items():
            btn = tk.Button(root, text=f"Adicionar {item} - R${preco:.2f}", 
                            width=30, command=lambda i=item, p=preco: self.adicionar_item(i, p))
            btn.pack(pady=5)

        tk.Label(root, text="Seu Pedido:", font=("Arial", 12, "bold")).pack(pady=15)
        
        # Lista para mostrar o pedido atual
        self.lista_pedido = tk.Listbox(root, width=40, height=10)
        self.lista_pedido.pack()

        # Exibição do Total
        self.label_total = tk.Label(root, text="Total: R$0.00", font=("Arial", 12, "bold"), fg="green")
        self.label_total.pack(pady=10)

        # Botões de ação
        tk.Button(root, text="Finalizar Pedido", bg="green", fg="white", 
                  command=self.finalizar).pack(side="left", padx=50)
        
        tk.Button(root, text="Limpar", bg="red", fg="white", 
                  command=self.limpar).pack(side="right", padx=50)

    def adicionar_item(self, nome, preco):
        self.pedido.append(preco)
        self.lista_pedido.insert(tk.END, f"{nome} - R${preco:.2f}")
        self.atualizar_total()

    def atualizar_total(self):
        total = sum(self.pedido)
        self.label_total.config(text=f"Total: R${total:.2f}")

    def finalizar(self):
        if not self.pedido:
            messagebox.showwarning("Aviso", "O pedido está vazio!")
        else:
            total = sum(self.pedido)
            messagebox.showinfo("Sucesso", f"Pedido realizado!\nTotal: R${total:.2f}")
            self.limpar()

    def limpar(self):
        self.pedido = []
        self.lista_pedido.delete(0, tk.END)
        self.atualizar_total()

if __name__ == "__main__":
    root = tk.Tk()
    app = SaborRapidoApp(root)
    root.mainloop()