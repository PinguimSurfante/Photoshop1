import os
import shutil


def montagem(caminho):
    for root, dirs, file in os.walk(caminho):
        #* se tiver um diretorio chamado montagem
        if 'Montagem' in dirs:
            #* caminho para a pasta 'Montagem'
            pasta_montagem = os.path.join(root, 'Montagem')
            
            #* Pasta anterior da Montagem
            pasta_anterior = os.path.dirname(pasta_montagem)
            # print(pasta_anterior)

            #* entrar na pasta montagem, e mover os arquivos e substituir os da pasta anterior de Montagem
            for arquivo in os.listdir(pasta_montagem):

                caminho_arquivo_montagem = os.path.join(pasta_montagem, arquivo)

                caminho_arquivo = os.path.join(pasta_anterior, arquivo)
                #* Para usar o shutil tem q encontrar as localizaçao das pastas
                shutil.move(caminho_arquivo_montagem, caminho_arquivo)

                print(f'Arquivo {arquivo} movido para {pasta_anterior}')


pasta_01 = 'Coloca o lugar na sua pasta'

montagem(pasta_01) 