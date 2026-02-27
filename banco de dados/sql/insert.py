import sqlite3 as conector
import os
from modelo import pessoa 

# 1. Caminho inteligente para achar o 'meu_banco.db' na mesma pasta
diretorio = os.path.dirname(__file__)
caminho_banco = os.path.join(diretorio, "meu_banco.db")

conexao = conector.connect(caminho_banco)
cursor = conexao.cursor()

# Ativa chaves estrangeiras (boa prática já que você as definiu)
cursor.execute("PRAGMA foreign_keys = ON;")

# 2. Criando o objeto da Maria
p1 = pessoa(100000000099, 'Maria', '1990-01-31', False)
p2 = pessoa(202330000091, 'João', '1990-02-03', True)
p3 = pessoa(398293983859, 'josé', '2000-12-04', False)
# 3. Inserindo (O nome da tabela deve ser 'Pessoa' com P maiúsculo, conforme seu script)
comando = "INSERT OR IGNORE INTO Pessoa (cpf, nome, nascimento, oculos) VALUES (?, ?, ?, ?);"

try:
    cursor.execute(comando, (p1.cpf, p1.nome, p1.nascimento, p1.oculos))
    cursor.execute(comando, (p2.cpf, p2.nome, p2.nascimento, p2.oculos))
    cursor.execute(comando, (p3.cpf, p3.nome, p3.nascimento,p3.oculos))
    conexao.commit()
    print(" inserido com sucesso no meu_banco.db!")
except conector.IntegrityError:
    print("Erro: Este CPF já existe ou viola uma regra de integridade.")
finally:
    cursor.close()
    conexao.close()