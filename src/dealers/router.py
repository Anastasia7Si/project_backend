from typing import List, Annotated

from fastapi import APIRouter, Depends, HTTPException, Body
from sqlalchemy.ext.asyncio import AsyncSession

from ..database import get_async_session
from . import schemas, utils
from .enum import AllowStatus

router = APIRouter(
    prefix='/dealers',
    tags=['Dealers']
)


# ## Продукт Дилера

# Эндпоинт получения продуктов Дилера
@router.get('/products/',
            response_model=List[schemas.DealerPrice])
async def get_dealers_products(db: AsyncSession = Depends(get_async_session),
                               dealer_name: str = None,
                               status: AllowStatus = None,
                               limit: int = None,):
    db_products_dealers = await utils.get_dealers_prices(db, dealer_name, status, limit)
    if db_products_dealers is None:
        raise HTTPException(status_code=404, detail='Not found')
    return db_products_dealers


# Эндпоинт получения 1 продукта Дилера
@router.get('/products/{product_id}/',
            response_model=schemas.DealerPrice)
async def get_dealer_product(product_id: int,
                             db: AsyncSession = Depends(get_async_session)):
    dealer_product = await utils.get_dealer_price(db, product_id)
    if dealer_product is None:
        raise HTTPException(status_code=404, detail='Not found')
    return dealer_product


# Эндпоинт для создания связи и markup продукта дилера
@router.put('/products/{dealer_product_id}/{status}/',
            response_model=schemas.DealerPrice)
async def status_dealer_product(
                          dealer_product_id: int,
                          status: AllowStatus,
                          company_product_id: Annotated[int, Body(embed=True)] = None,
                          serial_number: Annotated[int, Body(embed=True)] = None,
                          db: AsyncSession = Depends(get_async_session)):
    if status is AllowStatus.markup and not (serial_number and company_product_id):
        raise HTTPException(status_code=400, detail='Для разметки необходимо передать company_product_id и serial_number')
    await utils.set_status_dealer_product(db, dealer_product_id, status, company_product_id, serial_number)
    return await utils.get_dealer_price(db, dealer_product_id)


# Эндпоинт записи продукта Дилера
@router.post('/products/',
             response_model=schemas.DealerPrice)
async def create_dealer_product(dealer_product: schemas.DealerPriceCreate,
                                db: AsyncSession = Depends(get_async_session)):
    return await utils.create_dealer_price(db, dealer_product)


# ## Дилер

# Эндпоинт для получения списка Дилеров
@router.get('/', response_model=List[schemas.Dealer])
async def get_dealers(db: AsyncSession = Depends(get_async_session),
                      limit: int = None):
    db_dealers = await utils.get_dealers(db, limit)
    if db_dealers is None:
        raise HTTPException(status_code=404, detail='Not found')
    return db_dealers


# Получение обьекта промежуточной модели
@router.get('/dealerprice/', response_model=List[schemas.ProductDealerKey])
async def get_relation_products(db: AsyncSession = Depends(get_async_session)):
    result = await utils.get_relation_products(db)
    return result


# Эндпоинт для получения 1 Дилера
@router.get('/{dealer_id}/',
            response_model=schemas.Dealer)
async def get_dealer(dealer_id: int,
                     db: AsyncSession = Depends(get_async_session)):
    db_dealer = await utils.get_dealer(db, dealer_id)
    if db_dealer is None:
        raise HTTPException(status_code=404, detail='Not found')
    return db_dealer


# Эндпоинт для записи Дилера в БД
@router.post('/', response_model=schemas.Dealer)
async def create_dealer(dealer: schemas.DealerCreate,
                        db: AsyncSession = Depends(get_async_session)):
    return await utils.create_dealer(db, dealer)
