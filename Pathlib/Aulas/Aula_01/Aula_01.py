import pathlib

# Pega a pasta onde o script Aula_01.py está
base = pathlib.Path(__file__).parent

# Cria o caminho para a nova pasta dentro de Aula_01
nova_pasta = base / "Nova_Pasta"

# Cria a nova pasta
nova_pasta.mkdir(exist_ok=True, parents=True)

print(f"Pasta criada em: {nova_pasta}")


# Define o caminho para um arquivo de texto
caminho_arquivo = pathlib.Path(r"C:\Users\Vitor\Desktop\Python\Curso_automações\Pathlib\Aulas\Aula_01\arquivo_texto")

# Exibe o caminho completo do arquivo
print(caminho_arquivo)

# Define um caminho absoluto para um arquivo de texto
caminho_arquivo2 = pathlib.Path(r"C:\Users\Vitor\Desktop\Python\Curso_automações\Pathlib\Aulas\Aula_01\arquivo_texto2")

# Exibe o caminho absoluto do arquivo
print(caminho_arquivo2)

# Verifica se o arquivo existe
if caminho_arquivo.exists():
    print(f"O arquivo {caminho_arquivo} existe.")
    
else:
    print(f"O arquivo {caminho_arquivo} não existe.")
    
    
# Define o caminho para uma pasta
caminho_pasta = pathlib.Path(r"C:\Users\Vitor\Desktop\Python\Curso_automações\Pathlib\Aulas\Aula_01\pasta_ex")

# Verifica se o caminho é uma pasta
if caminho_pasta.is_dir():
    print(f"O caminho {caminho_pasta} é uma pasta.")
else:
    print(f"O caminho {caminho_pasta} não é uma pasta.")

# Cria uma nova pasta com subpastas na pasta Aula_01
nova_pasta = pathlib.Path(base / "Nova_Pasta/outra_pasta/mais_uma_pasta")

# Cria a nova pasta, incluindo quaisquer pastas pai necessárias
nova_pasta.mkdir(exist_ok=True, parents=True)

# Remove o arquivo, se existir
caminho_arquivo2.unlink(missing_ok=True)

# Remove a pasta mais_uma_pasta
nova_pasta.rmdir()  


# Define o caminho para o arquivo avaliacao.txt na pasta Aula_01
avaliacao = pathlib.Path("Pathlib/Aulas/Aula_01/Avaliação.txt")

# Escreve texto no arquivo avaliacao.txt
#texto = avaliacao.read_text()
#print(texto)

# Escreve texto no arquivo avaliacao.txt
avaliacao.write_text("Avaliação de Pathlib", encoding="utf-8")

# Define a pasta atual
pasta = pathlib.Path()

# Lista todos os arquivos e pastas na pasta atual
for arquivo in pasta.iterdir():
    print(f'{arquivo} é um arquivo ou pasta na pasta atual.')
    
# Lista todos os arquivos .txt na pasta atual
for arquivo in pasta.glob("*.txt"):
    print(f"{arquivo} é um arquivo de texto.")
    

