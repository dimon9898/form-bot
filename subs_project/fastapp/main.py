from fastapi import FastAPI
from fastapp.api_router import api_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_methods=['*'],
    allow_headers=['*']
)

