from fastapi import FastAPI

from .company.router import router as company_router
from .dealers.router import router as dealers_router


app = FastAPI()


app.include_router(company_router)

app.include_router(dealers_router)
