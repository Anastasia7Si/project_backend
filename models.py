from sqlalchemy import (Column, create_engine, DateTime, Float, ForeignKey,
                        Integer, MetaData, String, URL)
from sqlalchemy.orm import DeclarativeBase, relationship

metadata = MetaData()

engine = create_engine(
    "postgresql+psycopg2://'user':'password'@localhost/'name_db'"
    )


class Base(DeclarativeBase):
    pass


class Dealers(Base):
    __tablename__ = 'marketing_dealer'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))


class DealerPrice(Base):
    __tablename__ = 'marketing_dealerprice'

    id = Column(Integer, primary_key=True)
    product_key = Column(Integer, unique=True)
    price = Column(Float)
    product_url = Column(URL, nullable=True)
    product_name = Column(String(150))
    date = Column(DateTime)
    dealer_id = Column(ForeignKey('marketing_dealer.id'))

    dealer = relationship('Dealers')


class Product(Base):
    __tablename__ = 'marketing_product'

    id = Column(Integer, primary_key=True)
    article = Column(String(30))
    ean_13 = Column(String(13), nullable=True)
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


class ProductDealerKey(Base):
    __tablename__ = 'marketing_productdealerkey'

    key = Column(ForeignKey('marketing_dealerprice.id'))
    product_id = Column(ForeignKey('marketing_product.id'))
    dealer_id = Column(ForeignKey('marketing_dealer.id'))

    product = relationship('Product')
    dealer = relationship('Dealer')


metadata.create_all(engine)
