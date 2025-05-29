from fastapi import FastAPI
from pydantic import BaseModel

# Modelo para o Produto
class Produto(BaseModel):
    nome: str
    preco: float
    em_estoque: bool = True  # valor padrão

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Teste FastAPI!"}

@app.get("/produto/{produto_id}")
def read_item(produto_id: int, q: str = None):
    return {"Id do Produto": produto_id, "Query Parameter": q}

@app.post("/produto/")
def criar_produto(produto: Produto):
    return {"mensagem": "Produto criado com sucesso!", "produto": produto}



