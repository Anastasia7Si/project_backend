from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from ..database import get_async_session
from ..dealers.utils import get_dealer_price
from . import schemas, utils


router = APIRouter(
    prefix='/company',
    tags=['Company']
)


@router.get('/machine-matching/{dealer_product_id}',
            response_model=List[schemas.Product])
async def matching_matching(dealer_product_id: int,
                            db: AsyncSession = Depends(get_async_session)):
    """Эндпоинт запроса результатов ML."""

    dealer_product = await get_dealer_price(db, dealer_product_id)
    dealer_product_ids = utils.send_request_ml_matching(
        dealer_product.product_name
        )
    company_products = await utils.get_dealer_products(db, dealer_product_ids)
    return company_products


@router.get('/products/',
            response_model=List[schemas.Product])
async def get_company_product(db: AsyncSession = Depends(get_async_session),
                              limit: int = None):
    """Эндпоинт получения одного продуктов Компании."""

    company_products = await utils.get_company_products(db, limit)
    if company_products is None:
        raise HTTPException(status_code=404, detail='Not found')
    return company_products


@router.get('/products/{product_id}/',
            response_model=schemas.Product)
async def get_one_company_product(product_id: int,
                                  db: AsyncSession = Depends(
                                      get_async_session)):
    """Эндпоинт получения одного продукта Компании."""

    company_product = await utils.get_company_product(db, product_id)
    if company_product is None:
        raise HTTPException(status_code=404, detail='Not found')
    return company_product


@router.get('/load_csv/')
async def load_csv(db: AsyncSession = Depends(get_async_session)):
    """Эндпоинт для загрузки файлов в базу данных."""

    await utils.load_csv(db)
    return {"detail": "Загружено!"}
