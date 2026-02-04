from pathlib import Path
import shutil
from datetime import datetime

# Define o diretório base como o diretório onde o script está localizado
base = Path(__file__).parent

# Descompacta o arquivo organizador.zip na pasta organizador_descompactado
shutil.unpack_archive(base / 'organizador.zip', base / 'organizador_descompactado', 'zip')

# Cria a pasta para os arquivos organizados
pasta_organizada = base / 'arquivos_organizados'

# Define o nome do arquivo de log
arquivo_log = "registro.log"

# Inicializa a contagem de arquivos organizados
arquivo_qtd = 0

extensoes_encontradas = []

# Cria a pasta organizada se não existir
if not pasta_organizada.exists():
    
    # Cria a pasta organizada
    pasta_organizada.mkdir(parents=True)
    
    # itera sobre os arquivos descompactados
for arquivo in (base / 'organizador_descompactado').iterdir():
    
    # Incrementa a contagem de arquivos organizados
    arquivo_qtd += 1
    
    # Obtém a extensão do arquivo em letras minúsculas
    extensao = arquivo.suffix.lower()[1:]  # Remove o ponto do início da extensão
    
    # Adiciona a extensão à lista se ainda não estiver presente
    if extensao not in extensoes_encontradas:
        extensoes_encontradas.append(extensao)
    
    # Define o caminho da subpasta para a extensão
    subpasta = pasta_organizada / extensao
    
    # Cria a subpasta se não existir
    if not subpasta.exists():
        subpasta.mkdir(parents=True)

    destino = subpasta / arquivo.name
    
    # copia o arquivo para a subpasta correspondente
    shutil.move (arquivo, destino)
    
    # Registra a operação no arquivo de log
    with open(base/arquivo_log, "a", encoding="utf-8") as log:
        
        # Obtém a data e hora atuais formatadas
        agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Escreve a entrada no log
        log.write(f"{agora} - Arquivo '{arquivo.name}' movido para '{subpasta}'\n")    
        
        
# Exibe a mensagem de conclusão
print(f"Organização concluída! {arquivo_qtd} arquivos organizados em {len(extensoes_encontradas)} categorias.")

# Exibe as extensões encontradas
for ext in extensoes_encontradas:
    print(f"- {ext}")