from sqlalchemy.orm import Session

from . import models, schemas


# CRUD для Дилера

# Получение Дилера
def get_dealer(db: Session, dealer_id: int):
    return db.query(models.Dealer).filter(
        models.Dealer.id == dealer_id).first()


# Получение списка Дилеров
def get_dealers(db: Session, limit: int):
    return db.query(models.Dealer).limit(limit).all()


# Запись Дилера в БД
def create_dealer(db: Session, dealer: schemas.DealerCreate):
    db_dealer = models.Dealer(**dealer.model_dump())
    db.add(db_dealer)
    db.commit()
    db.refresh(db_dealer)
    return db_dealer


### CRUD для продуктов Дилера

# Получение продуктов Дилеров
def get_dealers_prices(db: Session, dealer_name: str, limit: int):
    if dealer_name:
        return db.query(
            models.DealerPrice
        ).join(
            models.Dealer
        ).filter(
            models.Dealer.name == dealer_name
        ).limit(limit)
    return db.query(models.DealerPrice).limit(limit).all()


# Получение продукта Дилера
def get_dealer_price(db: Session, price_id: int):
    return db.query(
        models.DealerPrice
    ).filter(
        models.DealerPrice.id == price_id
    ).first()


# Запись продукта Дилера в БД
def create_dealer_price(db: Session, dealer_price: schemas.DealerPrice):
    db_dealer_price = models.DealerPrice(**dealer_price.model_dump())
    db.add(db_dealer_price)
    db.commit()
    db.refresh(db_dealer_price)
    return db_dealer_price


### CRUD

# Получение продуктов Компании
def get_company_products(db: Session, limit: int):
    return db.query(models.Product).limit(limit)


# Получение продукта Компании
def get_company_product(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id)


# Запись продукта Компании
def create_company_product(db: Session, product: schemas.ProductCreate):
    company_product = models.Product(**product.model_dump())
    db.add(company_product)
    db.commit()
    db.refresh(company_product)
    return company_product
