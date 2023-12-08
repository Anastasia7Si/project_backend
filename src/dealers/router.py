from typing import Annotated, List

from fastapi import APIRouter, Body, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from ..database import get_async_session
from . import schemas, utils
from .enum import AllowStatus
from .exceptions import (NoBodyRequestException, NoDealer, NoDealerProduct,
                         NoDealers, NoDealersProducts)

router = APIRouter(
    prefix='/dealers',
    tags=['Dealers']
)


@router.get(
    '/products/',
    response_model=List[schemas.DealerPrice],
    status_code=status.HTTP_200_OK
)
async def get_dealers_products(
    db: AsyncSession = Depends(get_async_session),
    dealer_name: str = None,
    status: AllowStatus = None,
    limit: int = None
):
    """Эндпоинт получения продуктов Дилеров."""

    products_dealers = await utils.get_dealers_prices(
        db,
        dealer_name,
        status,
        limit
    )
    if not products_dealers:
        raise NoDealersProducts()
    return products_dealers


@router.get(
    '/products/{product_id}/',
    response_model=schemas.DealerPrice,
    status_code=status.HTTP_200_OK
)
async def get_dealer_product(
    product_id: int,
    db: AsyncSession = Depends(get_async_session)
):
    """Эндпоинт получения продукта Дилеров."""

    dealer_product = await utils.get_dealer_price(
        db, product_id
    )
    if not dealer_product:
        raise NoDealerProduct(id=product_id)
    return dealer_product


@router.put(
    '/products/{dealer_product_id}/{status}/',
    response_model=schemas.DealerPrice,
    status_code=status.HTTP_200_OK
)
async def status_dealer_product(
    dealer_product_id: int,
    status: AllowStatus,
    company_product_id: Annotated[int, Body(embed=True)] = None,
    serial_number: Annotated[int, Body(embed=True)] = None,
    db: AsyncSession = Depends(get_async_session)
):
    """Эндпоинт изменения статуса разметки продуктов Дилеров."""

    if status is AllowStatus.markup and not (
        serial_number and company_product_id
    ):
        raise NoBodyRequestException()
    await utils.set_status_dealer_product(
        db,
        dealer_product_id,
        status,
        company_product_id,
        serial_number
    )
    return await utils.get_dealer_price(
        db, dealer_product_id
    )


@router.get(
    '/', response_model=List[schemas.Dealer],
    status_code=status.HTTP_200_OK
)
async def get_dealers(
    db: AsyncSession = Depends(get_async_session),
    limit: int = None
):
    """Эндпоинт получения Дилеров."""

    dealers = await utils.get_dealers(db, limit)
    if not dealers:
        raise NoDealers()
    return dealers


@router.get(
    '/{dealer_id}/',
    response_model=schemas.Dealer,
    status_code=status.HTTP_200_OK
)
async def get_dealer(
    dealer_id: int,
    db: AsyncSession = Depends(get_async_session)
):
    """Эндпоинт получения Дилера."""

    dealer = await utils.get_dealer(db, dealer_id)
    if not dealer:
        raise NoDealer(id=dealer_id)
    return dealer
