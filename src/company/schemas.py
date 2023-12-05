from pydantic import BaseModel
from typing import List
# ## Схемы продукта Компании
from ..dealers.schemas import DealerPrice

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
    dealer_products: List[DealerPrice] | None = None

    class Config:
        orm_mode = True


# Схема записи продукта компании
class ProductCreate(ProductBase):
    pass
