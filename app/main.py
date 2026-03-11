from fastapi import FastAPI
from app.routers.standards import router as standards_router

app = FastAPI(title="Standards API")
app.include_router(standards_router)

@app.get("/")
def root():
    return {"message": "Standards API is running"}
