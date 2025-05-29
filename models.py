from pydantic import BaseModel

# Modelo para o Produto
class Produto(BaseModel):
    nome: str
    preco: float
    em_estoque: bool = True  # valor padrão