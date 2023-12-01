from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from . import models, schemas

### CRUD

#Получение продуктов Компании
async def get_company_products(db: AsyncSession, limit: int):
    result = await db.execute(
        select(
            models.Product
        ).limit(limit)
    )
    return result.scalars().all()


#Получение продукта Компании
async def get_company_product(db: AsyncSession, product_id: int):
    result = await db.execute(
        select(
            models.Product
        ).filter(
            models.Product.id == product_id
        )
    )
    return result.scalars().first()


#Запись продукта Компании
async def create_company_product(db: AsyncSession, product: schemas.ProductCreate):
    company_product = models.Product(**product.model_dump())
    db.add(company_product)
    await db.commit()
    return company_product
