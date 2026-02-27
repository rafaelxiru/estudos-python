import tkinter as Tk
from tkinter import messagebox


def submit():
    # recupera os dados dos campos de entrada
    nome = nome_entry.get()
    email = email_entry.get()
    ##verifica qual radio button foi selecionado
    linguagem_preferida = linguagem_var.get()
    print("Nome:", nome)
    print("Email:", email)
    print("Linguagem preferida:", linguagem_preferida)

    ##mostra uma caixa de mensagem com os dados submetidos
    messagebox.showinfo(
        "Dados submetidos",
        f"Nome: {nome}\n Email: {email}\n Linguagem preferida: {linguagem_preferida}",
    )


# cria a janela principal
root = Tk.Tk()
root.title("Formulario de inscrição")
# cria um frame para organizar os widgets(componetes da tela)
frame = Tk.Frame(root)
frame.pack(padx=100, pady=100)

# label para o campo de nome
nome_label = Tk.Label(frame, text="Nome:")
nome_label.grid(row=0, column=0, sticky="e")
# campo de entrada para nome
nome_entry = Tk.Entry(frame)
nome_entry.grid(row=0, column=1)

# Label para o campo de email
email_label = Tk.Label(frame, text="Email:")
email_label.grid(row=1, column=0, sticky="e")

# campo de entrada para email
email_entry = Tk.Entry(frame)
email_entry.grid(row=1, column=1)

# variavel para armazenar escolha da linguagem
linguagem_var = Tk.StringVar(value="Python")

python_radio = Tk.Radiobutton(
    frame, text="python", variable=linguagem_var, value="Python"
)
python_radio.grid(row=2, column=0)
java_radio = Tk.Radiobutton(frame, text="java", variable=linguagem_var, value="Java")
java_radio.grid(row=2, column=1)
submit_button = Tk.Button(frame, text="submeter", command=submit)
submit_button.grid(row=3, columnspan=2, pady=10)

root.mainloop()
