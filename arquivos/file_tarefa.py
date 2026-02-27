import os  # Importa a biblioteca para interagir com o sistema operacional (pastas, caminhos)
import shutil  # Importa a biblioteca para manipulação de arquivos (mover, copiar)

# Define a função responsável por criar as pastas caso elas não existam
def criar_diretorio(diretorios):
    for diretorio in diretorios:  # Percorre a lista de caminhos de diretórios recebida
        if not os.path.exists(diretorio):  # Verifica se a pasta já existe no computador
            try:  # Tenta executar o bloco abaixo
                os.makedirs(diretorio)  # Cria a pasta fisicamente
                print(f"diretorio {diretorio} criado com sucesso")  # Avisa que deu certo
            except PermissionError:  # Caso o Windows/Linux negue o acesso
                print(f"Sem permissão para criar o diretoório {diretorio}")
            except Exception as e:  # Captura qualquer outro erro inesperado
                print(f"Erro ao criar o diretótio {diretorio}: {e}")

# Define a função que identifica e move os arquivos
def mover_arquivo(diretorio_origem, caminho_banco):
    for arquivo in os.listdir(diretorio_origem):  # Lista tudo o que tem dentro da pasta de origem
        caminho_arquivo = os.path.join(diretorio_origem, arquivo)  # Monta o caminho completo do arquivo
        
        if os.path.isfile(caminho_arquivo):  # Verifica se o item é um arquivo (e não uma pasta)
            extensao = arquivo.split('.')[-1].lower()  # Pega o texto após o último ponto e deixa em minúsculo
            
            if extensao in ['pdf','txt','jpg']:  # Verifica se a extensão está na nossa lista de interesse
                diretorio_destino = os.path.join(diretorio_origem, extensao)
                  # Define a pasta destino (ex: /pdf)
            elif extensao in ['scv', 'sql', 'json']:
                diretorio_destino = os.path.join(caminho_banco, extensao)
                
                try:  # Tenta realizar a movimentação
                    shutil.move(caminho_arquivo, diretorio_destino)  # Move o arquivo da origem para o destino
                    print(f"Arquivo {arquivo} movido para {diretorio_destino}")  # Sucesso!
                except PermissionError:  # Caso o arquivo esteja aberto ou protegido
                    print(f"Sem permissão para mover o arquivo {arquivo}.")    
                except Exception as e:  # Erros genéricos (disco cheio, caminho inválido, etc)
                    print(f"Erro inesperado ao mover{arquivo}: {e}")
            else:  # Se a extensão não for pdf, txt ou jpg
                # Opcional: ignorar arquivos do sistema que começam com ponto
                if not arquivo.startswith('.'):
                    print(F"Extensão {extensao} de arquivo {arquivo} não é suportada.")

# Função principal que organiza a execução do script
def main():
    diretorio_trabalho = "diretorio trabalho"  # Define o nome da pasta onde tudo vai acontecer
    banco_de_dados = "banco de dados"
    # Cria uma lista com os caminhos das subpastas que queremos (pdf, txt, jpg)
    diretorios = [os.path.join(diretorio_trabalho, 'pdf'),
                  os.path.join(diretorio_trabalho, 'txt'),
                  os.path.join(diretorio_trabalho, 'jpg'),
                  os.path.join(banco_de_dados, 'csv'),
                  os.path.join(banco_de_dados, 'sql'),
                  os.path.join(banco_de_dados, 'json')]

                  
    
    criar_diretorio(diretorios)  # Chama a função para criar as pastas de organização
    mover_arquivo(diretorio_trabalho, banco_de_dados)  # Chama a função para mover os arquivos para essas pastas

# Ponto de entrada do script: garante que o código só rode se for o arquivo principal
if __name__ == "__main__":
    main()  # Inicia o programa chamando a função main