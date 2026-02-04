""" Exercício 1 – Criando estrutura de pastas
Crie a seguinte estrutura:

├──dados/
│  ├── entrada/
│  └── saida/
├──relatorios/
Crie todas as pastas em uma única execução do seu código."""

from pathlib import Path

# Definindo o caminho base como o diretório atual do script
base= Path(__file__).parent

# Definindo os caminhos das pastas a serem criadas
pasta_dados = base / 'dados' / 'entrada'
pasta_saida = base / 'dados' / 'saida' 
pasta_relatorios = base / 'relatorios'


# Criando as pastas com todos os diretórios pais necessários
pasta_dados.mkdir(parents=True, exist_ok=True)
pasta_saida.mkdir(parents=True, exist_ok=True)
pasta_relatorios.mkdir(parents=True, exist_ok=True) 