import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd  # Se não tiver, use: pip install pandas openpyxl

# 1. Funções do Sistema
def cadastrar_aluno():
    try:
        nome = entrada_nome.get()
        if not nome:
            messagebox.showwarning("Erro", "O nome do aluno é obrigatório!")
            return
            
        n1 = float(entrada_nota1.get())
        n2 = float(entrada_nota2.get())
        n3 = float(entrada_nota3.get())

        media = (n1 + n2 + n3) / 3
        situacao = "Aprovado" if media >= 7 else "Recuperação" if media >= 5 else "Reprovado"

        tabela.insert("", "end", values=(nome, n1, n2, n3, f"{media:.2f}", situacao))

        # Limpa os campos após inserir
        entrada_nome.delete(0, tk.END)
        entrada_nota1.delete(0, tk.END)
        entrada_nota2.delete(0, tk.END)
        entrada_nota3.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Erro", "As notas devem ser números (use ponto em vez de vírgula)!")

def exportar_para_excel():
    dados = []
    # Pega cada linha da tabela visual
    for item in tabela.get_children():
        dados.append(tabela.item(item)['values'])
    
    if not dados:
        messagebox.showwarning("Aviso", "A tabela está vazia!")
        return

    # Gera o arquivo Excel
    try:
        colunas_lista = ["Nome", "Nota1", "Nota2", "Nota3", "Média", "Situação"]
        df = pd.DataFrame(dados, columns=colunas_lista)
        df.to_excel("notasalunos.xlsx", index=False)
        messagebox.showinfo("Sucesso", "Arquivo 'notasalunos.xlsx' salvo na pasta do projeto!")
    except Exception as e:
        messagebox.showerror("Erro", f"Feche o arquivo Excel antes de exportar! Erro: {e}")

# 2. Interface Principal
janela = tk.Tk()
janela.title("Sistema de Gestão Escolar")
janela.geometry("750x600")

# 3. Campos de Entrada
frame_form = tk.Frame(janela)
frame_form.pack(pady=10)

tk.Label(frame_form, text="Nome:").grid(row=0, column=0, padx=5, pady=5)
entrada_nome = tk.Entry(frame_form)
entrada_nome.grid(row=0, column=1)

tk.Label(frame_form, text="Nota 1:").grid(row=1, column=0)
entrada_nota1 = tk.Entry(frame_form)
entrada_nota1.grid(row=1, column=1)

tk.Label(frame_form, text="Nota 2:").grid(row=2, column=0)
entrada_nota2 = tk.Entry(frame_form)
entrada_nota2.grid(row=2, column=1)

tk.Label(frame_form, text="Nota 3:").grid(row=3, column=0)
entrada_nota3 = tk.Entry(frame_form)
entrada_nota3.grid(row=3, column=1)

# 4. Botões de Ação
tk.Button(janela, text="Cadastrar Aluno", command=cadastrar_aluno, bg="#28a745", fg="white", width=20).pack(pady=5)
tk.Button(janela, text="Exportar para Excel", command=exportar_para_excel, bg="#007bff", fg="white", width=20).pack(pady=5)

# 5. Tabela (Treeview)
colunas = ("Nome", "Nota1", "Nota2", "Nota3", "Média", "Situação")
tabela = ttk.Treeview(janela, columns=colunas, show="headings")

# O erro estava aqui: certifique-se de que as duas linhas abaixo estejam recuadas!
for col in colunas:
    tabela.heading(col, text=col)
    tabela.column(col, width=110, anchor="center")

tabela.pack(padx=10, pady=10, fill="both", expand=True)

# 6. Barra de Rolagem
sb = ttk.Scrollbar(janela, orient="vertical", command=tabela.yview)
tabela.configure(yscrollcommand=sb.set)
sb.pack(side="right", fill="y")

# 7. Dados Iniciais
dados_teste = [
    ("Alice", 8.5, 7.0, 9.0),
    ("Bruno", 5.0, 6.0, 4.5),
    ("Carlos", 3.5, 4.0, 2.0)
]

for n, n1, n2, n3 in dados_teste:
    m = (n1 + n2 + n3) / 3
    s = "Aprovado" if m >= 7 else "Recuperação" if m >= 5 else "Reprovado"
    tabela.insert("", "end", values=(n, n1, n2, n3, f"{m:.2f}", s))

janela.mainloop()