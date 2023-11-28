from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, Field


### Схемы продуктов Дилера

#Базовая схема продукта Дилера
class DealerPriceBase(BaseModel):
    product_key: int
    price: float = Field(gt=0)
    product_url: str
    product_name: str
    date: str
    dealer_id: int


#Схема чтения продукта Дилера
class DealerPrice(DealerPriceBase):
    markup: bool
    id: int

    class Config:
        orm_mode = True

# Схема записи продукта Дилера
class DealerPriceCreate(DealerPriceBase):
    pass


### Схемы для модели Дилера

# Базовая схема Дилера
class DealerBase(BaseModel):
    name: str
    dealer_product: Optional[List[DealerPrice]] = []

# Схема чтения Дилера
class Dealer(DealerBase):
    id: int

    class Config:
        orm_mode = True

# Схема записи Дилера
class DealerCreate(DealerBase):
    pass 


### Схемы продукта Компании

#Базовая схема продукта Компании
class ProductBase(BaseModel):
    article: str
    ean_13: str
    name: str
    cost: float = Field(gt=0)
    min_recommended_price: float | None 
    recommended_price: float | None = Field(gt=0)
    category_id: float
    ozon_name: str
    name_1c: str
    wb_name: str 
    ozon_article: str 
    wb_article: str 
    ym_article_td: str

#Схема чтения продукта Компании
class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True

#Схема записи продукта компании
class ProductCreate(ProductBase):
    pass


###Схемы промежуточной таблицы связи продуктов

#Базовая схема для промежуточной модели
class ProductDealerKeyBase(BaseModel):
    key: int
    product_id: int
    dealer_id: int

    product: Product
    dealer: Dealer

#Схема чтения промежуточной модели 
class ProductDealerKey(BaseModel):
    date_markup: datetime
    id: int

    class Config:
        orm_mode = True

#Схема записи промежуточной модели
class ProductDealerKeyCreate(ProductDealerKey):
    pass
