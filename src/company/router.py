from fastapi import APIRouter
from . import utils, schemas
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, HTTPException

from typing import List


from ..database import get_async_session


router = APIRouter(
    prefix='/company',
    tags=['Tags']
)


### Продукты Компании

#Эндпоинт получения продуктов Компании НАДО БУДЕТ ПОДКЛЮЧИТЬ К ML
@router.get('/products/', 
            response_model=List[schemas.Product])
async def get_company_product(dealer_product_id: int = None, 
                              db: AsyncSession = Depends(get_async_session), 
                              limit: int = None):
    company_products = await utils.get_company_products(db, limit)
    if company_products is None:
        raise HTTPException(status_code=404, detail='Not found')
    return company_products


#Эндпоинт получения 1 продукта Компании
@router.get('/products/{product_id}/', 
            response_model=schemas.Product)
async def get_one_company_product(product_id: int, 
                            db: AsyncSession = Depends(get_async_session)):
    company_product = await utils.get_company_product(db, product_id)
    if company_product is None:
        raise HTTPException(status_code=404, detail='Not found')
    return company_product


#Эндпоинт записи продукта Компании
@router.post('/products/', 
             response_model=schemas.Product)
async def create_company_product(product: schemas.ProductCreate, 
                           db: AsyncSession = Depends(get_async_session)):
    return await utils.create_company_product(db, product)
