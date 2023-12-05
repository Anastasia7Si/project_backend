from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel

from .enum import AllowStatus

# ## Схемы продуктов Дилера


# Базовая схема продукта Дилера
class DealerPriceBase(BaseModel):
    product_key: str
    price: float
    product_url: str
    product_name: str
    date: str
    dealer_id: int


# Схема чтения продукта Дилера
class DealerPrice(DealerPriceBase):
    status: AllowStatus | None = None
    product_id: int | None
    serial_number: int | None
    date_status: datetime | None
    id: int

    class Config:
        orm_mode = True


# Схема записи продукта Дилера
class DealerPriceCreate(DealerPriceBase):
    pass


# ## Схемы для модели Дилера

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

# ##Схемы промежуточной таблицы связи продуктов

# Базовая схема для промежуточной модели
class ProductDealerKeyBase(BaseModel):
    product_id: int
    dealer_id: int
    serial_number: int

# Схема чтения промежуточной модели
class ProductDealerKey(ProductDealerKeyBase):
    key: int
    date_markup: datetime
    id: int

    product: int
    dealer: int

    class Config:
        orm_mode = True


# Схема записи промежуточной модели
class ProductDealerKeyCreate(ProductDealerKeyBase):
    pass


