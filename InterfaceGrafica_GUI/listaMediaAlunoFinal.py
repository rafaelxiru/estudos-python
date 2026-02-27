import tkinter as tk
from tkinter import ttk
import pandas as pd 

class PrincipalRAD:
    def __init__(self, win):
        #componentes 
        self.lblNome=tk.label(win, text= 'Nome do Aluno:')
        self.lblNota1=tk.label(win, text= 'Nota 1')
        self.lblNota2=tk.label(win, text= 'Nota 2')
        self.lblMedia=tk.label(win, text= 'Média')
        self.txtNome=tk.Entry(bd=3)
        self.txtNota1=tk.Entry()
        self.txtNota2=tk.Entry()
        self.btncalcular=tk.Button(win, text= 'calcular Média', command=self.fcalcularMedia)
        