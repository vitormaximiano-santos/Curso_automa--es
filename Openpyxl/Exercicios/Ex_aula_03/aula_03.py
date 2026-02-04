import openpyxl as px 


# Abrindo o arquivo
arquivo = px.load_workbook('Openpyxl\\Exercicios\\Ex_aula_03\\alunos.xlsx')

# Selecionando a planilha
planilha_alunos = arquivo['Alunos']

notas = planilha_alunos['D']

# Exercício 1

# Imprimindo os valores exatos das células
print(planilha_alunos['B2'].value)
print(planilha_alunos['D5'].value)
print(planilha_alunos['E10'].value)
print('-' * 50)
# Exercício 2

# Percorra toda a coluna “Nota Final” e exiba somente os alunos com nota acima de 8.0
for celula in notas:
    
    # Ignorando o cabeçalho
    if celula.row == 1:
        continue
    
    # Imprimindo os valores exatos das células
    if celula.value > 8.0:
        print(celula.value)
print('-' * 50)

# Exercício 3   

for linha in planilha_alunos.iter_rows(min_row=2,values_only=True):
    
    # desempacotando cada linha, ou seja, obtendo os valores de cada linha e de cada coluna para cada aluno
    nome,curso,idade,nota_final,data_matricula = linha
    print('-' * 50)
    
    # Imprimindo os valores exatos das células
    print(f"""Nome = {nome}
    Curso = {curso}
    Idade = {idade}
    Nota Final = {nota_final}
    Data Matricula = {data_matricula.strftime('%d/%m/%Y')}""") 
    
    # data_matricula é um objeto datetime, precisamos usar o método strftime() para formatar a data para o formato desejado, no caso Dia/Mes/Ano

