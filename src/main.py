from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .company.router import router as company_router
from .dealers.router import router as dealers_router

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8001",
    "http://localhost:5173",
    "http://127.0.0.1:8080",
    "http://127.0.0.1:8001",
    "http://127.0.0.1:5173",
    "http://127.0.0.1:1",
    "http://localhost:80",
    "http://127.0.0.1:80",
    "http://localhost:8000",
    "http://127.0.0.1:8000"
]


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(company_router)

app.include_router(dealers_router)
