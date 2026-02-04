"""Exercício 2 — Contador de letras
Crie um arquivo chamado mensagem.txt com um parágrafo de texto que você inventar. Depois, escreva um script que conte e exiba quantas letras existem nesse texto.
"""

from datetime import datetime

# Define o caminho do arquivo mensagem.txt
caminho = "Open/Exercicios/exercicio_2/mensagem.txt"

# Solicita ao usuário que digite uma frase e remove espaços em branco extras no início e no fim
frase = input("Digite uma frase: ").strip()

# Remove os espaços entre as palavras para contar apenas as letras
frase_sem_espacos = frase.replace(" ", "")

# Abre o arquivo mensagem.txt em modo de escrita e codificação UTF-8
with open(caminho, "w", encoding="utf-8") as arquivo:
    arquivo.write(frase)
    
    print("A frase tem", len(frase_sem_espacos), "caracteres.")
