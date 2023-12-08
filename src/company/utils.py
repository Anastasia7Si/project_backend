import csv
import requests
from typing import List

import aiofiles
import requests

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from ..dealers.models import Dealer, DealerPrice
from . import models


async def get_company_products(db: AsyncSession,
                               limit: int):
    stmt = select(models.Product).limit(limit)
    result = await db.execute(stmt)
    await db.commit()
    return result.unique().scalars().all()


async def get_company_product(db: AsyncSession,
                              product_id: int):
    stmt = select(
        models.Product
    ).filter(
        models.Product.id == product_id
    )
    result = await db.execute(stmt)
    return result.scalars().first()


def send_request_ml_matching(dealer_product_name: str):
    payload = {'name_dealer_product': dealer_product_name}
    response = requests.post(
        'http://localhost:8001/machine-matching',
        json=payload
    )
    product_ids = response.json()
    return product_ids


async def get_matching_company_products(db: AsyncSession,
                                        dealer_ids: List[int]):
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


async def load_csv(db: AsyncSession):
    async with aiofiles.open(
        '*your_path*',
        mode='r',
        newline='',
        encoding='UTF-8'
    ) as file:
        content = await file.read()
        content = content.replace('\r\n', '\n')
        reader = csv.DictReader(
            content.splitlines(),
            delimiter=';'
        )
        for row in reader:
            record = models.Product(
                id=int(row['id']),
                article=row['article'],
                ean_13=row['ean_13'],
                name=row['name'],
                cost=float(
                    row['cost']
                ) if row['cost'] != '' else None,
                recommended_price=float(
                    row['recommended_price']
                ) if row['recommended_price'] != '' else None,
                category_id=float(
                    row['category_id']
                ) if row['category_id'] != '' else None,
                ozon_name=row['ozon_name'],
                name_1c=row['name_1c'],
                wb_name=row['wb_name'],
                ozon_article=row['ozon_article'],
                wb_article=row['wb_article'],
                ym_article=row['ym_article'],
                wb_article_td=row['wb_article_td']
            )
            db.add(record)
        await db.commit()
    async with aiofiles.open(
        '*your_path*',
        mode='r',
        newline='',
        encoding='UTF-8'
    ) as file:
        content = await file.read()
        content = content.replace('\r\n', '\n')
        reader = csv.DictReader(
            content.splitlines(),
            delimiter=';'
        )
        for row in reader:
            record = Dealer(
                id=int(row['id']),
                name=row['name']
            )
            db.add(record)
        await db.commit()
    async with aiofiles.open(
        '*your_path*',
        mode='r',
        newline='',
        encoding='UTF-8'
    ) as file:
        content = await file.read()
        content = content.replace('\r\n', '\n')
        reader = csv.DictReader(
            content.splitlines(),
            delimiter=';'
        )
        for row in reader:
            record = DealerPrice(
                id=int(row['id']),
                product_key=str(row['product_key']),
                product_name=row['product_name'],
                price=float(row['price']),
                product_url=row['product_url'],
                date=row['date'],
                dealer_id=int(row['dealer_id'])
            )
            db.add(record)
        await db.commit()
