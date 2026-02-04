import openpyxl as px 

# Criando uma nova planilha do Excel
arquivo = px.Workbook()

# Selecionando a planilha ativa
planilha_pessoas = arquivo.active

# Renomeando a planilha ativa
planilha_pessoas.title = "Pessoas"

# Adicionando cabeçalhos às colunas
planilha_pessoas['A1'] = "Nome"
planilha_pessoas['B1'] = "Cidade"

# Adicionando dados às linhas subsequentes, usando indexação de células
planilha_pessoas['A2'] = "João"
planilha_pessoas['B2'] = "Recife"
planilha_pessoas['A3'] = "Maria"
planilha_pessoas['B3'] = "São Paulo"    
planilha_pessoas['A4'] = "Otavio"
planilha_pessoas['B4'] = "Belo Horizonte"

# Adicionando dados às linhas subsequentes, usando o método append
planilha_pessoas.append(["Leticia", "Curitiba"])
planilha_pessoas.append(["Gustavo", "Salvador"])

# Criando uma nova planilha chamada "Visitas"
planilha_visitas = arquivo.create_sheet("Visitas")

# Adicionando cabeçalhos às colunas
planilha_visitas.append(["01/01/2025", 134])
planilha_visitas.append(["02/01/2025", 155])

# Adicionando dados às linhas subsequentes, usando indexação de células
planilha_visitas["b2"] = 142


arquivo.save("Openpyxl\Exercicios\Ex_aula_02\Pessoas.xlsx")
