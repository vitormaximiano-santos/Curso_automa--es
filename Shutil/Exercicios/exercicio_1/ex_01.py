"""1. Cópia simples com estrutura
Crie um script que:

Crie uma pasta imagens.

Coloque 2 arquivos fictícios .png dentro dela

Copie todos os arquivos .png da pasta imagens para uma nova pasta chamada backup."""

from pathlib import Path
import shutil

# Criar a pasta imagens
imagens = Path("Shutil/Exercicios/exercicio_1/images")

# Criar a pasta imagens se não existir
imagens.mkdir(parents=True, exist_ok=True)

# Criar a pasta imagens se não existir
backup = Path("Shutil/Exercicios/exercicio_1/backup")

# Criar a pasta backup se não existir
backup.mkdir(parents=True, exist_ok=True)

# Criar arquivos fictícios .png dentro da pasta imagens
shutil.copytree(imagens, backup, dirs_exist_ok=True )