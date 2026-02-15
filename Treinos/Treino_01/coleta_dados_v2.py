from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import openpyxl as px

# Carregar dados do Excel
arquivo = px.load_workbook(r'Treinos\Treino_01\alunos.xlsx')
planilha_alunos = arquivo['Sheet1']

# Criar lista para armazenar os dados dos alunos
alunos = []

# Iterar sobre as linhas do Excel (ignorando "portugues")
for linha in planilha_alunos.iter_rows(values_only=True, min_row=2):
    nome, serie, _, matematica, historia, geografia, educacao_fisica, situacao = linha
    alunos.append({
        "nome": nome,
        "serie": serie,
        "matematica": matematica,
        "historia": historia,
        "geografia": geografia,
        "educacao_fisica": educacao_fisica,
        "situacao": situacao
    })

# Iniciar navegador
driver = webdriver.Chrome()
driver.get("https://forms.office.com/r/Kjm6aRCYYm")  # coloque o link do seu formulário

time.sleep(3)  # esperar carregar

for aluno in alunos:
    # Localizar todos os campos de texto (na ordem que aparecem)
    campos = driver.find_elements(By.XPATH, '//input[@data-automation-id="textInput"]')

    # Preencher dinamicamente os campos com os valores do aluno
    valores = [
        aluno["nome"],
        aluno["serie"],
        aluno["matematica"],
        aluno["historia"],
        aluno["geografia"],
        aluno["educacao_fisica"]
    ]

    for campo, valor in zip(campos, valores):
        campo.send_keys(str(valor))

    # Campo de opção (radio button) para situação
    if aluno["situacao"].lower() == "aprovado":
        driver.find_element(By.XPATH, '//input[@type="radio" and @value="Aprovado"]').click()
    else:
        driver.find_element(By.XPATH, '//input[@type="radio" and @value="Reprovado"]').click()

    # Enviar formulário
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # rolar para o final
    time.sleep(1)
    botao_enviar = driver.find_element(By.XPATH, '//button[@data-automation-id="submitButton"]')
    botao_enviar.click()

    time.sleep(2)  # esperar envio antes de passar para o próximo

    # Reabrir o formulário para o próximo aluno
    driver.get("https://forms.office.com/r/Kjm6aRCYYm")
    time.sleep(2)
