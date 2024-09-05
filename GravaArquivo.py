with open ("aula.txt", "w") as arq:
    arq.write("Falei Falei Falei")
    arq.write("\nFalei Falei Falei")


with open ("aula.txt", "r") as arq:
    conteudo = arq.read()
    print(conteudo)
    
with open ("index.html", 'w') as index:
    index.write("<body><h1>Index</h1>")
    index.write("<br><h2>Exemplo HTML com json e manipulação de arquivos</h2>")
    index.write("<h3>")
    nome = ""
    while nome != "SAIR":
        nome = input("Digite um nome ou SAIR: ")
        if nome != "SAIR":
            arq.write("<br>" + nome)
    arq.write("</h3></body>")
    
with open("aula.txt", "r") as arq:
    conteudo = arq.read()
print("Tipo de dado da Variavel: ", type(conteudo))
print("\nConteúdo do arquivo:\n", conteudo)