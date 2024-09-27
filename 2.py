import os

def rename_file(directory, letra_sub, nova_letra):
    for root, dirs, files in os.walk(directory):
        # # print(root)
        # print(dirs)
        # # print(files)
        for arquivo in dirs:
            print(arquivo)
            new_archieve = arquivo.replace(letra_sub, nova_letra)
            old_path = os.path.join(root, arquivo)
            new_path = os.path.join(root, new_archieve)
            if old_path != new_path:
                os.rename(old_path, new_path)
                print(f'Renamed directory: {old_path} -> {new_path}')
                

caminho = 'C:\@trab\ALBUNS  13\AVULSAS'

rename_file(caminho, '�', 'Ã')

