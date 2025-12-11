from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {
        "msg": "hello from fastapi in container"
    }

@app.get("/health")
def health():
    return {
        "ok": True
    }