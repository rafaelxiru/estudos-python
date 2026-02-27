from faker import Faker 
from conectar import conexao, meu_cursor

# Configurando o faker para gerar dados em português
fake = Faker('pt_BR')

print("Iniciando a inserção de dados...")

try:
    for _ in range(10):
        nome_produto = fake.word().capitalize() # Capitalize deixa a primeira letra maiúscula
        preco = round(fake.random_number(digits=5) / 100, 2)
        
        meu_cursor.execute("INSERT INTO produto (nome, preco) VALUES (%s, %s)", (nome_produto, preco))
        
        # Commit pode ficar dentro do loop para garantir cada inserção, 
        # ou fora para salvar tudo de uma vez.
        conexao.commit()
        print(f"Produto '{nome_produto}' inserido com sucesso!")

except Exception as e:
    print(f"Ocorreu um erro: {e}")
    conexao.rollback()

finally:
    # AGORA SIM: Fechamos o cursor e a conexão DEPOIS de terminar o loop
    meu_cursor.close()
    conexao.close()
    print("\nConexão encerrada com segurança.")
    