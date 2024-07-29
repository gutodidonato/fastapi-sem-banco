from typing import Optional

from fastapi import FastAPI

app = FastAPI()


restaurante = {
    1: {"nome": "Restaurante da tia Teteia", "status": "ativo"},
    2: {"nome": "Cantinho do Sabor", "status": "ativo"},
    3: {"nome": "Sabor Familiar", "status": "ativo"},
    4: {"nome": "Rancho da Vovó", "status": "ativo"},
    5: {"nome": "Sabor Caseiro", "status": "ativo"},
}

@app.get("/")
def read_root():
    return {"message": "Bem-vindo ao API de Restaurantes"}

@app.get("/restaurante/{id_restaurante}")
def pegar_restaurante(id_restaurante: int):
    if id_restaurante in restaurante:
        return restaurante[id_restaurante]
    else:
        return {"erro": f"Não existe um Restaurante com o ID {id_restaurante}"}
    

@app.get("/todos-restaurantes/")
def pegar_restaurante():
    return restaurante


@app.post("/inserir-restaurante/{nome_restaurante}-{status}")
def inserir_restaurante(nome_restaurante: str, status: str):
    id_restaurante = len(restaurante) + 1
    restaurante[id_restaurante] = {"nome": nome_restaurante, "status": status}
    return f"{nome_restaurante} criado com sucesso, seus status é {status}"



@app.put("/atualizar-restaurante/{id_restaurante}-{nome_restaurante}-{status}")
def atualizar_restaurante(id_restaurante: int, nome_restaurante: str, status: str):
    print(restaurante)
    if not restaurante[id_restaurante]:
        return "Não existe esse restaurante"
    else:
        restaurante[id_restaurante] = {"nome": nome_restaurante, "status": status}
        return "Restaurante atualizado com sucesso"        


@app.delete("/deletar-restaurante/{id_restaurante}")
def deletar_restaurante(id_restaurante: int):
    if id_restaurante in restaurante:
        del restaurante[id_restaurante]
        return {"Restaurante deletado "}
    else:
        return {"erro": f"Não existe um Restaurante com o ID {id_restaurante}"}

