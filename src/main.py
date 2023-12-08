from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from .company.exceptions import NoAllProductsException, NoProductException
from .company.router import router as company_router
from .dealers.exceptions import (NoBodyRequestException, NoDealer,
                                 NoDealerProduct, NoDealers, NoDealersProducts)
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


app = FastAPI(
    title='Prosept',
    summary='App for matching company and dealers products',
    version='0.0.1',
    license_info={
        'name': 'Prosept',
        'url': 'https://prosept.ru/',
    }
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(company_router)

app.include_router(dealers_router)


@app.exception_handler(NoProductException)
async def no_product_exception_handler(request: Request,
                                       exc: NoProductException):
    return JSONResponse(
        status_code=404,
        content={
            'message': f'Продукта компании с id={exc.id} не существует'
        }
    )


@app.exception_handler(NoAllProductsException)
async def no_all_products_exception_handler(request: Request,
                                            exc: NoAllProductsException):
    return JSONResponse(
        status_code=404,
        content={
            'message': 'В базе данных нет записей продукта компании'
        }
    )


@app.exception_handler(NoDealer)
async def no_dealer_exception_handlers(request: Request,
                                       exc: NoDealer):
    return JSONResponse(
        status_code=404,
        content={
            'message': f'Дилера с id={exc.id} не существует'
        }
    )


@app.exception_handler(NoDealers)
async def no_dealers_exception_handlers(request: Request,
                                        exc: NoDealers):
    return JSONResponse(
        status_code=404,
        content={
            'message': 'В базе данных нет информации о Дилерах'
        }
    )


@app.exception_handler(NoDealerProduct)
async def no_product_dealers_exception_handlers(request: Request,
                                                exc: NoDealerProduct):
    return JSONResponse(
        status_code=404,
        content={
            'message': f'Продукта Дилера с id={exc.id} не существует'
        }
    )


@app.exception_handler(NoDealersProducts)
async def no_products_dealers_exception_handlers(request: Request,
                                                 exc: NoDealersProducts):
    return JSONResponse(
        status_code=404,
        content={
            'message': 'В базе данных нет записей товаров Дилеров'
        }
    )


@app.exception_handler(NoBodyRequestException)
async def no_body_request_exception_handlers(request: Request,
                                             exc: NoBodyRequestException):
    return JSONResponse(
        status_code=400,
        content={
            'message': 'Для разметки необходимо передать '
                       'company_product_id и serial_number'
        }
    )
