from fastapi import FastAPI

app = FastAPI(
    title="MediSense AI",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to MediSense AI"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }