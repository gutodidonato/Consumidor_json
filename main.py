import os
import json

pastas_docs = [p for p in os.listdir() if os.path.isdir(p)]
lista_metadata = []
raw_string = "../../../Videos/Videos_Housi/Arquivos_Mobile/"

for pasta in pastas_docs:
    caminho_metadata = os.path.join(pasta, "metadata.json")
    video_local = os.path.join(pasta, "1.mp4")

    if os.path.exists(caminho_metadata):
        with open(caminho_metadata, "r+", encoding="utf-8") as f:
            try:
                dados = json.load(f)
                if not isinstance(dados, dict):
                    dados = {}
            except json.JSONDecodeError:
                dados = {}

            dados["location"] = raw_string + os.path.join(pasta, "1.mp4")
            dados["coverwide"] = raw_string + os.path.join(pasta ,"2.png")
            dados["cover"] = raw_string + os.path.join(pasta ,"1.png")
            f.seek(0)
            f.truncate()
            json.dump(dados, f, indent=2, ensure_ascii=False)

            lista_metadata.append(dados)


with open('metadata.json', "w", encoding="utf-8") as file_global:
    json.dump(lista_metadata, file_global, indent=2, ensure_ascii=False)


with open('metadata.json', "r", encoding="utf-8") as f:
    dados = json.load(f)
    print(json.dumps(dados, indent=2, ensure_ascii=False))
