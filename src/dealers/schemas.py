from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel

from ..company.schemas import ProductForDealer
from .enum import AllowStatus


class DealerPriceBase(BaseModel):
    product_key: str
    price: float
    product_url: str
    product_name: str
    date: str
    dealer_id: int


class DealerPrice(DealerPriceBase):
    status: AllowStatus | None = None
    product_id: int | None
    product: ProductForDealer | None
    serial_number: int | None
    date_status: datetime | None
    id: int

    class Config:
        orm_mode = True


class DealerBase(BaseModel):
    name: str
    dealer_product: Optional[List[DealerPrice]] = []


class Dealer(DealerBase):
    id: int

    class Config:
        orm_mode = True
