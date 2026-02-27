import psycopg2
import sys

# Ajuste para o Windows não travar nos acentos
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def executar_crud():
    conn = None
    try:
        print("Tentando conectar ao PostgreSQL...")
        
        # --- AQUI ESTAVA O ERRO: Corrigi 'postegres' para 'postgres' ---
        conn = psycopg2.connect(
            host = 'localhost',
            port = 5432,
            database = 'postgres',   # Mudei para o banco padrão 'postgres' que sempre existe
            user = 'postgres',       # Nome corrigido aqui
            password = 'admin123'        # <--- Verifique se sua senha é essa mesma
        )
        
        cursor = conn.cursor()
        print("CONEXÃO ESTABELECIDA COM SUCESSO!")

        # 1. CRIAR TABELA
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS public."AGENDA" (
                id INTEGER PRIMARY KEY,
                nome TEXT NOT NULL,
                telefone CHAR(12) NOT NULL
            );
        """)

        # 2. INSERIR DADO DE TESTE
        cursor.execute("""
            INSERT INTO public."AGENDA" (id, nome, telefone)
            VALUES (1, 'Rafael Estudo', '11999999999')
            ON CONFLICT (id) DO NOTHING;
        """)
        #ON CONFLICT (id) DO NOTHING; 
#Essa é a parte que evita erros. O ID costuma ser uma "Chave Primária" (Primary Key), o que significa que não podem existir dois registros com o mesmo ID.
#O que aconteceria SEM essa linha: Se você rodasse o código duas vezes, na segunda vez o Python daria um erro enorme dizendo: "duplicate key value violates unique constraint".
#O que acontece COM essa linha: O banco de dados olha e diz: "Opa, eu já tenho o ID 2 aqui. Em vez de dar erro e parar o programa, eu vou apenas não fazer nada (DO NOTHING) e seguir em frente".
        cursor.execute("""
                       INSERT INTO public."AGENDA" (id, nome, telefone)
                       VALUES(2, 'Leticia', '6129832999')
                        ON CONFLICT (id) DO NOTHING; 
                       """)
# SALVA os dados na minha tabela do banco de dados. Se não fizer isso, os dados ficam só na memória e não são guardados de verdade.
        conn.commit()
        print("Tabela e dados verificados!")

        # 3. MOSTRAR RESULTADOS
        print("\n--- LISTA DA AGENDA ---")
        cursor.execute('SELECT * FROM public."AGENDA";') # (*) selecio a tabela inteira 
        for row in cursor.fetchall():#pega tudo que tem na tabela e mostra linha por linha 
            print(f"ID: {row[0]} | Nome: {row[1]} | Tel: {row[2]}")#row[0] é o ID, row[1] é o nome, row[2] é o telefone. O número entre colchetes indica a posição da coluna na tabela (começando do 0).
        print("-----------------------\n")

    except Exception:
        # Se der erro, ele vai mostrar essa mensagem limpa sem travar no UTF-8
        print("\n[ERRO DE CONEXÃO]")
        print("Causas prováveis:")
        print("- A senha 'admin' pode estar errada.")
        print("- O serviço do PostgreSQL pode estar parado.")
        print("- Dica: Verifique a senha no pgAdmin.")

    finally:
        if conn:
            cursor.close()
            conn.close()
            print("Conexão encerrada.")

if __name__ == "__main__":
    executar_crud()