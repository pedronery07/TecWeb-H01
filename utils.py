import json

def extract_route(requisicao):
    return requisicao.split(' ')[1][1:]

def read_file(caminho):
    with open(caminho, "rb") as file:
        return file.read()
    
def load_data(arq_json):
    arq_json = "data/" + arq_json
    with open(arq_json, "r") as file:
        return json.load(file)

def load_template(arquivo):
    arquivo = "templates/" + arquivo
    with open(arquivo, "r") as file:
        return file.read()

def add_note(params):
    # Carregando os dados do arquivo JSON
    with open("data/notes.json", "r") as file:
        dados = json.load(file)
    
    # Adicionando a nova nota aos dados
    nova_nota = {"titulo": params["título"], "detalhes": params["detalhes"]}
    dados.append(nova_nota)

    # Escrevendo os dados atualizados de volta ao arquivo JSON
    with open("data/notes.json", "w") as file:
        json.dump(dados, file)

def build_response(body='', code=200, reason="OK", headers=''):
    if code == 302:
        return f'HTTP/1.1 {code} {reason}\n{headers}\n\n{body}'.encode()
    return f'HTTP/1.1 {code} {reason}\n{headers}\n{body}'.encode()