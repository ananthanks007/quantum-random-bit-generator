from fastapi import FastAPI
from qrbg import quantum_random_bit

app = FastAPI()

@app.get("/qrbg")
def qrbg(bits: int = 32):
    random_bit = quantum_random_bit(bits)
    return {"random_bit": random_bit}
