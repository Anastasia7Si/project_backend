from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .company.router import router as company_router
from .dealers.router import router as dealers_router

origins = [
    "http://proseptmatching.zapto.org:3000",
    "http://proseptmatching.zapto.org:8080",
    "http://proseptmatching.zapto.org:8001",
    "http://proseptmatching.zapto.org:5173",
    "http://proseptmatching.zapto.org",
    "http://ds_ml:8001",
    "http://ds_ml"
]


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie",
                   "Access-Control-Allow-Headers",
                   "Access-Control-Allow-Origin",
                   "Authorization"],
)


app.include_router(company_router)

app.include_router(dealers_router)
