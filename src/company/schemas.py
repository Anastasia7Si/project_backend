from pydantic import BaseModel
from typing import List


# Базовая схема продукта Компании
class ProductBase(BaseModel):
    article: str
    ean_13: str | None
    name: str | None
    cost: float | None 
    recommended_price: float | None
    category_id: float | None
    ozon_name: str | None
    name_1c: str | None
    wb_name: str | None
    ozon_article: str | None
    wb_article_td: str | None
    ym_article: str | None


# Схема чтения продукта Компании
class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True


class ProductShort(BaseModel):
    id: int
    article: str
    name_1c: str | None


class ProductForDealer(BaseModel):
    name_1c: str


# Схема записи продукта компании
class ProductCreate(ProductBase):
    pass
