"""3. Automatizando extração de arquivos
Considerando o arquivo zip que deixei na sessão de recursos, crie um script que:

Crie uma pasta chamada extraido/.

Extraia o conteúdo do .zip dentro da pasta criada.

Ao final, liste todos os arquivos extraídos."""

from pathlib import Path
import shutil
import os

# Caminhos corrigidos (sem espaços extras e com raw string)
zip_path = r"Shutil\Exercicios\exercicio_3\arquivos_secretos.zip"
extract_path = r"Shutil\Exercicios\exercicio_3\extraidos"

# Cria a pasta extraidos se não existir
os.makedirs(extract_path, exist_ok=True)

# Extraindo o arquivo zip
shutil.unpack_archive(zip_path, extract_path, "zip")

# Caminho da pasta onde os arquivos foram extraídos
extraidos = Path(extract_path)

# Listando os arquivos extraídos
for arquivo in extraidos.rglob("*"):
    print(arquivo.stem)
