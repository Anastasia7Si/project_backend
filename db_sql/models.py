from sqlalchemy import (Column, TIMESTAMP, Float, ForeignKey, Integer,
                        String, Boolean)
from sqlalchemy.orm import relationship
from datetime  import datetime

from .database import Base


#Модель Дилера
class Dealer(Base):
    __tablename__ = 'marketing_dealer'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))

    dealer_product = relationship('DealerPrice')


#Модель продукта Дилера
class DealerPrice(Base):
    __tablename__ = 'marketing_dealerprice'

    id = Column(Integer, primary_key=True)
    product_key = Column(Integer, unique=True)
    price = Column(Float)
    product_url = Column(String, nullable=True)
    product_name = Column(String(150), nullable=False)
    date = Column(String, nullable=False)
    dealer_id = Column(ForeignKey('marketing_dealer.id'), nullable=False)
    markup = Column(Boolean, default=False)

    dealer = relationship('Dealer')


#Модель продукта Компании
class Product(Base):
    __tablename__ = 'marketing_product'

    id = Column(Integer, primary_key=True)
    article = Column(String(30))
    ean_13 = Column(String(15), nullable=True)
    name = Column(String(150), nullable=True)
    cost = Column(Float, nullable=True)
    min_recommended_price = Column(Float, nullable=True)
    recommended_price = Column(Float, nullable=True)
    category_id = Column(Float, nullable=True)
    ozon_name = Column(String(150), nullable=True)
    name_1c = Column(String(150), nullable=True)
    wb_name = Column(String(150), nullable=True)
    ozon_article = Column(String(30), nullable=True)
    wb_article = Column(String(30), nullable=True)
    ym_article_td = Column(String(30), nullable=True)


#Модель соответствия продуктов
class ProductDealerKey(Base):
    __tablename__ = 'marketing_productdealerkey'

    id = Column(Integer, primary_key=True)
    date_markup = Column(TIMESTAMP, nullable=False, default=datetime.utcnow)
    key = Column(Integer, ForeignKey('marketing_dealerprice.id'))
    product_id = Column(Integer, ForeignKey('marketing_product.id'))
    dealer_id = Column(Integer, ForeignKey('marketing_dealer.id'))

    product = relationship('Product')
    dealer = relationship('Dealer')
