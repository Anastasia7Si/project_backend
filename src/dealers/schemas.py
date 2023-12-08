from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel

from ..company.schemas import ProductForDealer
from .enum import AllowStatus


class DealerPriceBase(BaseModel):
    """Базовая схема продукта Дилера."""

    product_key: str
    price: float
    product_url: str
    product_name: str
    date: str
    dealer_id: int


class DealerPrice(DealerPriceBase):
    """Схема продукта Дилера."""

    status: AllowStatus | None = None
    product_id: int | None
    product: ProductForDealer | None
    serial_number: int | None
    date_status: datetime | None
    id: int

    class Config:
        orm_mode = True


class DealerBase(BaseModel):
    """Базовая схема Дилера."""

    name: str
    dealer_product: Optional[List[DealerPrice]] = []


class Dealer(DealerBase):
    """Схема продукта Дилера."""

    id: int

    class Config:
        orm_mode = True
