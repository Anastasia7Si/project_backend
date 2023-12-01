from enum import Enum
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from ..database import get_async_session
from . import schemas, utils


class AllowQuery(str, Enum):
    markup = 'markup'
    unclaimed = 'unclaimed'
    postponed = 'postponed'


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
                               markup: bool = None,
                               unclaimed: bool = None,
                               limit: int = None,
                               postponed: bool = None):
    print(limit)
    db_products_dealers = await utils.get_dealers_prices(db, dealer_name,
                                                         limit=limit)
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
@router.put('/products/{product_id}/{action}/',
            response_model=schemas.DealerPrice)
async def markup_dealer_product(
                          product_id: int,
                          action: AllowQuery,
                          keys: schemas.ProductDealerKeyCreate | None = None,
                          db: AsyncSession = Depends(get_async_session)):
    if action is AllowQuery.markup:
        if not keys:
            raise HTTPException(status_code=400,
                                detail='Нет тела запроса для markup')
        await utils.markup_dealer_price(db, product_id)
        await utils.create_relation_products(db, product_id, keys)
    if action is AllowQuery.unclaimed:
        await utils.unclaimed_dealer_price(db, product_id)
    if action is AllowQuery.postponed:
        await utils.postponed_dealer_price(db, product_id)
    return await utils.get_dealer_price(db, product_id)


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
    return await utils.get_relation_products(db)


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
