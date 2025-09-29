from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def read_root():
    return {"mensagem": "Bem-vindo à API da Cris!"}

@app.post("/auth/me")
async def auth_me(request : Request):
    body = await request.json()
    usuario = body.get("user", "desconhecido")
    return{"user": usuario, "ping": "pong"}