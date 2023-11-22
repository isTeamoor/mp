from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import dbActions


app = FastAPI()
app.include_router(dbActions.router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def hello():
    return {'data':'Hi'}