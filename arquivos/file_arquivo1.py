import os

arquivo1 = open("dados1. txt", 'r', encoding='utf8')
print(os.path.abspath(arquivo1.name))
arquivo1.write("olá mundo!!")
arquivo1.seek(0)
conteudo=arquivo1.read()
print("conteudo do arquivo:", conteudo)
print("tipo de conteudo:", type (conteudo))

print(os.path.relpath(arquivo1.name))
print(arquivo1)

arquivo1.close()

#Imagine que o Python é um garçom anotando um pedido.

#open(): Ele pega o bloco de notas.

#write(): Ele escreve o pedido no bloco, mas ainda está segurando o bloco na mão (na memória RAM).

#Sem o close(): Ele vai embora com o bloco na mão. A cozinha (o seu HD) nunca recebe o papel.

#Com o close(): Ele arranca a folha e entrega na cozinha. Agora o pedido (texto) está salvo!

# função path.relpath para imprimir o caminho relativo 

# função path.abspath para exibir o caminho absoluto

######algumas instruçoes####
#<_io.TextIOWrapper name='dados1.txt' mode='r' encoding='cp1252'>
#O tipo do objeto, TextIOWrapper, que trata de arquivos de texto.
#O nome do arquivo, name='dados.txt'.
#O modo de acesso ao arquivo, mode='r'.
#A codificação do arquivo, encoding='cp1252'.].

#Quando abrimos um arquivo, precisamos informar ao Python o que desejamos fazer, ou seja, qual será o modo (mode) de acesso ao arquivo. O modo é um dos parâmetros da função open, e cada modo é representado por uma string.
#Os principais modos são:
#'r'(read)- modo de leitura (padrão);
#'w' (write)- modo de escrita (cria um arquivo novo ou sobrescreve um arquivo existente);
#'a' (append)- modo de anexação (adiciona conteúdo ao final do arquivo existente

#'r'	Abre o arquivo para leitura (default).
#'w'	Abre o arquivo para escrita, truncando o arquivo primeiro.
#'x'	Cria um arquivo para escrita e falha, caso ele exista.
#'a'	Abre o arquivo para escrita, acrescentando conteúdo ao final do arquivo, caso ele exista.
#'b'	Modo binário.
#'t'	Modo texto (default).
#'+'	Abre o arquivo para atualização (leitura ou escrita).

