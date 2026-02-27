import PySimpleGUI as sg

# 1. Escolha um tema (ele tem centenas!)
sg.theme('DarkBlue3')

# 2. Defina o que aparece na janela (linhas e colunas)
layout = [
    [sg.Text('Bem-vindo ao seu sistema, Rafael!')],
    [sg.Text('Digite algo:'), sg.Input(key='-INPUT-')],
    [sg.Button('OK'), sg.Button('Sair')]
]

# 3. Crie a janela
window = sg.Window('Janela do Rafael', layout)

# 4. O "coração" do programa (loop de eventos)
while True:
    event, values = window.read()
    
    # Se fechar a janela ou clicar em Sair, para o programa
    if event == sg.WIN_CLOSED or event == 'Sair':
        break
        
    # Se clicar em OK, mostra o que foi digitado
    if event == 'OK':
        sg.popup(f"Você digitou: {values['-INPUT-']}")

window.close()