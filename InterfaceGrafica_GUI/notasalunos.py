import tkinter as tk
from tkinter import ttk


# 1. Definição das Funções (Devem vir antes de serem usadas nos botões)
def cadastrar_aluno():
    try:
        nome = entrada_nome.get()
        n1 = float(entrada_nota1.get())
        n2 = float(entrada_nota2.get())
        n3 = float(entrada_nota3.get())

        media = (n1 + n2 + n3) / 3
        situacao = (
            "Aprovado" if media >= 7 else "Recuperação" if media >= 5 else "Reprovado"
        )

        tabela.insert("", "end", values=(nome, n1, n2, n3, f"{media:.2f}", situacao))

        # Limpa os campos após o cadastro
        entrada_nome.delete(0, tk.END)
        entrada_nota1.delete(0, tk.END)
        entrada_nota2.delete(0, tk.END)
        entrada_nota3.delete(0, tk.END)
    except ValueError:
        print("Erro: Insira valores numéricos nas notas!")


# 2. Configuração da Janela Principal
janela = tk.Tk()
janela.title("Sistema de Gestão Escolar")
janela.geometry("700x500")

# 3. Elementos da Interface (Widgets)
tk.Label(janela, text="Nome do Aluno:").pack()
entrada_nome = tk.Entry(janela)
entrada_nome.pack()

tk.Label(janela, text="Nota 1:").pack()
entrada_nota1 = tk.Entry(janela)
entrada_nota1.pack()

tk.Label(janela, text="Nota 2:").pack()
entrada_nota2 = tk.Entry(janela)
entrada_nota2.pack()

tk.Label(janela, text="Nota 3:").pack()
entrada_nota3 = tk.Entry(janela)
entrada_nota3.pack()

tk.Button(
    janela, text="Cadastrar Aluno", command=cadastrar_aluno, bg="green", fg="white"
).pack(pady=10)

# 4. Tabela (Treeview)
colunas = ("Nome", "Nota1", "Nota2", "Nota3", "Média", "Situação")
tabela = ttk.Treeview(janela, columns=colunas, show="headings")

for col in colunas:
    tabela.heading(col, text=col)
    tabela.column(col, width=100, anchor="center")

tabela.pack(padx=10, pady=10, fill="both", expand=True)

# 5. Barra de Rolagem
scrollbar = ttk.Scrollbar(janela, orient="vertical", command=tabela.yview)
tabela.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")

# 6. Dados Iniciais (Corrigido para 3 notas cada)
alunos_iniciais = [
    ("Alice", 8.5, 7.0, 9.0),
    ("Bruno", 5.0, 6.0, 4.5),
    ("Carlos", 3.5, 4.0, 2.0),
    ("Daniela", 9.0, 9.5, 10.0),
]

for nome, n1, n2, n3 in alunos_iniciais:
    media = (n1 + n2 + n3) / 3
    situacao = (
        "Aprovado" if media >= 7 else "Recuperação" if media >= 5 else "Reprovado"
    )
    tabela.insert("", "end", values=(nome, n1, n2, n3, f"{media:.2f}", situacao))

janela.mainloop()
