from datetime import datetime
from sqlalchemy import (TIMESTAMP, Column, Float, ForeignKey, Integer,
                        String)
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import ENUM as pgEnum


from ..database import Base


# Модель Дилера
class Dealer(Base):
    __tablename__ = 'marketing_dealer'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))

    dealer_product = relationship('DealerPrice', lazy='joined')


# Модель продукта Дилера
class DealerPrice(Base):
    __tablename__ = 'marketing_dealerprice'

    id = Column(Integer, primary_key=True)
    product_key = Column(Integer, unique=True)
    price = Column(Float)
    product_url = Column(String, nullable=True)
    product_name = Column(String(150), nullable=False)
    date = Column(String, nullable=False)
    dealer_id = Column(ForeignKey('marketing_dealer.id'), nullable=False)
    status = Column(pgEnum('markup', 'unclaimed', 'postponed', 'waiting', name='status_type'), default='waiting', nullable=True)

    dealer = relationship('Dealer', lazy='joined')


# Модель соответствия продуктов
class ProductDealerKey(Base):
    __tablename__ = 'marketing_productdealerkey'

    id = Column(Integer, primary_key=True)
    date_markup = Column(TIMESTAMP, nullable=False, default=datetime.utcnow)
    key = Column(Integer, ForeignKey('marketing_dealerprice.id'))
    product_id = Column(Integer, ForeignKey('marketing_product.id'))
    dealer_id = Column(Integer, ForeignKey('marketing_dealer.id'))

    product = relationship('Product', lazy='joined')
    dealer = relationship('Dealer', lazy='joined')
