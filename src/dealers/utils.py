from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload, selectinload
from . import models, schemas
from .enum import AllowStatus
from datetime import datetime

# CRUD для Дилера
# Получение Дилера
async def get_dealer(db: AsyncSession, dealer_id: int):
    results = await db.execute(
        select(
            models.Dealer
        ).filter(
            models.Dealer.id == dealer_id
        )
    )
    return results.unique().scalars().first()


# Получение списка Дилеров
async def get_dealers(db: AsyncSession, limit: int):
    results = await db.execute(select(models.Dealer).limit(limit))
    return results.unique().scalars().all()


# Запись Дилера в БД
async def create_dealer(db: AsyncSession, dealer: schemas.DealerCreate):
    db_dealer = models.Dealer(**dealer.model_dump())
    db.add(db_dealer)
    await db.commit()
    return db_dealer


# ## CRUD для продуктов Дилера

# Получение продуктов Дилеров
async def get_dealers_prices(db: AsyncSession, dealer_name: str,
                             status: AllowStatus,  limit: int):
    if dealer_name and status:
        results = await db.execute(
            select(
                models.DealerPrice
            ).join(
                models.Dealer
            ).filter(
                models.Dealer.name == dealer_name,
                models.DealerPrice.status == status.value
            ).limit(limit)
        )
        return results.unique().scalars().all()
    if dealer_name:
        results = await db.execute(
            select(
                models.DealerPrice
            ).join(
                models.Dealer
            ).filter(
                models.Dealer.name == dealer_name
            ).limit(limit)
        )
        return results.unique().scalars().all()
    if status:
        results = await db.execute(
            select(
                models.DealerPrice
            ).join(
                models.Dealer
            ).filter(
                models.DealerPrice.status == status.value
            ).limit(limit)
        )
        return results.unique().scalars().all()
    results = await db.execute(select(models.DealerPrice).limit(limit))
    return results.unique().scalars().all()


# Получение продукта Дилера
async def get_dealer_price(db: AsyncSession, price_id: int):
    results = await db.execute(
        select(
            models.DealerPrice   
        ).filter(
            models.DealerPrice.id == price_id
        )
    )
    return results.unique().scalars().first()


# Запись продукта Дилера в БД
async def create_dealer_price(db: AsyncSession, dealer_price: schemas.DealerPrice):
    db_dealer_price = models.DealerPrice(**dealer_price.model_dump())
    db.add(db_dealer_price)
    await db.commit()
    return db_dealer_price


# ## CRUD для связи продуктов

async def create_relation_products(db: AsyncSession, dealer_product_id: int,
                                   company_product_id: schemas.ProductDealerKeyCreate,
                                   serial_number: int,
                                   status: AllowStatus):
    print(serial_number)
    stmt = (
        update(
            models.DealerPrice
        ).where(
            models.DealerPrice.id == dealer_product_id
        ).values(
            product_id = company_product_id,
            serial_number = serial_number,
            status = status.value,
            date_status = datetime.utcnow()
        ).returning(
            models.DealerPrice
        )
    )
    result = await db.execute(stmt)
    return result


async def get_relation_products(db: AsyncSession):
    results = await db.execute(
        select(
            models.ProductDealerKey
        )
    )
    return results.unique().scalars().all()


async def set_status_dealer_product(db: AsyncSession, dealer_product_id: int, status: AllowStatus, company_product_id = None, serial_number: int = None):
    if status is AllowStatus.markup:
        result = await create_relation_products(db, dealer_product_id, company_product_id, serial_number, status)
    else:
        stmt = (
            update(
                models.DealerPrice
            ).where(
                models.DealerPrice.id == dealer_product_id
            ).values(
                status = status.value,
                product_id = None,
                serial_number = None,
                date_status = datetime.utcnow()
            ).returning(
                models.DealerPrice
            )
        )
        result = await db.execute(stmt)
    await db.commit()
    return result.first()
