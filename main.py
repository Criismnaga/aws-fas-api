from fastapi import FastAPI
from typing import Optional  # <- importa aqui

app = FastAPI()

@app.get("/")
def read_root():
    return {"mensagem": "Bem-vindo à API da Cris!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
