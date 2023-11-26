from sqlalchemy.orm import Session

from .models import Dealer, DealerPrice, Product
from .schemas import DealerCreate, DealerPriceCreate


#Получение Дилера
def get_dealer(db: Session, dealer_id: int):
    return db.query(Dealer).filter(Dealer.id == dealer_id).first()


#Запись Дилера в БД
def create_dealer(db: Session, dealer: DealerCreate):
    db_dealer = Dealer(**dealer.model_dump())
    db.add(db_dealer)
    db.commit()
    db.refresh(db_dealer)
    return db_dealer


#Получение продукта Дилера
def get_dealer_price(db: Session, price_id: int):
    return db.query(DealerPrice).filter(DealerPrice.id == price_id).first()


#Запись продукта Дилера в БД
def create_dealer_price(db: Session, dealer_price: DealerPriceCreate):
    db_dealer_price = DealerPrice(**dealer_price.model_dump())
    db.add(db_dealer_price)
    db.commit()
    db.refresh(db_dealer_price)
    return db_dealer_price


#Получение продукта Компании
def get_product(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()
