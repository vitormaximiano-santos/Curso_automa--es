import shutil
import os

# Criar diretório de backup, se não existir
os.makedirs("Shutil/Aulas/Aula_01/Backup", exist_ok=True)

# Copiar arquivo para o diretório de backup
shutil.copy("Shutil/Aulas/Aula_01/arquivo.txt",
            "Shutil/Aulas/Aula_01/Backup/arquivo_backup.txt")
print("Arquivo copiado com sucesso!")

# Copiar diretório inteiro para o diretório de backup
shutil.copytree("Shutil/Aulas/Aula_01/meus_arquivos", "Shutil/Aulas/Aula_01/Backup/meus_arquivos_backup", dirs_exist_ok=True)
print("Diretório copiado com sucesso!")

if not os.path.exists("Shutil/Aulas/Aula_01/meus_arquivos"):
    os.makedirs("Shutil/Aulas/Aula_01/meus_arquivos")
# Mover arquivo para outro diretório
    shutil.move("Shutil/Aulas/Aula_01/teste.txt", "Shutil/Aulas/Aula_01/meus_arquivos/teste.txt")

# Remover arquivo de backup
shutil.rmtree("C:\\Users\\Vitor\\Desktop\\Python\\Curso_automações\\Shutil\\Aulas\\Aula_01\\Backup\\meus_arquivos_backup")

# Compactar diretório em um arquivo zip
shutil.make_archive("Shutil/Aulas/Aula_01/meus_arquivos_compactado","zip","Shutil/Aulas/Aula_01/meus_arquivos")

shutil.unpack_archive("Shutil/Aulas/Aula_01/meus_arquivos_compactado.zip","Shutil/Aulas/Aula_01/Descompactado","zip")