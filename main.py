#
#Converter todos os arquivos para jpeg
#

from PIL import Image, ImageOps
import os
import pandas as pd

rostos_originais = "originais" # Variavel rostos_originais guarda a pasta originais
rostos_corrigidos = "corrigidos" # Variavel rostos_corrigidos guarda a pasta corrigidos

os.makedirs(rostos_corrigidos, exist_ok = True) # Se a pasta corrigidos já existir, ele não da erro, se não existir ele criará

for file in os.listdir(rostos_originais): # Se existir arquivos ele faz esse loop
    if any(ext in i for ext in ["jpg", "jpeg", "png"] for i in os.listdir(rostos_originais)): # Verifica se tem a extensão correta
        in_path = os.path.join(rostos_originais, file) # Define in_path com o caminho dos arquivos "rostos_originais"
        out_path = os.path.join(rostos_corrigidos, file) # efine in_path com o caminho dos arquivos "rostos_corrigidos"

        imagem = Image.open(in_path).convert("RGB").rotate(90) # Rotaciona a imagem em 90 graus para fotos tirada com o celular em pe
        imagem.save(out_path, format="JPEG") # Salva imagem em formato JPEG

        print(f"Convertido : {file}") # Aparece na tela o arquivo que foi convertido
    else: # Se não...
        print(f"Erro ao converter : {file} : {e}") #Aparece qual arquivo que deu erro e o codigo de erro

#
# A biblioteca cv2 ou OpenCV serve para nos ajudar na leitura da camera
#

import cv2 # Importa a biblioteca do OenCV

def tirar_foto(filename = "foto.jpg"): # Cria a função "tirar_foto"
    camera = cv2.VideoCapture(0) # Define a vaiavel camera para abrir o video0

    if not camera.isOpened(): # Se a camera não abrir
        print("Não foi possivel acessar a webcam") # Aparece mesagem dizendo q nao foi possivel acessar a webcam
        return None # Retorna vazio
    print("Pressione 'Espaço' para capturar a foto ou 'Esc' para cancelar") # Se a camera abrir normalmente aparece essa mensagem

    while True: # Abre um loop

        ret, frame = camera.read() # DEclara uma variavel para fazer a elitura da camera
        if not ret: # Se a camera não conseguir le, então retorna o erro abaixo
            print("Erro: Não foi possivel")
            break # Finaliza o loop
        cv2.imshow("Captura da Webcam", frame) # Abre uma janela como o titulo "Captura da Webcam"

        key = cv2.waitKey(1) # Define a variavel key para exibr um quadro a cada 1ms


        if key == 27: # Se a Tecla ESC for pressionada aparecera a mensagem abaixo
            print("Cancelado")
            break # Finaliza a função
        elif key == ord(' '):  # Le se a Tecla Espaço foi pressionada
            cv2.imwrite(filename, frame) # Salva a imagem capturada
            print(f"Foto capturada e salva como {filename}") # Aparece a mensagem ao lado e o nome que foi salva a imagem
            break

    camera.release() # Libera a captura da imagem
    cv2.destroyAllWindows() # Fecha a janela da Webcam

    return filename # Fecha a função e retorna filename

#
# A Biblioteca Tkinter nos ajuda com a interface grafica, assim nos ajudando para selecionar os arquivos sem precisar digitar o caminho
#

import tkinter as tk # Importa o modulo tkinter 
from tkinter import filedialog # Importa o filedialog para seleção dos arquivos

def selecionar_arquivo(): # Cria uma função para selecionar os arquivos

    root = tk.Tk() # Chama Tk para iniciar a janela
    root.withdraw() # Esconde a janela principal

    arquivo_selecionado = filedialog.askopenfilename( # Abre a janela para o usuaria selecionar o arquivos
        title = "Selecione uma imagem", # O titulo da Janela
        filetypes = [("Imagens", "*.jpg")] # Filtra apenas os arquivos .jpg
    )

    if arquivo_selecionado: # Verifica se o usuario selecionou um arquivo

        print(f"Arquivo Selecionado : {arquivo_selecionado}") # Aparece a mensagem do arquivo selecionado
        return arquivo_selecionado # Fecha a função e retorna "arquivo_selecionado"

#
# A biblioteca deepface nos ajuda com a identificação e comparação de imagens
#

from deepface import DeepFace # Importa o modulo deepface

def reconhecer_rosto_deepface(foto, pasta_rostos): # Chama uma função para reconhecimento dos rostos e comparar a foto com as fotos da pasta
    try: # Aqui mostra que pode gerar uma exceção
        print("Buscando rosto na pasta de rosto conhecidos") # Emite a mensagem de buscando rostos
        resultado = DeepFace.find(img_path = foto, db_path = pasta_rostos, model_name = "Facenet") # Declara uma variavel para facilitar para declarar os caminhos usando modelo facenet

        if resultado[0].shape[0] > 0: # VErifica se foi encontrado o rosto
            nome_arquivo = os.path.basename(resultado[0].iloc[0]['identity']) # Identifica o nome do arquivo da imagem igual
            nome = os.path.splitext(nome_arquivo)[0] # Remove a extensão para aparecer só o nome do arquivo
            print(f"Rosto conhecido como {nome}") # Printa qual foi o nome da foto compativel
            print("Pessoa identificada, acesso liberado") # Libera o acesso a pessoa

        else: # Se não retorno o rosto não reconhecido
            print("Rosto não reconhecido")

    except Exception as e: # Se Ocorrer alguma excessao
        print("Erro ao tentar reconhecer o rosto") # Aarece a mensagem
        uploaded = selecionar_arquivo() # Chama a função para slecionar arquivo
        for nome_arquivo in uploaded.keys(): # Repete os arquivos selecionados
            reconhecer_rosto_deepface(nome_arquivo, pasta_rostos) # Chama a função de novo

##### Continuação do Codigo

escolha = input("Digite 'webcam' para usar a camera ou 'upload' para enviar uma imagem: ").strip().lower() # Aparece para o usuario digitar alguma opção

if escolha == "upload": # Se a escolha for "upload"
    arquivo_foto = selecionar_arquivo() # Delcara variavel para chamar a função "selecionar_arquivos"
    if arquivo_foto: # Se for upload
        rostos_corrigidos = 'C:\\Users\\teusl\\Desktop\\Projeto Faculdade Python\\corrigidos' # Local onde estão as fotos corrigidas
        reconhecer_rosto_deepface(arquivo_foto, rostos_corrigidos) # Chama a função deepface
else: # Se não..
    print("Usando a WebCam") # Mostra a mensagem
    arquivo_foto = tirar_foto() # Declara variavel para chamar a função "tirar_foto"
    rostos_corrigidos = 'C:\\Users\\teusl\\Desktop\\Projeto Faculdade Python\\corrigidos' # Local onde estão as fotos corrigidas
    reconhecer_rosto_deepface(arquivo_foto, rostos_corrigidos) # Chama a função deepface