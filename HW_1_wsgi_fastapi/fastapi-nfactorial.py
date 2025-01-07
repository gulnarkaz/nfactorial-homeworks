from fastapi import FastAPI
import math

app = FastAPI()

@app.get("/{num}")
def nfactorial(num: int):
    return {"nfactorial": math.factorial(num)}

