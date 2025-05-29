✅ Documentação - API FastAPI Básica

📌 1. Requisitos:
- Python 3.8+ instalado
- pip instalado

📌 2. Criar e ativar ambiente virtual:

# Criar a venv
- python -m venv venv

# Ativar (Windows)
- venv\Scripts\activate

# Ativar (Linux/macOS)
- source venv/bin/activate

📌 3. Instalar dependências:
- pip install fastapi uvicorn

📌 4. Rodar o servidor:
# Rodar o Servidor
- uvicorn main:app --reload

📌 5. Acessar a API:
# URL base:
- http://127.0.0.1:8000

📌 6. Acessar a documentação automática:
# Swagger UI:
- http://127.0.0.1:8000/docs

# ReDoc:
- http://127.0.0.1:8000/redoc