import sqlite3 as conector
try:
     conexao = conector.connect("meubanco.bd")
     cursor = conexao.cursor()
     print("conexão estabelecida com sucesso!")

     comando = ''' CREATE TABLE Pessoa(
              cpf INTEGER NOT NULL,
              nome text NOT NULL,
              nascimento DATE NOT NULL,
              oculos BOOLEAN NOT NULL,
              PRIMARY KEY (cpf))'''

     cursor.execute (comando)
     conexao.commit()
except conector.DatabaseError as err:
        print("Erro de banco de dados ",err)
finally:
      if conexao: 
         cursor.close()
         conexao.close()