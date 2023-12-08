import csv
import aiofiles

from src.dealers.models import Dealer, DealerPrice
from sqlalchemy.ext.asyncio import AsyncSession

from . import models


async def load_csv(db: AsyncSession):
    async with aiofiles.open(
        '/app/csv/marketing_product.csv',
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
        '/app/csv/marketing_dealerprice.csv',
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
        '/app/csv/marketing_dealer.csv',
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
