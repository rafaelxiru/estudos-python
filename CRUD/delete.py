import psycopg2

try:
    # 1. CONEXÃO (Usando os dados que funcionaram antes)
    conn = psycopg2.connect(
        host = 'localhost',       # Corrigido de 'localelhost'
        database = 'postgres',    # No teste anterior funcionou com 'postgres'
        user = 'postgres',        # Corrigido de 'admin'
        password = 'admin123'     # Corrigido de 'passowird'
    )

    cursor = conn.cursor()

    # 2. ATUALIZAR (UPDATE)
    # Note que tirei uma aspa extra que tinha depois de "AGENDA"
    cursor.execute("""
        DELETE FROM public."AGENDA"
        WHERE id = 1;
    """)

    # Importante: O commit salva a alteração no banco!
    conn.commit()
    print("Dado deletado com sucesso!")

    # 3. LER OS DADOS (SELECT)
    # Corrigido de 'execut' para 'execute'
    cursor.execute('SELECT id, nome, telefone FROM public."AGENDA";')
    
    rows = cursor.fetchall()

    print("\n--- DADOS ATUALIZADOS ---")
    for row in rows:
        print(f"ID: {row[0]} | Nome: {row[1]} | Telefone: {row[2]}")
    print("------------------------")

    cursor.close()
    conn.close()

except Exception as e:
    print(f"Erro ao atualizar: {e}")