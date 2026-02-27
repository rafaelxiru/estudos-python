from conectar import conexao, meu_cursor

try:
    print("Criando tabela...")
    meu_cursor.execute("""
        CREATE TABLE IF NOT EXISTS PRODUTO (
            CODIGO SERIAL PRIMARY KEY,
            NOME VARCHAR(100) NOT NULL,
            PRECO NUMERIC(10, 2) NOT NULL
        );
    """)
    # Importante: No PostgreSQL, precisamos confirmar as alterações
    conexao.commit() 
    print("Tabela 'PRODUTO' criada ou já existente!")

except Exception as e:
    print(f"Erro ao criar tabela: {e}")
    conexao.rollback() # Cancela a transação em caso de erro
