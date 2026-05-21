"""Simple FastAPI app for PR workflow lab."""
from fastapi import FastAPI

app = FastAPI(title="PR Lab")


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.get("/divide")
def divide(a: int, b: int) -> dict:
    # 故意 bug:沒驗證 b != 0
    return {"result": a / b}


@app.get("/multiply")
def multiply(a: int, b: int) -> dict:
    """Multiply a by b."""
    return {"result": a * b}
