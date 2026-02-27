import psycopg2
import sys

# TESTE DE DIAGNÓSTICO
try:
    print("Tentando conectar...")
    # COLOQUE SEUS DADOS REAIS AQUI
    conexao = psycopg2.connect(
        host='127.0.0.1',
        database='postgres',
        user='postgres',
        password='admin123',
        port='5432'
    )
    print("CONECTADO COM SUCESSO!")
    meu_cursor = conexao.cursor()

except Exception:
    # Isso aqui força o Python a mostrar o erro original do sistema
    import traceback
    print("\n--- ERRO DETALHADO ABAIXO ---")
    traceback.print_exc()
    print("----------------------------\n")