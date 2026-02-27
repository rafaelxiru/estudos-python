from conectar import conexao, meu_cursor

def ler_produtos():
    try:
        # Busca todos os produtos ordenados pelo código
        meu_cursor.execute("SELECT * FROM PRODUTO ORDER BY CODIGO;")
        produtos = meu_cursor.fetchall()
        
        print("\n" + "="*45)
        print(f"{'ID':<5} | {'NOME DO PRODUTO':<25} | {'PREÇO':<10}")
        print("-" * 45)
        
        for p in produtos:
            # p[0] é o ID, p[1] é o Nome, p[2] é o Preço
            print(f"{p[0]:<5} | {p[1]:<25} | R$ {p[2]:>8.2f}")
            
        print("="*45 + "\n")
        
    except Exception as e:
        print(f"Erro ao ler dados: {e}")
    finally:
        # Fecha a conexão após listar tudo
        meu_cursor.close()
        conexao.close()
        print("Consulta finalizada e conexão fechada.")

if __name__ == "__main__":
    ler_produtos()