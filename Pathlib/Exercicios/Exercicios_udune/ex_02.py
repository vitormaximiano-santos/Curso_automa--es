"""Exercício 2  Criar vários arquivos de exemplo
Dentro da pasta entrada/, crie 3 arquivos vazios:
dados1.txt
dados2.txt
dados3.txt"""
 
from pathlib import Path
from ex_01 import base

# Lista de nomes de arquivos a serem criados
arquivos = ['dados1.txt', 'dados2.txt', 'dados3.txt']

# Definindo o caminho da pasta entrada
pasta_entrada = base / 'dados' / 'entrada'

# Criando a pasta entrada se não existir
pasta_entrada.mkdir(parents=True, exist_ok=True)

# Criando os arquivos dentro da pasta entrada
for nome_arquivo in arquivos: # nome_arquivo recebe cada item da lista arquivos
    
    arquivo_path = pasta_entrada / nome_arquivo # Define o caminho completo do arquivo
    
    arquivo_path.touch(exist_ok=True) # Cria o arquivo se não existir
    
    print(f'Arquivo criado: {arquivo_path}') # Imprime o caminho do arquivo criado
    
