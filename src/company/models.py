from sqlalchemy import (Column, Float, Integer,
                        String)


from ..database import Base


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
