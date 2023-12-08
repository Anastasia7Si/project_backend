
import requests
from typing import List

from sqlalchemy.ext.asyncio import AsyncSession

from . import models


from sqlalchemy import func, select


async def get_company_products(db: AsyncSession,
                               limit: int):
    """Функция получения продуктов Компании."""

    stmt = select(models.Product).limit(limit)
    result = await db.execute(stmt)
    await db.commit()
    return result.unique().scalars().all()


async def get_company_product(db: AsyncSession,
                              product_id: int):
    """Функция получения продукта Компании."""
    stmt = select(
        models.Product
    ).filter(
        models.Product.id == product_id
    )
    result = await db.execute(stmt)
    return result.scalars().first()


def send_request_ml_matching(dealer_product_name: str):
    """Функция отправки запроса к ML."""
    payload = {'name_dealer_product': dealer_product_name}
    response = requests.post(
        'http://ds_ml:8001/machine-matching',
        json=payload
    )
    product_ids = response.json()
    return product_ids


async def get_matching_company_products(db: AsyncSession,
                                        dealer_ids: List[int]):
    """Функция получения результатов от ML."""

    stmt = select(
        models.Product
    ).order_by(
        func.array_position(
            dealer_ids,
            models.Product.id
        )
    )
    result = await db.execute(stmt)
    return result.unique().scalars().all()
