from typing import List

from pydantic import BaseModel


# Схемы для модели продукта Дилера
class DealerPriceBase(BaseModel):
    product_key: int
    price: float
    product_url: str
    product_name: str
    date: str
    dealer_id: int


class DealerPrice(DealerPriceBase):
    id: int

    class Config:
        orm_mode = True


class DealerPriceCreate(DealerPriceBase):
    pass


# Схемы для модели Дилера
class DealerBase(BaseModel):
    name: str


class Dealer(DealerBase):
    id: int
    dealer_product: List[DealerPrice]

    class Config:
        orm_mode = True


class DealerCreate(DealerBase):
    pass


# Схемы для модели продукта Компании
class Product(BaseModel):
    id: int
    arcticle: str
    ean_13: str
    name: str
    cost: float
    min_recommended_price: float
    recommended_price: float
    category_id: float
    ozon_name: str
    name_1c: str
    wb_name: str
    ozon_article: str
    wb_article: str
    ym_article_td: str

    class Config:
        orm_mode = True


class ProductCreate(BaseModel):
    pass


# Схема для промежуточной таблицы связи продуктов
class ProductDealerKey(BaseModel):
    id: int
    key: int
    product_id: int
    dealer_id: int

    product: Product
    dealer: Dealer

    class Config:
        orm_mode = True


class ProductDealerKeyCreate(ProductDealerKey):
    pass
