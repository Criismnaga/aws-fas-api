from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserRequest(BaseModel):
    user: str

@app.get("/")
def read_root():
    return {"mensagem": "Bem-vindo à API da Cris!"}

@app.post("/auth/me", summary="Retorna usuario")
async def auth_me(data : UserRequest):
    return{"user": data.user, "ping": "pong"}