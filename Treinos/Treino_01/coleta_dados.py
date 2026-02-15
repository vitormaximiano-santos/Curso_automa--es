from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import openpyxl as px

# Carregar dados do Excel
arquivo = px.load_workbook(r'Treinos\Treino_01\alunos.xlsx')
planilha_alunos = arquivo['Sheet1']

# Criar lista para armazenar os dados dos alunos
alunos = []

# Iterar sobre as linhas do Excel
for linha in planilha_alunos.iter_rows(values_only=True, min_row=2):
    nome, serie, portugues, matematica, historia, geografia, educacao_fisica, situacao = linha
    alunos.append({
        "nome": nome,
        "serie": serie,
        "portugues": portugues,
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

    # Preencher cada campo com os dados do aluno
    campos[0].send_keys(aluno["nome"])
    campos[1].send_keys(aluno["serie"])
    campos[2].send_keys(str(aluno["portugues"]))
    campos[3].send_keys(str(aluno["matematica"]))
    campos[4].send_keys(str(aluno["historia"]))
    campos[5].send_keys(str(aluno["geografia"]))
    campos[6].send_keys(str(aluno["educacao_fisica"]))

    # Campo de opção (radio button) para situação
    if aluno["situacao"].lower() == "aprovado":
        driver.find_element(By.XPATH, '//input[@type="radio" and @value="Aprovado"]').click()
    
    else:
        driver.find_element(By.XPATH, '//input[@type="radio" and @value="Reprovado"]').click()


# Enviar formulário
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # rolar para o final
    time.sleep(1)  # esperar o scroll terminar
    botao_enviar = driver.find_element(By.XPATH, '//button[@data-automation-id="submitButton"]')  # localizar o botão de envio
    botao_enviar.click()  # clicar no botão de envio

    time.sleep(2)  # esperar envio antes de passar para o próximo

    driver.get("https://forms.office.com/r/Kjm6aRCYYm")  # reabrir o formulário para o próximo aluno
    time.sleep(2)
