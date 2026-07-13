from fastapi import FastAPI
from datetime import datetime

app = FastAPI(title="FastAPI + Docker", version="1.0.0")

@app.get("/")
def root():
    return {"message": "🚀 Автодеплой работает! v2"}

@app.get("/health")
def health():
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

@app.get("/time")
def get_time():
    return {"current_time": datetime.now().isoformat()}

@app.get("/multiply/{a}/{b}")
def multiply(a: int, b: int):
    return {"result": a * b}

@app.get("/divide/{a}/{b}")
def divide(a: int, b: int):
    if b == 0:
        return {"error": "Деление на ноль"}, 400
    return {"result": a / b}