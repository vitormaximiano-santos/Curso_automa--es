from pathlib import Path
from shutil import rmtree

# Definindo o caminho do projeto
caminho_projeto = Path()

# Exibindo o caminho do projeto
print(caminho_projeto)
print("-" * 20)

# Exibindo o caminho absoluto do projeto
print(caminho_projeto.absolute())
print("-" * 20)

# Definindo o caminho do projeto usando __file__
caminho_arquivo = Path(__file__)
print(caminho_arquivo)
print("-" * 20)

# Exibindo o diretório pai do arquivo atual
print(caminho_arquivo.parent)
print("-" * 20)

# Exibindo o diretório pai do diretório pai
ideias = caminho_arquivo.parent / 'Ideias'
print(ideias / 'arquivo.txt')  

print("-" * 20)
print(Path.home())  # Diretório home do usuário


print("-" * 20)
# Definindo um caminho para um arquivo na área de trabalho
arquivo = Path.home() / 'Desktop' / 'arquivo.txt'

#print("-" * 20)
#arquivo.touch()  # Cria o arquivo se não existir
#print(arquivo)   # Exibe o caminho do arquivo criado

#print("-" * 20)
#arquivo.write_text('Ola Mundo!!!')  # Escreve texto no arquivo
#print(arquivo.read_text())  # Lê e exibe o conteúdo do arquivo

#arquivo.unlink()  # Remove o arquivo
#print(f'Arquivo {arquivo} removido.')
print("-" * 20)

# Escrevendo múltiplas linhas em um arquivo
with caminho_arquivo.open('w') as f:
    f.write('linha 1\n')
    f.write('linha 2\n')    

print(caminho_arquivo.read_text())  # Lê e exibe o conteúdo do arquivo
print("-" * 20)

 # Definindo o caminho da nova pasta
caminho_pasta = Path.home() / 'Desktop' / 'Nova_Pasta'
caminho_pasta.mkdir(exist_ok=True)  # Cria a pasta se não existir

# Definindo o caminho da subpasta
subpasta = caminho_pasta / 'Subpasta'
subpasta.mkdir(exist_ok=True)  # Cria a subpasta se não existir

# Definindo o caminho do novo arquivo na subpasta
outro_arquivo = subpasta / 'outro_arquivo.txt'
outro_arquivo.write_text('Conteúdo do outro arquivo.')  # Escreve texto no novo arquivo
outro_arquivo.touch()  # Cria o arquivo se não existir

mais_arquivo = caminho_pasta / 'mais_arquivo.txt'
mais_arquivo.write_text('Conteúdo do mais arquivo.')  # Escreve texto no novo arquivo
mais_arquivo.touch()  # Cria o arquivo se não existir

caminho_pasta.rmdir()  # Remove a pasta (apenas se estiver vazia)
print(f'Pasta {caminho_pasta} removida.')

files = caminho_pasta / 'files' # Cria uma subpasta 'files'
files.mkdir(exist_ok=True) # Cria a subpasta se não existir


for item in range(10):
    arquivo_temp = files / f'arquivo_{item}.txt'
    
    if arquivo_temp.exists():
        arquivo_temp.unlink()  # Remove o arquivo se existir
        
    else:
        arquivo_temp.touch()  # Cria o arquivo se não existir
        
        # Escrevendo conteúdo no arquivo
    with arquivo_temp.open('w') as f:
        f.write(f'Conteúdo do arquivo\n')
        f.write(f'Arquivo número {item}\n')
        
# Removendo a pasta 'files' e todo o seu conteúdo
def rmtree(root,remove_root=True):
    for item in root.iterdir(): # Itera sobre os itens na pasta root
        if item.is_dir():
            print('DIR  :',item) #
            rmtree(item,False)
            item.rmdir()
        else:
            print('FILE :',item)
            item.unlink()
    if remove_root:
        root.rmdir()
        
# Chamando a função para remover a pasta 'files'
rmtree(files)