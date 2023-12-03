from fastapi import FastAPI

from .company.router import router as company_router
from .dealers.router import router as dealers_router

from fastapi.middleware.cors import CORSMiddleware


origins = [
    '*',
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
