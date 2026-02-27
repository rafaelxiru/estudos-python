"""
import flet as ft

def main(page: ft.Page):
    page.title = "Meu App Flet"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK

    texto = ft.Text("Olá, Leticia e Rafael!", size=30, color="blue")
    
    def mudar_texto(e):
        texto.value = "O Flet funcionou perfeitamente!"
        page.update()

    botao = ft.ElevatedButton("Clique em mim", on_click=mudar_texto)

    page.add(texto, botao)

ft.app(target=main)
"""

#-----------------------------------------------------------------

import customtkinter as ctk

# Configuração visual
ctk.set_appearance_mode("dark")  # Modos: "System", "Dark", "Light"
ctk.set_default_color_theme("blue") 

app = ctk.CTk()
app.geometry("400x240")
app.title("Sistema do Rafael")

def clique():
    print("Botão pressionado!")

label = ctk.CTkLabel(app, text="Interface Moderna", font=("Roboto", 24))
label.pack(pady=20)

botao = ctk.CTkButton(app, text="Clique Aqui", command=clique)
botao.pack(pady=10)

app.mainloop()