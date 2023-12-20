import os
import shutil
#'Imagens': ['.gif', '.png', '.jpg', '.jpeg', '.jfif'],
#'Vídeos': ['.mp4', '.avi', '.mkv', '.mov'],
#'Documentos': ['.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx'],
#'Áudios': ['.mp3', '.wav', '.ogg']

from_dir = "C:/Users/luizg/Downloads"
to_dir = "C:/Users/luizg/Downloads"

list_of_files = os.listdir(from_dir)
print(list_of_files)

# Mova todos os arquivos de imagem da pasta Downloads para outra pasta
for file_name in list_of_files:

    name, extension = os.path.splitext(file_name)
    #print(name)
    #print(extension)

    if extension == '':
        continue
    if extension in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:

        path1 = from_dir + '/' + file_name                         # Exemplo path1 : Downloads/nomeImagem1.jpg        
        path2 = to_dir + '/' + "Imagem"                   # Exemplo path2 : D:/Meus Arquivos/Arquivos_Imagem      
        path3 = to_dir + '/' + "Imagem" + '/' + file_name # Exemplo path3 : D:/Meus Arquivos/Arquivos_Imagem/nomeImagem1.jpg
        #print("path1 " , path1)
        #print("path3 ", path3)

        # Verifique se o caminho da pasta/diretório existe antes de mover
        # Caso contrário, crie uma NOVA pasta/diretório, e então mova
        if os.path.exists(path2):
          print("Movendo " + file_name + ".....")

          # Mover de path1 ---> path3
          shutil.move(path1, path3)

        else:
          os.makedirs(path2)
          print("Movendo " + file_name + ".....")
          shutil.move(path1, path3)
    if extension in ['.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx']:
        path1 = from_dir + '/' + file_name                         # Exemplo path1 : Downloads/nomeImagem1.jpg        
        path2 = to_dir + '/' + "Documentos"                   # Exemplo path2 : D:/Meus Arquivos/Arquivos_Imagem      
        path3 = to_dir + '/' + "Documentos" + '/' + file_name # Exemplo path3 : D:/Meus Arquivos/Arquivos_Imagem/nomeImagem1.jpg
        if os.path.exists(path2):
          print("Movendo " + file_name + ".....")
          shutil.move(path1, path3)
        else:
          os.makedirs(path2)
          print("Movendo " + file_name + ".....")
          shutil.move(path1, path3)
    if extension in ['.mp4', '.avi', '.mkv', '.mov']:
        path1 = from_dir + '/' + file_name                         # Exemplo path1 : Downloads/nomeImagem1.jpg        
        path2 = to_dir + '/' + "Videos"                   # Exemplo path2 : D:/Meus Arquivos/Arquivos_Imagem      
        path3 = to_dir + '/' + "Videos" + '/' + file_name # Exemplo path3 : D:/Meus Arquivos/Arquivos_Imagem/nomeImagem1.jpg
        if os.path.exists(path2):
          print("Movendo " + file_name + ".....")
          shutil.move(path1, path3)
        else:
          os.makedirs(path2)
          print("Movendo " + file_name + ".....")
          shutil.move(path1, path3)
    if extension in ['.mp3', '.wav', '.ogg']:
        path1 = from_dir + '/' + file_name                         # Exemplo path1 : Downloads/nomeImagem1.jpg        
        path2 = to_dir + '/' + "Audios"                   # Exemplo path2 : D:/Meus Arquivos/Arquivos_Imagem      
        path3 = to_dir + '/' + "Audios" + '/' + file_name # Exemplo path3 : D:/Meus Arquivos/Arquivos_Imagem/nomeImagem1.jpg
        if os.path.exists(path2):
          print("Movendo " + file_name + ".....")
          shutil.move(path1, path3)
        else:
          os.makedirs(path2)
          print("Movendo " + file_name + ".....")
          shutil.move(path1, path3)
    if extension in ['.zip', '.rar', '.7z', '.tar', '.tgz']:
        path1 = from_dir + '/' + file_name                         # Exemplo path1 : Downloads/nomeImagem1.jpg        
        path2 = to_dir + '/' + "Compactados"                   # Exemplo path2 : D:/Meus Arquivos/Arquivos_Imagem      
        path3 = to_dir + '/' + "Compactados" + '/' + file_name # Exemplo path3 : D:/Meus Arquivos/Arquivos_Imagem/nomeImagem1.jpg
        if os.path.exists(path2):
          print("Movendo " + file_name + ".....")
          shutil.move(path1, path3)
        else:
          os.makedirs(path2)
          print("Movendo " + file_name + ".....")
          shutil.move(path1, path3)
    if extension in ['.exe', '.bin', '.cmd', '.msi', '.dmg']:
        path1 = from_dir + '/' + file_name                         # Exemplo path1 : Downloads/nomeImagem1.jpg        
        path2 = to_dir + '/' + "Setup"                   # Exemplo path2 : D:/Meus Arquivos/Arquivos_Imagem      
        path3 = to_dir + '/' + "Setup" + '/' + file_name # Exemplo path3 : D:/Meus Arquivos/Arquivos_Imagem/nomeImagem1.jpg
        if os.path.exists(path2):
          print("Movendo " + file_name + ".....")
          shutil.move(path1, path3)
        else:
          os.makedirs(path2)
          print("Movendo " + file_name + ".....")
          shutil.move(path1, path3)