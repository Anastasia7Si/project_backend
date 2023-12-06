from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel

from .enum import AllowStatus
from ..company.schemas import ProductForDealer
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
    product: ProductForDealer | None
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
