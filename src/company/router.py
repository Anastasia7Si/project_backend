from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from ..database import get_async_session
from ..dealers.utils import get_dealer_price
from . import schemas, utils
from .exceptions import NoAllProductsException, NoProductException

router = APIRouter(
    prefix='/company',
    tags=['Company']
)


@router.get(
    '/machine-matching/{dealer_product_id}',
    response_model=List[schemas.Product],
    status_code=status.HTTP_200_OK
)
async def matching_matching(
    dealer_product_id: int,
    db: AsyncSession = Depends(get_async_session)
):
    dealer_product = await get_dealer_price(
        db, dealer_product_id
    )
    dealer_product_ids = utils.send_request_ml_matching(
        dealer_product.product_name
    )
    company_products = await utils.get_company_products(
        db, dealer_product_ids
    )
    return company_products


@router.get(
    '/products/',
    response_model=List[schemas.Product],
    status_code=status.HTTP_200_OK
)
async def get_company_products(
    db: AsyncSession = Depends(get_async_session),
    limit: int = None
):
    company_products = await utils.get_matching_company_products(
        db, limit
    )
    if not company_products:
        raise NoAllProductsException()
    return company_products


@router.get(
    '/products/{product_id}/',
    response_model=schemas.Product,
    status_code=status.HTTP_200_OK
)
async def get_one_company_product(
    product_id: int,
    db: AsyncSession = Depends(get_async_session)
):
    company_product = await utils.get_company_product(
        db, product_id
    )
    if not company_product:
        raise NoProductException(id=product_id)
    return company_product


@router.get('/load_csv/')
async def load_csv(db: AsyncSession = Depends(get_async_session)):
    """Эндпоинт для загрузки файлов в базу данных."""

    await utils.load_csv(db)
    return {"detail": "Загружено!"}
