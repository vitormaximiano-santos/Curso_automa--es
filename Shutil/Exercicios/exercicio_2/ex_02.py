"""2. Mover e renomear arquivos automaticamente
Crie um script que:

Verifica se existe um arquivo chamado relatorio.txt.

Move esse arquivo para uma pasta chamada relatorios_antigos.

Durante a movimentação, renomeie o arquivo para relatorio_backup.txt."""

from pathlib import Path
import shutil

# Caminho do arquivo relatorio.txt
relatorio = Path("Shutil/Exercicios/exercicio_2/relatorio.txt")

# Verifica se o arquivo relatorio.txt existe
relatorio_antigo = Path("Shutil/Exercicios/exercicio_2/relatorio_antigos")

# Criar a pasta relatorios_antigos se não existir
relatorio_antigo.mkdir(parents=True, exist_ok=True)

# Mover e renomear o arquivo relatorio.txt
shutil.move(relatorio, relatorio_antigo / "relatorio_backup.txt")