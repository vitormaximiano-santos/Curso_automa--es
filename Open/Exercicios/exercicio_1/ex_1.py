"""Exercício 1 — Criando um relatório simples
Crie um arquivo chamado relatorio.txt que contenha a frase "Estou aprendendo Python!

Inclua no final do arquivo a data e hora de criação do arquivo de forma automática"""

from datetime import datetime

# Define o caminho completo do arquivo
caminho = "Open/Exercicios/exercicio_1/relatorio.txt"

# Cria e escreve no arquivo
with open(caminho, "w", encoding="utf-8") as arquivo:
    arquivo.write("Estou aprendendo Python!\n")
    
    # Adiciona a data e hora atual ao arquivo
    data_hora_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    arquivo.write(f"Data e hora de criação do arquivo: {data_hora_atual}\n")
