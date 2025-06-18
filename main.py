import os
import json
from PIL import Image

pastas_docs = [p for p in os.listdir() if os.path.isdir(p)]
lista_metadata = []
raw_string = "/arquivos/"


def acha_video(path : str): 
    arquivos = os.listdir(path)
    for arquivo in arquivos:
        if (arquivo.endswith(".mp4")):
            return arquivo

def acha_imagem_wide(path : str):
    arquivo_grande = ""
    arquivo_normal = ""
    
    arquivos = os.listdir(path)
    for arquivo in arquivos:
        if (arquivo.endswith(".jpg") or arquivo.endswith(".png")):
            print(os.path.join(path, arquivo))
            im = Image.open(os.path.join(path, arquivo))
            width, height = im.size
            if (width > 1200):
                arquivo_grande = arquivo
            else:
                arquivo_normal = arquivo
    return arquivo_grande, arquivo_normal
                
            
        

for pasta in pastas_docs:
    caminho_metadata = os.path.join(pasta, "metadata.json")
    
    ''' ACHA VIDEO + IMAGEM + IMAGEM_WIDE'''
    
    ''' A PASTA É PASTA CACETE '''

    video_local = acha_video(pasta)
    imagem_wide, imagem_normal = acha_imagem_wide(pasta)

    if os.path.exists(caminho_metadata):
        with open(caminho_metadata, "r+", encoding="utf-8") as f:
            try:
                dados = json.load(f)
                if not isinstance(dados, dict):
                    dados = {}
            except json.JSONDecodeError:
                dados = {}
                
            print(f'{video_local} - {imagem_normal} - {imagem_wide}')

            dados["location"] = raw_string  + pasta + '/' +  video_local
            dados["coverwide"] = raw_string  + pasta + '/' + imagem_wide
            dados["cover"] = raw_string + pasta + '/' + imagem_normal
            
            f.seek(0)
            f.truncate()
            json.dump(dados, f, indent=2, ensure_ascii=False)

            lista_metadata.append(dados)


with open('metadata.json', "w", encoding="utf-8") as file_global:
    json.dump(lista_metadata, file_global, indent=2, ensure_ascii=False)


with open('metadata.json', "r", encoding="utf-8") as f:
    dados = json.load(f)
    print(json.dumps(dados, indent=2, ensure_ascii=False))
