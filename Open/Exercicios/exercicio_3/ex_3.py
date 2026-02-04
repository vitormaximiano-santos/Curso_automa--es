"""
Exercício 3 — Filtrando logs por palavra-chave
Baixe o arquivo logs.txt anexado, e escreva um programa que:

Leia todas as linhas do arquivo

Peça ao usuário uma palavra-chave (como ERROR, INFO, WARNING, etc...)

Mostre apenas as linhas que contenham essa palavra-chave."""

# Abrindo o arquivo de logs no modo de leitura
with open('Open/Exercicios/exercicio_3/acesso.log', 'r', encoding='utf-8') as file:
    
    # Solicitando ao usuário a palavra-chave para filtrar os logs
    palavra_chave = input("Digite a palavra-chave para filtrar os logs (ex: ERROR, INFO, WARNING): ")
    
    # Iterando sobre cada linha do arquivo
    for linha in file.readlines():
        
        # Verificando se a palavra-chave está presente na linha (case insensitive)
        if palavra_chave.upper() in linha:
            
            # Imprimindo a linha que contém a palavra-chave
            print(linha.strip())