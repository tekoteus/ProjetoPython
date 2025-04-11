#
#Converter todos os arquivos para jpeg
#

from PIL import Image, ImageOps
import os
import pandas as pd

rostos_originais = "originais" # Variavel rostos_originais guarda a pasta originais
rostos_corrigidos = "corrigidos"

os.makedirs(rostos_corrigidos, exist_ok = True) #Se a pasta corrigidos já existir, ele não da erro, se não existir ele criará

for file in os.listdir(rostos_originais): #Se existir arquivos ele faz esse loop
    if any(ext in i for ext in ["jpg", "jpeg", "png"] for i in os.listdir(rostos_originais)): #Verifica se tem a extensão correta
        in_path = os.path.join(rostos_originais, file) #Define in_path com o caminho dos arquivos "rostos_originais"
        out_path = os.path.join(rostos_corrigidos, file) #Define in_path com o caminho dos arquivos "rostos_corrigidos"

        imagem = Image.open(in_path).convert("RGB").rotate(90)
        imagem.save(out_path, format="JPEG")

        print(f"Convertido : {file}")
    else:
        print(f"Erro ao converter : {file} : {e}")




import cv2

def tirar_foto(filename = "foto.jpg"):
    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        print("Não foi possivel acessar a webcam")
        return None
    print("Pressione 'Espaço' para capturar a foto ou 'Esc' para cancelar")

    while True:

        ret, frame = camera.read()
        if not ret:
            print("Erro: Não foi possivel")
            break
        cv2.imshow("Captura da Webcam", frame)

        key = cv2.waitKey(1)


        if key == 27: #Tecla ESC
            print("Cancelado")
            break
        elif key == ord(' '):  # Tecla Espaço
            # Salva a imagem capturada
            cv2.imwrite(filename, frame)
            print(f"Foto capturada e salva como {filename}")
            break

    camera.release()
    cv2.destroyAllWindows()

    return filename





import tkinter as tk
from tkinter import filedialog

def selecionar_arquivo():

    root = tk.Tk()
    root.withdraw()

    arquivo_selecionado = filedialog.askopenfilename(
        title = "Selecione uma imagem",
        filetypes = [("Imagens", "*.jpg")]
    )

    if arquivo_selecionado:

        print(f"Arquivo Selecionado : {arquivo_selecionado}")
        return arquivo_selecionado


from deepface import DeepFace

def reconhecer_rosto_deepface(foto, pasta_rostos):
    try:
        print("Buscando rosto na pasta de rosto conhecidos")
        resultado = DeepFace.find(img_path = foto, db_path = pasta_rostos, model_name = "Facenet")

        if resultado[0].shape[0] > 0:
            nome_arquivo = os.path.basename(resultado[0].iloc[0]['identity'])
            nome = os.path.splitext(nome_arquivo)[0]
            print(f"Rosto conhecido como {nome}")
            print("Pessoa identificada, acesso liberado")

        else:
            print("Rosto não reconhecido")

    except Exception as e:
        print("Erro ao tentar reconhecer o rosto")

        uploaded = selecionar_arquivo()
        for nome_arquivo in uploaded.keys():
            reconhecer_rosto_deepface(nome_arquivo, pasta_rostos)




escolha = input("Digite 'webcam' para usar a camera ou 'upload' para enviar uma imagem: ").strip().lower()

if escolha == "upload":
    arquivo_foto = selecionar_arquivo()
    if arquivo_foto:
        rostos_corrigidos = 'C:\\Users\\teusl\\Desktop\\Projeto Faculdade Python\\corrigidos'
        reconhecer_rosto_deepface(arquivo_foto, rostos_corrigidos)
else:
    print("Usando a WebCam")
    arquivo_foto = tirar_foto()

    rostos_corrigidos = 'C:\\Users\\teusl\\Desktop\\Projeto Faculdade Python\\corrigidos'
    reconhecer_rosto_deepface(arquivo_foto, rostos_corrigidos)









