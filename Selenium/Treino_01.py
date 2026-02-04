# importa a biblioteca Selenium e o módulo time
from selenium import webdriver
import time


# importa módulos adicionais do Selenium
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# inicia o navegador Chrome
navegador = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
time.sleep(2)

# navega para o site da Hashtag Treinamentos
navegador.get("https://www.hashtagtreinamentos.com")

# localiza o botão verde na página pelo nome da classe CSS
botao_verde = navegador.find_element("class name", "botao-verde")

# realiza o clique no botão verde
botao_verde.click()

# localiza todos os botões com a classe "header-titulo"
botoes = navegador.find_elements("class name", "header-titulo")

# itera sobre os botões para encontrar o que tem
# o texto "Assinatura" e clica nele .
for botao in botoes:
    if botao.text == "Assinatura":
        botao.click()
        break

# troca para a nova aba aberta
abas=navegador.window_handles
navegador.switch_to.window(abas[1])

# navega para a página do curso de Python
navegador.get("https://www.hashtagtreinamentos.com/curso-python?")

# maximiza a janela do navegador
navegador.maximize_window()

# preenche o formulário de inscrição
navegador.find_element("id","firstname").send_keys("Vitor")
navegador.find_element("id","email").send_keys("Vitor@gmail.com")
navegador.find_element("id","phone").send_keys("11999999999")

# localiza o botão de envio do formulário
envio_formulario= navegador.find_element("id","_form_2475_submit")

# rola a página até o botão de envio do formulário
navegador.execute_script("arguments[0].scrollIntoView({block: 'center'})",
                         envio_formulario)

# espera até que o botão de envio do formulário esteja clicável
aguarde = WebDriverWait(navegador, 10)
aguarde.until(EC.element_to_be_clickable(envio_formulario))

# clica no botão de envio do formulário
envio_formulario.click()

time.sleep(15)