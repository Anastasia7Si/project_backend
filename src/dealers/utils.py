from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from . import models, schemas

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
async def get_dealers_prices(db: AsyncSession, dealer_name: str = None,
                             markup: bool = None,  limit: int = None):
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
        return results.scalars().all()
    results = await db.execute(select(models.DealerPrice).limit(limit))
    return results.scalars().all()


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

async def create_relation_products(db: AsyncSession, product_id: int,
                                   product_key: schemas.ProductDealerKeyCreate):
    product_relation = models.ProductDealerKey(
        key=product_id, **product_key.model_dump())
    db.add(product_relation)
    await db.commit()
    return product_relation


async def get_relation_products(db: AsyncSession):
    results = await db.execute(
        select(
            models.ProductDealerKey
        )
    )
    return results.unique().scalars().all()


async def markup_dealer_price(db: AsyncSession, product_id: int):
    stmt = (
        update(models.DealerPrice).
        where(models.DealerPrice.id == product_id).
        values(markup = True).
        returning(models.DealerPrice)
    )
    result = await db.execute(stmt)
    await db.commit()
    return result.first()


async def unclaimed_dealer_price(db: AsyncSession, product_id: int):
    stmt = (
        update(models.DealerPrice).
        where(models.DealerPrice.id == product_id).
        values(unclaimed = True).
        returning(models.DealerPrice)
    )
    result = await db.execute(stmt)
    await db.commit()
    return result.first()


async def postponed_dealer_price(db: AsyncSession, product_id: int):
    stmt = (
        update(models.DealerPrice).
        where(models.DealerPrice.id == product_id).
        values(postponed = True).
        returning(models.DealerPrice)
    )
    result = await db.execute(stmt)
    await db.commit()
    return result.first()
