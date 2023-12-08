from datetime import datetime

from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from . import models
from .enum import AllowStatus


async def get_dealer(db: AsyncSession,
                     dealer_id: int):
    """Функция получения Дилера."""

    stmt = select(
        models.Dealer
    ).filter(
        models.Dealer.id == dealer_id
    )
    results = await db.execute(stmt)
    return results.unique().scalars().first()


async def get_dealers(db: AsyncSession,
                      limit: int):
    """Функция получения Дилеров."""

    stmt = select(
        models.Dealer
    ).limit(
        limit
    )
    results = await db.execute(stmt)
    return results.unique().scalars().all()


async def prices_by_name_and_status(db: AsyncSession,
                                    dealer_name: str,
                                    status: AllowStatus,
                                    limit: int):
    """Функция получения продуктов Дилера по статусу и имени."""

    stmt = select(
        models.DealerPrice
    ).join(
        models.Dealer
    ).filter(
        models.Dealer.name == dealer_name,
        models.DealerPrice.status == status.value
    ).limit(limit)
    products = await db.execute(stmt)
    return products.unique().scalars().all()


async def prices_by_name(db: AsyncSession,
                         dealer_name: str,
                         limit: str):
    """Функция получения продуктов Дилера по статусу."""

    stmt = select(
        models.DealerPrice
    ).join(
        models.Dealer
    ).filter(
        models.Dealer.name == dealer_name
    ).limit(limit)
    products = await db.execute(stmt)
    return products.unique().scalars().all()


async def prices_by_status(db: AsyncSession,
                           status: AllowStatus,
                           limit: int):
    """Функция получения продуктов Дилера по статусу."""

    stmt = select(
        models.DealerPrice
    ).join(
        models.Dealer
    ).filter(
        models.DealerPrice.status == status.value
    ).limit(limit)
    products = await db.execute(stmt)
    return products.unique().scalars().all()


async def get_dealers_prices(db: AsyncSession, dealer_name: str,
                             status: AllowStatus, limit: int):
    """Функция получения продуктов Дилера."""

    if dealer_name and status:
        return await prices_by_name_and_status(
            db,
            dealer_name,
            status,
            limit
        )
    if dealer_name:
        return await prices_by_name(
            db,
            dealer_name,
            limit
        )
    if status:
        return await prices_by_status(
            db,
            status,
            limit
        )
    stmt = select(
        models.DealerPrice
    ).limit(limit)
    results = await db.execute(stmt)
    return results.unique().scalars().all()


async def get_dealer_price(db: AsyncSession,
                           price_id: int):
    """Функция получения продуктов Дилера по id."""

    results = await db.execute(
        select(
            models.DealerPrice
        ).filter(
            models.DealerPrice.id == price_id
        )
    )
    return results.unique().scalars().first()


async def set_markup_products(db: AsyncSession,
                              dealer_product_id: int,
                              company_product_id: int,
                              serial_number: int,
                              status: AllowStatus):
    """Функция изменения продуктов Дилера по статусу."""

    stmt = (
        update(
            models.DealerPrice
        ).where(
            models.DealerPrice.id == dealer_product_id
        ).values(
            product_id=company_product_id,
            serial_number=serial_number,
            status=status.value,
            date_status=datetime.utcnow()
        ).returning(
            models.DealerPrice
        )
    )
    result = await db.execute(stmt)
    return result


async def set_status_dealer_product(db: AsyncSession,
                                    dealer_product_id: int,
                                    status: AllowStatus,
                                    company_product_id: int,
                                    serial_number: int):
    """Функция изменения продуктов Дилера."""

    if status is AllowStatus.markup:
        result = await set_markup_products(
            db,
            dealer_product_id,
            company_product_id,
            serial_number,
            status
        )
    else:
        stmt = (
            update(
                models.DealerPrice
            ).where(
                models.DealerPrice.id == dealer_product_id
            ).values(
                status=status.value,
                product_id=None,
                serial_number=None,
                date_status=datetime.utcnow()
            ).returning(
                models.DealerPrice
            )
        )
        result = await db.execute(stmt)
    await db.commit()
    return result.first()
