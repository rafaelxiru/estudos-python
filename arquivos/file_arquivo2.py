import os 
#abrindo umo aquivo no modo escrita 
arquivo = open ('exemplo.txt', 'w', encoding='utf8')
#exibindo os atributos do arquivo
print("Nome do arquivo:", arquivo.name)
print("Modo de acesso:", arquivo.mode)
print("Arquivo esta fechado?", arquivo.closed)
#escrevendo no aquivo
arquivo.write("este é um exemplo de escrita em arquivo.\n")

#fechando o arquivo
arquivo.close()

#verificando se o arquivo esta fechado
print("Arquivo esta fechado?", arquivo.closed)

#exibindo caminhos relativo e absoluto
realpath = os.path.relpath('exemplo.txt')
abspath = os.path.abspath('exemplo.txt')
print("Caminho relativo:", realpath)
print("Caminho absoluto:", abspath)