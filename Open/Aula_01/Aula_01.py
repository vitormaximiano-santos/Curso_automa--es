# Abrindo um arquivo em modo de leitura
arquivo = open("Open/Aula_01/Aula_01.txt", "r", encoding="utf-8")

# Lendo o conteúdo do arquivo
conteudo = arquivo.read()

# Exibindo o conteúdo lido
print(conteudo)

# Fechando o arquivo (manualmente)
#arquivo.close()

# Usando o gerenciador de contexto 'with' para abrir o arquivo (automaticamente fecha o arquivo) e escrevendo no arquivo (substitui o conteúdo existente)
with open("Open/Aula_01/Aula_01.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Olá, mundo!")
    
# Usando o gerenciador de contexto 'with' para abrir o arquivo (automaticamente fecha o arquivo) e escrevendo no arquivo (adiciona ao conteúdo existente)    
with open("Open/Aula_01/Aula_01.txt", "a", encoding="utf-8") as arquivo:   
    arquivo.write("\n belo dia,não?")
    
    
# Usando o gerenciador de contexto 'with' para abrir o arquivo (automaticamente fecha o arquivo) e lendo e escrevendo no arquivo
with open("Open/Aula_01/Aula_01.txt", "r+", encoding="utf-8") as arquivo:
    arquivo.write("\n Vamos aprender Python!")
    arquivo.seek(0)  # Move o cursor para o início do arquivo (necessario para ler desde o começo)
    print(arquivo.read())  # Lê e imprime o conteúdo atualizado do arquivo


# Usando o gerenciador de contexto 'with' para abrir o arquivo (automaticamente fecha o arquivo) e lendo do arquivo
with open("Open/Aula_01/Aula_01.txt", "r", encoding="utf-8") as arquivo:
    # Lendo todas as linhas do arquivo como uma lista
    print(arquivo.readlines()) 
    
    