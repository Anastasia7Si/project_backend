from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from typing import List

from .database import LocalSession, engine
from . import schemas, crud


app = FastAPI()


def get_db():
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()


### Продукт Дилера

# Эндпоинт получения продуктов Дилера
@app.get('/dealers/products/',
         response_model=List[schemas.DealerPrice])
def get_dealers_products(db: Session = Depends(get_db),
                         dealer_name: str = None,
                         limit: int = None):
    db_products_dealers = crud.get_dealers_prices(db, dealer_name, limit)
    if db_products_dealers is None:
        raise HTTPException(status_code=404, detail='Not found')
    return db_products_dealers


# Эндпоинт получения 1 продукта Дилера
@app.get('/dealers/products/{product_id}/',
         response_model=schemas.DealerPrice)
def get_dealer_product(product_id: int,
                       db: Session = Depends(get_db)):
    dealer_product = crud.get_dealer_price(db, product_id)
    if dealer_product is None:
        raise HTTPException(status_code=404, detail='Not found')
    return dealer_product


# Эндпоинт записи продукта Дилера
@app.post('/dealers/products/',
          response_model=schemas.DealerPrice)
def create_dealer_product(dealer_product: schemas.DealerPriceCreate,
                          db: Session = Depends(get_db)):
    return crud.create_dealer_price(db, dealer_product)


### Дилер

# Эндпоинт для получения списка Дилеров
@app.get('/dealers/',
         response_model=List[schemas.Dealer])
def get_dealers(db: Session = Depends(get_db),
                limit: int = None):
    db_dealers = crud.get_dealers(db, limit)
    if db_dealers is None:
        raise HTTPException(status_code=404, detail='Not found')
    return db_dealers


# Эндпоинт для получения 1 Дилера
@app.get('/dealers/{dealer_id}/',
         response_model=schemas.Dealer)
def get_dealer(dealer_id: int,
               db: Session = Depends(get_db)):
    db_dealer = crud.get_dealer(db, dealer_id)
    if db_dealer is None:
        raise HTTPException(status_code=404, detail='Not found')
    return db_dealer


# Эндпоинт для записи Дилера в БД
@app.post('/dealers/',
          response_model=schemas.Dealer)
def create_dealer(dealer: schemas.DealerCreate,
                  db: Session = Depends(get_db)):
    return crud.create_dealer(db, dealer)


### Продукты Компании

# Эндпоинт получения продуктов Компании
@app.get('/company/products/',
         response_model=List[schemas.Product])
def get_company_product(db: Session = Depends(get_db),
                        limit: int = None):
    company_products = crud.get_company_products(db, limit)
    if company_products is None:
        raise HTTPException(status_code=404, detail='Not found')
    return company_products


# Эндпоинт получения 1 продукта Компании
@app.get('/company/product/{product_id}/',
         response_model=schemas.Product)
def get_one_company_product(product_id: int,
                            db: Session = Depends(get_db)):
    company_product = crud.get_company_product(db, product_id)
    if company_product is None:
        raise HTTPException(status_code=404, detail='Not found')
    return company_product


# Эндпоинт записи продукта Компании
@app.post('/company/products/',
          response_model=schemas.Product)
def create_company_product(product: schemas.ProductCreate,
                           db: Session = Depends(get_db)):
    return crud.create_company_product(db, product)
