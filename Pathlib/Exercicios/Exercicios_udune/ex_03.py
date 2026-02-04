"""Exercício 3  Conferindo e filtrando arquivos .txt
Liste todos os arquivos .txt dentro de entrada/.

Imprima apenas o nome do arquivo (sem o caminho completo)."""

from pathlib import Path
from ex_01 import base

# Definindo o caminho da pasta entrada
pasta_entrada = base / 'dados' / 'entrada'

for arquivo in pasta_entrada.glob('*.txt'):
    print(arquivo.stem)  # Imprime apenas o nome do arquivo sem a extensão