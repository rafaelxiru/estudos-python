import sqlite3 as conector

try:
    # 1. Conexão e Cursor
    conexao = conector.connect("./meu_banco.db")
    cursor = conexao.cursor()
    
    # IMPORTANTE: Ativa a verificação de chaves estrangeiras no SQLite
    cursor.execute("PRAGMA foreign_keys = ON;")
    print("Conexão estabelecida e chaves estrangeiras ativadas!")

    # 2. Comando para criar a tabela Pessoa
    sql_pessoa = ''' CREATE TABLE IF NOT EXISTS Pessoa (
                        cpf INTEGER NOT NULL,
                        nome TEXT NOT NULL,
                        nascimento DATE NOT NULL,
                        oculos BOOLEAN NOT NULL,
                        PRIMARY KEY (cpf)
                    ); '''

    # 3. Comando para criar a tabela Marca
    sql_marca = ''' CREATE TABLE IF NOT EXISTS Marca (
                        id INTEGER NOT NULL,
                        nome TEXT NOT NULL,
                        sigla CHARACTER(2) NOT NULL,
                        PRIMARY KEY (id)
                    ); '''

    # 4. Comando para criar a tabela Veiculo (depende das outras duas)
    sql_veiculo = ''' CREATE TABLE IF NOT EXISTS Veiculo (
                        placa CHARACTER(7) NOT NULL,
                        ano INTEGER NOT NULL,
                        cor TEXT NOT NULL,
                        proprietario INTEGER NOT NULL,
                        marca INTEGER NOT NULL,
                        PRIMARY KEY (placa),
                        FOREIGN KEY(proprietario) REFERENCES Pessoa(cpf),
                        FOREIGN KEY(marca) REFERENCES Marca(id)
                    ); '''

    # Executando os comandos na ordem correta
    cursor.execute(sql_pessoa)
    cursor.execute(sql_marca)
    cursor.execute(sql_veiculo)
    
    # Efetivando as alterações
    conexao.commit()
    print("Todas as tabelas (Pessoa, Marca e Veiculo) foram verificadas/criadas!")

except conector.DatabaseError as err:
    print(f"Erro de banco de dados: {err}")

finally:
    if 'conexao' in locals():
        cursor.close()
        conexao.close()
        print("Conexão encerrada com segurança.")