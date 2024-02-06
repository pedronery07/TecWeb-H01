import json

def extract_route(requisicao):
    primeira_barra = requisicao.index('/')
    http = requisicao.index('HTTP')
    return requisicao[primeira_barra+1:http-1]

def read_file(caminho):
    with open(caminho, 'rb') as file:
        return file.read()
    
def load_data(arq_json):
    arq_json = "data/" + arq_json
    with open(arq_json, 'r') as file:
        return json.load(file)

def load_template(arquivo):
    arquivo = "templates/" + arquivo
    with open(arquivo, 'r') as file:
        return file.read()