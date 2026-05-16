from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Passando o número 1 e 2 na URL
@app.get("/soma/{numero1}/{numero2}")
def soma(numero1: int, numero2: int):
    total = numero1 + numero2
    return {"resultado": total}


@app.post("/soma_formato2")
def soma_formato2(numero1: int, numero2: int):
    total = numero1 + numero2
    return {"resultado": total}


# Passando o número 1 e 2 no corpo da requisição
class Numeros(BaseModel):
    numero1: int
    numero2: int

@app.post("/soma_formato3",response_model=Resultado,
summary="API para somar")
def soma_formato3(numeros: Numeros):
    total = numeros.numero1 + numeros.numero2
    return {"resultado": total}
