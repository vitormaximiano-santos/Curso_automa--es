# criar um arquivo com o nome alunos.xlsx

import pandas as pd
import random

# Listas de nomes e séries para simulação
nomes = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gabriel", "Helena", "Igor", "Juliana"]
series = ["6º ano", "7º ano", "8º ano", "9º ano"]

# Função para gerar notas aleatórias
def gerar_nota():
    return random.randint(0, 10)

# Função para determinar situação
def situacao(notas):
    media = sum(notas) / len(notas)
    return "Aprovado" if media >= 6 else "Reprovado"

# Criando os dados
dados = []
for i in range(10):
    notas = [gerar_nota() for _ in range(5)]  # 5 matérias
    dados.append({
        "nome": nomes[i],
        "serie": random.choice(series),
        "portugues": notas[0],
        "matematica": notas[1],
        "historia": notas[2],
        "geografia": notas[3],
        "educação fisica": notas[4],
        "situação": situacao(notas)
    })

# Criando DataFrame
df = pd.DataFrame(dados)

# Exportando para Excel
df.to_excel("alunos.xlsx", index=False, engine="openpyxl")

print("Arquivo 'alunos.xlsx' criado com sucesso!")
