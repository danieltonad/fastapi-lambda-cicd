from fastapi import FastAPI
from mangum import Mangum

app = FastAPI(title="Yo!")

handler = Mangum(app=app)

@app.get('/')
async def root():
    return "Lambda CICD + Git Actions (FastAPI)"