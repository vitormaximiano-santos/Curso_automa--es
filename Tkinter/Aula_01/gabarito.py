import requests
from tkinter import *


# para usar o seu codigo no Tkinter, coloque-o dentro de uma função

# Função para pegar as cotações
def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")  # requisição para a API

    requisicao_dic = requisicao.json() # converte a resposta em um dicionário

    # Pega as cotações
    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    # Atualiza o texto com as cotações
    texto_resposta['text'] = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''


# Cria janela e configura a janela
janela = Tk() # cria janela
janela.title("Cotação Atual de Moedas") # título da janela
texto = Label(janela, text="Clique no botão para ver as cotações de moedas") # texto para exibir
texto.grid(column=0, row=0, padx=10, pady=10) # posiciona o texto na janela

# Cria botão para pegar as cotações
botao = Button(janela, text="Buscar cotações", command=pegar_cotacoes) # cria botão
botao.grid(column=0, row=1, padx=10, pady=10) # posiciona o botão na janela

texto_resposta = Label(janela, text="") # cria texto para exibir as cotações
texto_resposta.grid(column=0, row=2, padx=10, pady=10) # posiciona o texto na janela


janela.mainloop()