from fastapi import FastAPI

app = FastAPI(title="Digital Fortune Cookie API")

@app.get("/")
def health_check():
    return {"status": "ok"}